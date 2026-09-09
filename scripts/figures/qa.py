#!/usr/bin/env python3
"""Layout QA for the generated book figures.

Runs every ``chNN.py`` figure script with ``common.save_figure`` intercepted so
the live ``Figure`` object can be inspected with a real renderer before it is
written to disk.  Three classes of problem are reported:

0. **Text spilling out of the shape that holds it** -- a node label wider than
   its circle, which on a filled node means white type on white paper.
1. **Overlapping text** -- any two visible, non-empty ``matplotlib.text.Text``
   artists whose window extents intersect by more than ``OVERLAP_TOL_PT`` points
   in *both* axes.  Texts that belong to the same legend or table are skipped,
   since those frames legitimately pack their own labels.
2. **Too-small print type** -- the drawn point size scaled by the reduction the
   figure undergoes when ``\\includegraphics[width=0.NN\\textwidth]`` places it in
   the 4.5 inch text block.  Anything under ``MIN_PRINT_PT`` is a blocker.
3. **Bad geometry** -- saved PNGs with an extreme aspect ratio or huge pixel
   dimensions.

Usage::

    .venv/bin/python3 scripts/figures/qa.py           # all chapters
    .venv/bin/python3 scripts/figures/qa.py 9 10 23   # only these chapters

Exits non-zero when any BLOCKER is found so it can gate CI.
"""

from __future__ import annotations

import os
import re
import runpy
import math
import struct
import sys
import traceback
from dataclasses import dataclass, field
from pathlib import Path

FIGURE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = FIGURE_DIR.parent.parent
CHAPTER_TEX_DIR = PROJECT_ROOT / "src" / "chapters"
GENERATED_DIR = PROJECT_ROOT / "src" / "figures" / "generated"
REPORT_PATH = PROJECT_ROOT / "review" / "layout" / "figure-qa.md"

# The 6x9 book has a 4.5 inch text block.
TEXT_BLOCK_IN = 4.5
# Default assumed placement width for a figure that no .tex file references.
DEFAULT_WIDTH_FRAC = 0.85

OVERLAP_TOL_PT = 1.5
OVERFLOW_TOL_PT = 1.0
MIN_PRINT_PT = 7.0
# A figure drawn much wider than it is printed reduces its type below the
# floor; STYLE.md asks for a drawn width no more than this times the printed.
MAX_DRAW_RATIO = 1.6
# A patch bigger than this share of the axes is a backdrop, not a label holder.
MAX_CONTAINER_AREA = 0.30
MAX_ASPECT = 2.5
MIN_ASPECT = 0.5
MAX_PIXELS = 4000

# The figure scripts render their labels with LaTeX.
_TEXLIVE = Path.home() / "texlive" / "2026" / "bin" / "universal-darwin"
if _TEXLIVE.is_dir() and str(_TEXLIVE) not in os.environ.get("PATH", ""):
    os.environ["PATH"] = f"{_TEXLIVE}{os.pathsep}{os.environ.get('PATH', '')}"

sys.path.insert(0, str(FIGURE_DIR))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.legend import Legend  # noqa: E402
from matplotlib.patches import Ellipse, Patch  # noqa: E402
from matplotlib.table import Table  # noqa: E402
from matplotlib.text import Text  # noqa: E402

import common  # noqa: E402


# --------------------------------------------------------------------------
# Placement widths from the LaTeX sources
# --------------------------------------------------------------------------

_INCLUDE_RE = re.compile(
    r"\\includegraphics\s*(?:\[(?P<opts>[^\]]*)\])?\s*\{(?P<path>[^}]*)\}",
    re.S,
)
_WIDTH_RE = re.compile(r"width\s*=\s*(?P<num>[0-9]*\.?[0-9]+)?\s*\\(?:text|line|column)width")


def load_placements() -> dict[str, float]:
    """Map ``ch09-error-sources`` -> fraction of the text block it is drawn at."""
    placements: dict[str, float] = {}
    for tex in sorted(CHAPTER_TEX_DIR.glob("*.tex")):
        source = tex.read_text(encoding="utf-8", errors="replace")
        for match in _INCLUDE_RE.finditer(source):
            path = match.group("path").strip()
            stem = Path(path).stem
            if not stem.startswith("ch"):
                continue
            opts = match.group("opts") or ""
            width_match = _WIDTH_RE.search(opts)
            if width_match is None:
                continue
            num = width_match.group("num")
            placements[stem] = float(num) if num else 1.0
    return placements


# --------------------------------------------------------------------------
# PNG geometry
# --------------------------------------------------------------------------


