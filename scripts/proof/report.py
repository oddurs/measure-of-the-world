"""Turn the LaTeX build log and the finished PDF into a layout defect list.

The build log knows exactly where every overfull line and oversized float
is, but it reports them by an internal file stack that is unreadable at a
glance. This resolves each warning back to a source file and line, sorts by
severity, and adds the checks a printer cares about: page geometry, embedded
fonts, and the effective resolution of every placed image.

Run: .venv/bin/python3 scripts/proof/report.py
Writes review/layout/pages.md.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOG = PROJECT_ROOT / "build" / "tmp" / "main.log"
PDF = PROJECT_ROOT / "build" / "out" / "measure-of-the-world.pdf"
OUT = PROJECT_ROOT / "review" / "layout" / "pages.md"

# Anything worse than this is worth a person's time; below it, microtype has
# usually absorbed the damage and the line just looks slightly loose.
SERIOUS_PT = 5.0

# Mixam: 6x9 trim inside a 6.25x9.25 stock, in PostScript points.
EXPECTED_STOCK = (450, 666)
EXPECTED_TRIM = (432, 648)
MIN_DPI = 300


def parse_log() -> tuple[list[dict], list[str]]:
    """Walk the log's parenthesised file stack to attribute each warning."""
    if not LOG.exists():
        return [], [f"no build log at {LOG.relative_to(PROJECT_ROOT)}; run make build first"]

    text = LOG.read_text(encoding="utf-8", errors="replace")
    findings: list[dict] = []
    page = 0

    # Tracking the log's parenthesis stack is unreliable: the log interleaves
    # arbitrary text containing unbalanced parentheses, so the stack drifts and
    # most warnings end up unattributed. Instead, remember every manuscript file
    # the log opens, and attribute a warning to the most recent one whose length
    # can actually contain the reported line number.
    opens: list[tuple[int, str, int]] = []  # (position in log, path, line count)
    for match in re.finditer(r"\((\.{0,2}/[\w./-]+\.tex)", text):
        path = match.group(1)
        candidate = (PROJECT_ROOT / "src" / path.lstrip("./")).resolve()
        if not candidate.exists():
            continue
        length = len(candidate.read_text(encoding="utf-8", errors="ignore").splitlines())
        opens.append((match.start(), path, length))

    def attribute(position: int, line_number: int | None) -> str:
        for start, path, length in reversed(opens):
            if start >= position:
                continue
            if line_number is None or line_number <= length:
                return path
        return "?"

    token = re.compile(
        r"\[(\d+)"                                                  # page shipped
        r"|Overfull \\hbox \(([\d.]+)pt too wide\) in paragraph at lines (\d+)--(\d+)"
        r"|Overfull \\vbox \(([\d.]+)pt too high\) has occurred while \\output is active"
        r"|Underfull \\hbox \(badness (\d+)\) in paragraph at lines (\d+)--(\d+)"
        r"|Float too large for page by ([\d.]+)pt on input line (\d+)"
        r"|LaTeX Warning: (`?h' float specifier changed to `ht'|Float too large)"
    )

    for match in token.finditer(text):
        shipped, hbox_pt, hb_from, hb_to, vbox_pt, badness, ub_from, ub_to, float_pt, float_line, _ = match.groups()
        if shipped:
            page = int(shipped)
        else:
            reported = hb_from or ub_from or float_line
            source = attribute(match.start(), int(reported) if reported else None)
            if hbox_pt:
                findings.append({
                    "kind": "overfull hbox", "pt": float(hbox_pt),
                    "file": source, "lines": f"{hb_from}-{hb_to}", "page": page,
                })
            elif vbox_pt:
                findings.append({
                    "kind": "overfull vbox", "pt": float(vbox_pt),
                    "file": source, "lines": "", "page": page,
                })
            elif badness:
                findings.append({
                    "kind": "underfull hbox", "pt": 0.0,
                    "file": source, "lines": f"{ub_from}-{ub_to}", "page": page,
                    "detail": f"badness {badness}",
                })
            elif float_pt:
                findings.append({
                    "kind": "float too large", "pt": float(float_pt),
                    "file": source, "lines": float_line, "page": page,
                })

    notes = []
    for pattern, message in (
        (r"LaTeX Warning: Reference `([^']*)' on page", "undefined reference"),
        (r"LaTeX Warning: Citation `([^']*)' on page", "undefined citation"),
        (r"LaTeX Warning: There were multiply-defined labels", "multiply-defined labels"),
    ):
        hits = re.findall(pattern, text)
        if hits:
            notes.append(f"{message}: {len(hits)} ({', '.join(sorted(set(hits))[:6])})")
    return findings, notes


