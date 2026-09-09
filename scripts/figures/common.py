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
    """Patch matplotlib.text.Text.set_fontsize so all sizes scale together.

    Chapter scripts pass fontsize=8/9/10 to hundreds of ax.text() calls; changing
    rcParams alone would leave those annotations too small in print.
    """
    from matplotlib import text as mtext
    if getattr(mtext.Text, "_print_scaled", False):
        return
    original = mtext.Text.set_fontsize

    def set_fontsize(self, fontsize):
        if isinstance(fontsize, (int, float)):
            fontsize = fontsize * PRINT_FONT_SCALE
        return original(self, fontsize)

    mtext.Text.set_fontsize = set_fontsize
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
    fig.savefig(OUTPUT_DIR / filename, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"Generated: {filename}")
