"""Shared utilities for matplotlib figure generation."""

from pathlib import Path
import matplotlib.pyplot as plt
import scienceplots

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "src" / "figures" / "generated"


def setup_style():
    """Configure consistent matplotlib style using SciencePlots."""
    # Use science style with LaTeX rendering for publication-quality typography
    plt.style.use(['science'])

    # Override with book-appropriate settings.
    #
    # Print scaling: the chapter scripts draw figures 6-8 inches wide, but the
    # 6x9 book has a 4.5 inch text block and most figures are placed at
    # 0.6-0.85\textwidth, so a figure is printed at roughly 0.45-0.7 of its
    # drawn size. The sizes below are chosen so that, after that reduction,
    # labels land at about 7-9pt on the page (the book's caption size is 9pt).
    plt.rcParams.update({
        'figure.figsize': (6, 4),
        'figure.dpi': 300,
        'font.family': 'serif',
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'legend.fontsize': 9,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'lines.linewidth': 2.0,
        'lines.markersize': 8,
        'axes.linewidth': 1.0,
        'grid.linewidth': 0.6,
        'grid.alpha': 0.3,
    })
    _install_print_font_scaling()


# Uniform enlargement applied to every numeric font size, whether it comes
# from rcParams or from an explicit fontsize= argument in a chapter script.
# Chosen so that an 8-10pt annotation drawn on a 7in-wide figure is still
# about 7-9pt after the figure is reduced to the 4.5in text block.
PRINT_FONT_SCALE = 1.45


def _install_print_font_scaling():
    """Scale every text size in a figure, whatever route it was set by.

    Chapter scripts pass fontsize=8/9/10 to hundreds of ax.text() calls, so
    changing rcParams alone would leave those annotations too small in print.
    Patching Text.set_fontsize catches those.

    Legends and axes titles do not go through that path: Legend builds its
    Text objects from a FontProperties instance, and FontProperties.set_size
    is what actually carries the number. Without patching it too, a legend
    written as legend(fontsize=8) reaches the page at about 4pt, which is how
    every legend in the book came to be unreadable while the annotations
    beside them were fine.
    """
    from matplotlib import text as mtext
    from matplotlib.font_manager import FontProperties

    if getattr(FontProperties, "_print_scaled", False):
        return

    original_size = FontProperties.set_size
    # Text.set_fontsize delegates to FontProperties.set_size, so scaling in
    # both places would apply the factor twice. This flag lets the outer call
    # hand off a value that is already scaled.
    guard = {"scaled": False}

    def set_size(self, size):
        # Only numeric sizes scale. Named sizes ("small", "large") resolve
        # against rcParams, which setup_style has already set for print.
        if isinstance(size, (int, float)) and not guard["scaled"]:
            size = size * PRINT_FONT_SCALE
        return original_size(self, size)

    original_set = mtext.Text.set_fontsize

    def set_fontsize(self, fontsize):
        if isinstance(fontsize, (int, float)):
            fontsize = fontsize * PRINT_FONT_SCALE
        guard["scaled"] = True
        try:
            return original_set(self, fontsize)
        finally:
            guard["scaled"] = False

    FontProperties.set_size = set_size
    mtext.Text.set_fontsize = set_fontsize
    FontProperties._print_scaled = True
    mtext.Text._print_scaled = True