def run(command: list[str]) -> str:
    if not shutil.which(command[0]):
        return ""
    try:
        return subprocess.run(command, capture_output=True, text=True, timeout=180).stdout
    except Exception:
        return ""


def check_pdf() -> list[str]:
    if not PDF.exists():
        return [f"no PDF at {PDF.relative_to(PROJECT_ROOT)}"]
    lines = []

    info = run(["pdfinfo", "-box", str(PDF)])
    if info:
        pages = re.search(r"Pages:\s+(\d+)", info)
        if pages:
            count = int(pages.group(1))
            lines.append(f"Pages: {count}"
                         + ("" if count % 2 == 0 else "  **odd; a printed book needs an even page count**"))
        for name, expected in (("MediaBox", EXPECTED_STOCK), ("TrimBox", EXPECTED_TRIM)):
            box = re.search(rf"{name}:\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)", info)
            if not box:
                lines.append(f"{name}: **not set** (Mixam reads the TrimBox to place the finished page)")
                continue
            x0, y0, x1, y1 = (float(v) for v in box.groups())
            width, height = round(x1 - x0), round(y1 - y0)
            ok = (width, height) == expected
            lines.append(
                f"{name}: {width} x {height} pt "
                + ("(correct)" if ok else f"**expected {expected[0]} x {expected[1]}**")
            )

    fonts = run(["pdffonts", str(PDF)])
    if fonts:
        rows = [r for r in fonts.splitlines()[2:] if r.strip()]
        not_embedded = [r.split()[0] for r in rows if len(r.split()) > 3 and r.split()[3] == "no"]
        lines.append(f"Fonts: {len(rows)} used, "
                     + ("all embedded" if not not_embedded
                        else f"**{len(not_embedded)} not embedded: {', '.join(not_embedded[:5])}**"))

    images = run(["pdfimages", "-list", str(PDF)])
    if images:
        low = []
        for row in images.splitlines()[2:]:
            parts = row.split()
            if len(parts) < 14:
                continue
            try:
                x_dpi, y_dpi = float(parts[12]), float(parts[13])
            except ValueError:
                continue
            if min(x_dpi, y_dpi) < MIN_DPI:
                low.append((int(parts[0]), min(x_dpi, y_dpi)))
        total = len([r for r in images.splitlines()[2:] if r.strip()])
        if low:
            worst = sorted(low, key=lambda p: p[1])[:8]
            lines.append(f"Images: {total} placed, **{len(low)} below {MIN_DPI} dpi**; "
                         "worst: " + ", ".join(f"p{page} at {dpi:.0f} dpi" for page, dpi in worst))
        else:
            lines.append(f"Images: {total} placed, all at or above {MIN_DPI} dpi")
    return lines


def main() -> int:
    findings, notes = parse_log()
    serious = [f for f in findings if f["pt"] >= SERIOUS_PT]
    serious.sort(key=lambda f: -f["pt"])

    report = ["# Layout report", "",
              "Generated by `scripts/proof/report.py` from the build log and the "
              "finished PDF. Do not edit by hand.", "",
              "## Printer checks", ""]
    report += [f"- {line}" for line in check_pdf()]
    report.append("")

    if notes:
        report += ["## Build warnings", ""] + [f"- {n}" for n in notes] + [""]

    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding["kind"]] = counts.get(finding["kind"], 0) + 1
    report += ["## Boxes", "", "| Kind | Count |", "|---|---:|"]
    for kind, count in sorted(counts.items(), key=lambda kv: -kv[1]):
        report.append(f"| {kind} | {count} |")
    report.append("")

    report += [
        f"## Needing attention ({len(serious)} over {SERIOUS_PT:g}pt)", "",
        "Sorted worst first. An overfull line sets type past the margin, so at "
        "these sizes it is visible on the page.", "",
        "| Overflow | Kind | Source | Lines | Page |", "|---:|---|---|---|---:|",
    ]
    for finding in serious:
        report.append(
            f"| {finding['pt']:.1f}pt | {finding['kind']} | `{finding['file']}` | "
            f"{finding['lines']} | {finding['page'] or '?'} |"
        )
    report.append("")

    by_file: dict[str, int] = {}
    for finding in findings:
        by_file[finding["file"]] = by_file.get(finding["file"], 0) + 1
    report += ["## All boxes by file", "", "| File | Count |", "|---|---:|"]
    for name, count in sorted(by_file.items(), key=lambda kv: -kv[1]):
        report.append(f"| `{name}` | {count} |")
    report.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(report), encoding="utf-8")

    print(f"{len(findings)} boxes, {len(serious)} over {SERIOUS_PT:g}pt")
    for line in check_pdf():
        print(f"  {line}")
    print(f"written to {OUT.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