def png_size(path: Path) -> tuple[int, int] | None:
    """Return (width, height) in pixels by reading the PNG IHDR chunk."""
    try:
        with path.open("rb") as handle:
            header = handle.read(24)
    except OSError:
        return None
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return int(width), int(height)


# --------------------------------------------------------------------------
# Findings
# --------------------------------------------------------------------------


@dataclass
class Finding:
    figure: str
    kind: str
    severity: str
    score: float
    detail: str


@dataclass
class FigureReport:
    name: str
    chapter: int
    width_frac: float
    drawn_w_in: float
    drawn_h_in: float
    saved_w_in: float
    saved_h_in: float
    min_print_pt: float
    n_texts: int
    draw_ratio: float = 0.0
    findings: list[Finding] = field(default_factory=list)


REPORTS: list[FigureReport] = []
ERRORS: list[tuple[str, str]] = []


def _describe(text: Text) -> str:
    raw = text.get_text().replace("\n", " / ").strip()
    if len(raw) > 44:
        raw = raw[:41] + "..."
    return raw


def _container_groups(fig) -> list[set[int]]:
    """Ids of Text artists that live inside the same legend or table."""
    groups: list[set[int]] = []
    for container in fig.findobj(Legend) + fig.findobj(Table):
        ids = {id(t) for t in container.findobj(Text) if t.get_text().strip()}
        if len(ids) > 1:
            groups.append(ids)
    return groups


def _offscreen_tick_labels(fig) -> set[int]:
    """Tick labels for locations outside the view interval are never drawn.

    ``findobj`` still returns them, at stale positions, so they have to be
    excluded or they masquerade as collisions.
    """
    excluded: set[int] = set()
    for axes in fig.axes:
        for axis in (axes.xaxis, axes.yaxis):
            try:
                low, high = sorted(axis.get_view_interval())
                ticks = list(axis.get_major_ticks()) + list(axis.get_minor_ticks())
            except Exception:
                continue
            span = high - low
            eps = span * 1e-6 if span else 0.0
            for tick in ticks:
                loc = tick.get_loc()
                if loc is None or low - eps <= loc <= high + eps:
                    continue
                for label in (tick.label1, tick.label2):
                    if label is not None:
                        excluded.add(id(label))
    return excluded


def _collect_texts(fig, renderer):
    """Visible, non-empty Text artists with their display-space bboxes."""
    out = []
    seen: set[int] = set()
    offscreen = _offscreen_tick_labels(fig)
    for text in fig.findobj(Text):
        if id(text) in offscreen:
            continue
        if id(text) in seen:
            continue
        seen.add(id(text))
        if not text.get_text() or not text.get_text().strip():
            continue
        if not text.get_visible():
            continue
        axes = text.axes
        if axes is not None and not axes.get_visible():
            continue
        try:
            # Annotation.get_window_extent unions in the arrow patch; call the
            # base implementation so only the glyphs are measured.
            bbox = Text.get_window_extent(text, renderer=renderer)
        except Exception:
            continue
        if bbox.width <= 0 or bbox.height <= 0:
            continue
        out.append((text, bbox))
    return out


def _source(text: Text, legend_ids: set[int]) -> str:
    """Where a Text came from, so a too-small size can be traced to its call."""
    if id(text) in legend_ids:
        return "legend"
    axes = text.axes
    if axes is not None:
        if text is axes.title or text in (axes._left_title, axes._right_title):
            return "title"
        for axis, tag in ((axes.xaxis, "xtick"), (axes.yaxis, "ytick")):
            if text is axis.label:
                return tag.replace("tick", "label")
            if text in axis.get_ticklabels() or text is axis.offsetText:
                return tag
    return "text"


def _overflow_points(text: Text, bbox, patch, renderer, px_to_pt: float):
    """How far a text's box escapes the patch that holds it, in points."""
    corners = [(bbox.x0, bbox.y0), (bbox.x1, bbox.y0),
               (bbox.x0, bbox.y1), (bbox.x1, bbox.y1)]
    if isinstance(patch, Ellipse):
        # The path is a unit circle at the origin; the patch transform is what
        # places and scales it, so the origin maps to the display centre.
        centre = patch.get_transform().transform((0.0, 0.0))
        half_w = patch.get_window_extent(renderer).width / 2
        half_h = patch.get_window_extent(renderer).height / 2
        if half_w <= 0 or half_h <= 0:
            return 0.0
        worst = 0.0
        for x, y in corners:
            radial = math.hypot((x - centre[0]) / half_w, (y - centre[1]) / half_h)
            if radial > 1.0:
                worst = max(worst, (radial - 1.0) * min(half_w, half_h))
        return worst * px_to_pt
    pbox = patch.get_window_extent(renderer)
    escape = max(pbox.x0 - bbox.x0, bbox.x1 - pbox.x1,
                 pbox.y0 - bbox.y0, bbox.y1 - pbox.y1, 0.0)
    return escape * px_to_pt