def save_figure(fig, name: str, chapter: int):
    """Save figure with consistent naming convention.

    Args:
        fig: matplotlib Figure object
        name: descriptive name (e.g., 'longitude-error')
        chapter: chapter number (1-25)
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"ch{chapter:02d}-{name}.png"
    _drop_duplicate_title(fig, filename)
    # 350 rather than 300: a figure drawn near its printed size and then
    # placed at 0.9 of the measure can land a shade under 300 dpi on the page,
    # which is the printer's floor. 350 gives enough headroom to survive a
    # placement change without pushing the PDF past 30 MB.
    fig.savefig(OUTPUT_DIR / filename, bbox_inches='tight', dpi=350)
    plt.close(fig)
    print(f"Generated: {filename}")


def _drop_duplicate_title(fig, filename: str):
    """Remove a whole-figure title, which the LaTeX caption already carries.

    See figures/STYLE.md. A title inside the image repeats the caption at a
    different size and in a different typeface, and in a book it is the caption
    that readers and indexes use. It also competes for space with the legend,
    which is where several of the collisions in this set came from.

    Panel titles in multi-panel figures are left alone: they label which panel
    is which, and no caption can do that job.
    """
    axes = fig.get_axes()
    if len(axes) != 1:
        return
    title = axes[0].get_title()
    if title:
        axes[0].set_title("")
        print(f"  dropped in-figure title from {filename}: {title.splitlines()[0]!r}")


def _renderer_for(fig):
    """A renderer usable for measuring text before the figure is saved."""
    try:
        return fig.canvas.get_renderer()
    except AttributeError:
        fig.canvas.draw()
        return fig.canvas.get_renderer()


def place_timeline_labels(ax, entries, base_offset=0.30, lane_step=None,
                          pad_points=10.0, stem_gap=0.02, stem_width=1.5,
                          marker_size=8, draw_stems=True, baseline=0.0,
                          sides=(1, -1)):
    """Lay out event labels around a horizontal timeline without collisions.

    Timeline figures in this book cluster many events into a few years, so a
    simple above/below alternation overprints.  Each label is measured with a
    real renderer, then packed into the first lane -- stepping outwards from
    the axis, alternating above and below -- that has horizontal room for it.

    Args:
        ax: the axes holding the timeline (drawn along y=0).
        entries: sequence of dicts with ``x`` and ``text``; optional keys
            ``color``, ``fontsize``, ``fontweight``, ``marker``.
        base_offset: distance from the axis to the innermost lane, in data units.
        lane_step: distance between lanes; measured from the labels if omitted.
        pad_points: horizontal clearance required between neighbouring labels.
        stem_gap: gap left between the stem and its label.
        draw_stems: draw the connector from the axis to each label.
        baseline: y value the timeline is drawn at.
        sides: which sides labels may use -- ``(1, -1)`` for both, ``(1,)`` to
            keep every label above the line, ``(-1,)`` for below.

    Returns:
        ``(texts, y_min, y_max)`` -- the created Text artists and the vertical
        extent they occupy, so the caller can set y limits with headroom.
    """
    fig = ax.figure
    renderer = _renderer_for(fig)
    inv = ax.transData.inverted()
    pad_px = pad_points * fig.dpi / 72.0

    widths, heights = [], []
    for entry in entries:
        probe = ax.text(entry['x'], baseline, entry['text'],
                        fontsize=entry.get('fontsize', 8),
                        fontweight=entry.get('fontweight', 'normal'),
                        ha='center', va='center', alpha=0.0)
        bbox = probe.get_window_extent(renderer=renderer)
        (x0, y0), (x1, y1) = inv.transform([
            (bbox.x0 - pad_px / 2, bbox.y0),
            (bbox.x1 + pad_px / 2, bbox.y1),
        ])
        widths.append(abs(x1 - x0))
        heights.append(abs(y1 - y0))
        probe.remove()

    if lane_step is None:
        lane_step = max(heights) * 1.35 if heights else 0.25

    # Pack into lanes, working left to right so the rightmost edge used by a
    # lane is all we need to remember.
    order = sorted(range(len(entries)), key=lambda i: entries[i]['x'])
    occupied = {1: [], -1: []}
    assignment = {}
    for rank, index in enumerate(order):
        left = entries[index]['x'] - widths[index] / 2
        right = entries[index]['x'] + widths[index] / 2
        preferred = sides[rank % len(sides)]
        candidates = (preferred,) + tuple(s for s in sides if s != preferred)
        placed = False
        for side in candidates:
            for lane, edge in enumerate(occupied[side]):
                if left >= edge:
                    occupied[side][lane] = right
                    assignment[index] = (side, lane)
                    placed = True
                    break
            if placed:
                break
        if not placed:
            side = min(candidates, key=lambda s: len(occupied[s]))
            occupied[side].append(right)
            assignment[index] = (side, len(occupied[side]) - 1)

    texts = []
    y_min, y_max = 0.0, 0.0
    for index, entry in enumerate(entries):
        side, lane = assignment[index]
        y = baseline + side * (base_offset + lane * lane_step)
        color = entry.get('color', 'black')
        if draw_stems:
            ax.plot([entry['x'], entry['x']], [baseline, y - side * stem_gap],
                    color=color, linewidth=stem_width, zorder=1)
        if marker_size:
            ax.plot(entry['x'], baseline, entry.get('marker', 'o'), color=color,
                    markersize=marker_size, zorder=3)
        texts.append(ax.text(
            entry['x'], y, entry['text'],
            fontsize=entry.get('fontsize', 8),
            fontweight=entry.get('fontweight', 'normal'),
            ha='center', va='bottom' if side > 0 else 'top', color=color,
            zorder=4,
            # Stems from outer lanes cross labels sitting in inner ones.
            bbox=dict(boxstyle='square,pad=0.12', facecolor='white',
                      edgecolor='none', alpha=0.85)))
        y_max = max(y_max, y + heights[index] if side > 0 else y)
        y_min = min(y_min, y - heights[index] if side < 0 else y)
    return texts, y_min, y_max