def _containers(axes, renderer):
    """Patches small enough to be reading as a label holder rather than a backdrop."""
    try:
        axes_box = axes.get_window_extent(renderer)
    except Exception:
        return []
    limit = axes_box.width * axes_box.height * MAX_CONTAINER_AREA
    found = []
    for patch in axes.findobj(Patch):
        if patch is axes.patch or not patch.get_visible():
            continue
        try:
            box = patch.get_window_extent(renderer)
        except Exception:
            continue
        if box.width <= 0 or box.height <= 0:
            continue
        if box.width * box.height > limit:
            continue
        found.append(patch)
    return found


def _axis_aligned(text: Text) -> bool:
    try:
        rot = float(text.get_rotation()) % 90.0
    except (TypeError, ValueError):
        return True
    return rot < 0.5 or rot > 89.5


def check_figure(fig, name: str, chapter: int, placements: dict[str, float]) -> None:
    full_name = f"ch{chapter:02d}-{name}"
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    dpi = fig.dpi
    px_to_pt = 72.0 / dpi

    drawn_w_in, drawn_h_in = fig.get_size_inches()
    try:
        tight = fig.get_tightbbox(renderer)
        saved_w_in, saved_h_in = float(tight.width), float(tight.height)
    except Exception:
        saved_w_in, saved_h_in = float(drawn_w_in), float(drawn_h_in)
    if saved_w_in <= 0:
        saved_w_in = float(drawn_w_in)
    if saved_h_in <= 0:
        saved_h_in = float(drawn_h_in)

    width_frac = placements.get(full_name, DEFAULT_WIDTH_FRAC)
    printed_w_in = width_frac * TEXT_BLOCK_IN
    # The saved PNG is the tight-cropped region, so that is what gets scaled to
    # printed_w_in on the page.
    scale = printed_w_in / saved_w_in

    texts = _collect_texts(fig, renderer)
    groups = _container_groups(fig)
    legend_ids = {id(t) for lg in fig.findobj(Legend) for t in lg.findobj(Text)}

    report = FigureReport(
        name=full_name,
        chapter=chapter,
        width_frac=width_frac,
        drawn_w_in=float(drawn_w_in),
        drawn_h_in=float(drawn_h_in),
        saved_w_in=saved_w_in,
        saved_h_in=saved_h_in,
        min_print_pt=float("inf"),
        n_texts=len(texts),
    )

    # --- font sizes -------------------------------------------------------
    smallest: dict[float, str] = {}
    for text, _ in texts:
        drawn_pt = float(text.get_fontsize())
        printed_pt = drawn_pt * scale
        if printed_pt < report.min_print_pt:
            report.min_print_pt = printed_pt
        if printed_pt < MIN_PRINT_PT:
            key = round(printed_pt, 2)
            smallest.setdefault(key, (drawn_pt, _source(text, legend_ids), _describe(text)))
    if report.min_print_pt == float("inf"):
        report.min_print_pt = 0.0
    for printed_pt, (drawn_pt, source, sample) in sorted(smallest.items()):
        report.findings.append(
            Finding(
                figure=full_name,
                kind="font",
                severity="BLOCKER",
                score=MIN_PRINT_PT - printed_pt,
                detail=(
                    f"{printed_pt:.1f}pt in print (drawn {drawn_pt:.1f}pt, "
                    f"x{scale:.2f}, {source}) e.g. \u201c{sample}\u201d"
                ),
            )
        )

    # --- text escaping the shape that holds it ----------------------------
    containers_by_axes = {}
    for text, box in texts:
        axes = text.axes
        if axes is None:
            continue
        # A node caption is set centre/centre inside its shape. A map or band
        # label is anchored to a point and may run past the fill it sits on,
        # which is not a defect.
        if text.get_horizontalalignment() != 'center' or \
                text.get_verticalalignment() != 'center':
            continue
        if id(axes) not in containers_by_axes:
            containers_by_axes[id(axes)] = _containers(axes, renderer)
        anchor = text.get_transform().transform(text.get_unitless_position())
        worst_patch, worst = None, 0.0
        for patch in containers_by_axes[id(axes)]:
            try:
                if not patch.contains_point(anchor):
                    continue
                # Only a label centred in the shape is one the shape holds; a
                # caption that happens to sit on a landmass fill is not.
                pbox = patch.get_window_extent(renderer)
                offset = math.hypot(anchor[0] - (pbox.x0 + pbox.x1) / 2,
                                    anchor[1] - (pbox.y0 + pbox.y1) / 2)
                if offset > 0.25 * math.hypot(pbox.width, pbox.height):
                    continue
                escape = _overflow_points(text, box, patch, renderer, px_to_pt)
            except Exception:
                continue
            if escape > worst:
                worst_patch, worst = patch, escape
        if worst_patch is not None and worst > OVERFLOW_TOL_PT:
            report.findings.append(
                Finding(
                    figure=full_name,
                    kind="overflow",
                    severity="BLOCKER",
                    score=worst,
                    detail=(
                        f"\u201c{_describe(text)}\u201d escapes its "
                        f"{type(worst_patch).__name__.lower()} by {worst:.1f}pt"
                    ),
                )
            )

    # --- overlaps ---------------------------------------------------------
    tol_px = OVERLAP_TOL_PT / px_to_pt
    for i in range(len(texts)):
        text_a, box_a = texts[i]
        for j in range(i + 1, len(texts)):
            text_b, box_b = texts[j]
            dx = min(box_a.x1, box_b.x1) - max(box_a.x0, box_b.x0)
            dy = min(box_a.y1, box_b.y1) - max(box_a.y0, box_b.y0)
            if dx <= tol_px or dy <= tol_px:
                continue
            if any(id(text_a) in g and id(text_b) in g for g in groups):
                continue
            rotated = not (_axis_aligned(text_a) and _axis_aligned(text_b))
            severity = "WARN" if rotated else "BLOCKER"
            note = " [rotated, bbox approximate]" if rotated else ""
            report.findings.append(
                Finding(
                    figure=full_name,
                    kind="overlap",
                    severity=severity,
                    score=min(dx, dy) * px_to_pt,
                    detail=(
                        f"\u201c{_describe(text_a)}\u201d \u21c4 "
                        f"\u201c{_describe(text_b)}\u201d "
                        f"({dx * px_to_pt:.1f}\u00d7{dy * px_to_pt:.1f}pt){note}"
                    ),
                )
            )

    ratio = saved_w_in / printed_w_in if printed_w_in else 0.0
    report.draw_ratio = ratio
    if ratio > MAX_DRAW_RATIO:
        report.findings.append(
            Finding(
                figure=full_name,
                kind="canvas",
                severity="WARN",
                score=ratio,
                detail=(
                    f"drawn {saved_w_in:.2f}in for a {printed_w_in:.2f}in slot "
                    f"({ratio:.2f}x); draw at about "
                    f"{printed_w_in * MAX_DRAW_RATIO:.1f}in"
                ),
            )
        )

    REPORTS.append(report)


def check_png(report: FigureReport) -> None:
    path = GENERATED_DIR / f"{report.name}.png"
    size = png_size(path)
    if size is None:
        return
    width, height = size
    aspect = width / height if height else 0.0
    if aspect > MAX_ASPECT or (aspect and aspect < MIN_ASPECT):
        report.findings.append(
            Finding(
                figure=report.name,
                kind="aspect",
                severity="WARN",
                score=abs(aspect - 1.0),
                detail=f"aspect {aspect:.2f} ({width}\u00d7{height}px)",
            )
        )
    if width > MAX_PIXELS or height > MAX_PIXELS:
        report.findings.append(
            Finding(
                figure=report.name,
                kind="pixels",
                severity="WARN",
                score=max(width, height) / MAX_PIXELS,
                detail=f"{width}\u00d7{height}px exceeds {MAX_PIXELS}px",
            )
        )


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------


def run_chapter(script: Path, placements: dict[str, float]) -> None:
    real_save = common._REAL_SAVE_FIGURE

    def intercepting_save(fig, name: str, chapter: int):
        try:
            check_figure(fig, name, chapter, placements)
        except Exception:
            ERRORS.append((f"ch{chapter:02d}-{name}", traceback.format_exc()))
        return real_save(fig, name, chapter)

    common.save_figure = intercepting_save
    try:
        runpy.run_path(str(script), run_name="__main__")
    except Exception:
        ERRORS.append((script.name, traceback.format_exc()))
    finally:
        common.save_figure = real_save
        plt.close("all")


SEVERITY_RANK = {"BLOCKER": 0, "WARN": 1}


def write_report(chapters: list[int]) -> tuple[int, int]:
    rows: list[Finding] = []
    for report in REPORTS:
        rows.extend(report.findings)
    rows.sort(key=lambda f: (SEVERITY_RANK[f.severity], {"overflow": 0, "overlap": 1, "font": 2}.get(f.kind, 3), -f.score))

    blockers = sum(1 for f in rows if f.severity == "BLOCKER")
    warnings = sum(1 for f in rows if f.severity == "WARN")

    lines = [
        "# Figure layout QA",
        "",
        f"Generated by `scripts/figures/qa.py` over "
        f"{'all chapters' if not chapters else 'chapters ' + ', '.join(str(c) for c in chapters)}.",
        "",
        f"- Figures checked: **{len(REPORTS)}**",
        f"- Blockers: **{blockers}**",
        f"- Warnings: **{warnings}**",
        "",
        f"A blocker is a text/text collision deeper than {OVERLAP_TOL_PT}pt in both axes, "
        f"or type that prints below {MIN_PRINT_PT}pt. Printed size is the drawn point size "
        f"times `(width_frac x {TEXT_BLOCK_IN}in) / saved_png_width_in`, using the tight-cropped "
        "width that `savefig(bbox_inches='tight')` actually writes.",
        "",
        "Each font row names where the text came from: `text` for an `ax.text`/`annotate` "
        "call, `legend` for a legend entry, `title`, `xlabel`/`ylabel`, `xtick`/`ytick`. "
        "A `legend` or `title` row drawn at a round size (8, 9, 10pt) has bypassed "
        "`common.PRINT_FONT_SCALE`, which only reaches sizes set through "
        "`Text.set_fontsize`.",
        "",
        "An overlap between two rotated labels is reported as a WARN, not a BLOCKER: "
        "window extents are axis aligned, so a rotated pair can be flagged when the "
        "glyphs do not actually touch.",
        "",
        "## Findings (worst first)",
        "",
        "| Severity | Figure | Kind | Detail |",
        "| --- | --- | --- | --- |",
    ]
    if rows:
        for finding in rows:
            detail = finding.detail.replace("|", "\\|")
            lines.append(f"| {finding.severity} | `{finding.figure}` | {finding.kind} | {detail} |")
    else:
        lines.append("| - | - | - | No problems found. |")

    lines += [
        "",
        "## Per-figure geometry",
        "",
        "| Figure | Placed at | Printed (in) | Saved (in) | Drawn/printed | Min print pt | Texts | Issues |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for report in sorted(REPORTS, key=lambda r: (-len(r.findings), r.chapter, r.name)):
        lines.append(
            f"| `{report.name}` "
            f"| {report.width_frac:.2f}\\textwidth "
            f"| {report.width_frac * TEXT_BLOCK_IN:.2f} "
            f"| {report.saved_w_in:.2f}x{report.saved_h_in:.2f} "
            f"| {report.draw_ratio:.2f} "
            f"| {report.min_print_pt:.1f} "
            f"| {report.n_texts} "
            f"| {len(report.findings)} |"
        )

    if ERRORS:
        lines += ["", "## Errors", ""]
        for where, tb in ERRORS:
            lines += [f"### {where}", "", "```", tb.strip(), "```", ""]

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return blockers, warnings


def main(argv: list[str]) -> int:
    chapters = [int(a) for a in argv if a.isdigit()]
    scripts = sorted(FIGURE_DIR.glob("ch[0-9][0-9].py"))
    if chapters:
        wanted = {f"ch{c:02d}.py" for c in chapters}
        scripts = [s for s in scripts if s.name in wanted]
    if not scripts:
        print("No figure scripts matched.", file=sys.stderr)
        return 2

    placements = load_placements()
    if not hasattr(common, "_REAL_SAVE_FIGURE"):
        common._REAL_SAVE_FIGURE = common.save_figure

    cwd = os.getcwd()
    os.chdir(FIGURE_DIR)
    try:
        for script in scripts:
            print(f"--- {script.name}")
            run_chapter(script, placements)
    finally:
        os.chdir(cwd)

    for report in REPORTS:
        check_png(report)

    blockers, warnings = write_report(chapters)

    print()
    print(f"Figures checked : {len(REPORTS)}")
    print(f"Blockers        : {blockers}")
    print(f"Warnings        : {warnings}")
    print(f"Report          : {REPORT_PATH.relative_to(PROJECT_ROOT)}")
    if ERRORS:
        print(f"Script errors   : {len(ERRORS)} (see report)")
    worst = [f for r in REPORTS for f in r.findings if f.severity == "BLOCKER"]
    worst.sort(key=lambda f: -f.score)
    for finding in worst[:15]:
        print(f"  {finding.figure}: {finding.kind}: {finding.detail}")
    return 1 if (blockers or ERRORS) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
