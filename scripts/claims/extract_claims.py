"""Extract checkable claims from the manuscript into per-file ledgers.

A claim is a sentence asserting something a reader could check against a
source: a date, a measurement, a named person doing a named thing, a
quotation, or a superlative. Prose that only explains or transitions is not
a claim and is skipped.

Output: review/claims/<name>.yaml, one record per claim:

    - id: ch04-017
      type: measurement
      status: unverified
      text: "..."
      source: ""
      note: ""

Existing ledgers are updated, never overwritten: a claim whose text is
unchanged keeps its status, source and note. Claims whose sentence has
disappeared from the manuscript are marked `stale` rather than deleted, so
that verification work is never silently lost.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = PROJECT_ROOT / "review" / "claims"

# Sentences shorter than this are usually fragments left by stripping macros.
MIN_CHARS = 45

MONTHS = (
    "January|February|March|April|May|June|July|August|September|October|"
    "November|December"
)

# Ordered: the first pattern that matches names the claim's type.
CLAIM_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("quotation", re.compile(r"[\u201c\u201d\"']{1}[^\u201c\u201d\"']{25,}[\u201c\u201d\"']{1}")),
    ("date", re.compile(rf"\b(?:{MONTHS})\s+\d{{1,2}},?\s+\d{{4}}\b|\b\d{{1,2}}\s+(?:{MONTHS})\s+\d{{4}}\b")),
    ("date", re.compile(r"\b1[5-9]\d{2}\b|\b20[0-2]\d\b")),
    ("measurement", re.compile(
        r"\b\d+(?:\.\d+)?\s*(?:arc\s?-?(?:seconds?|minutes?)|arcsec|arcmin|"
        r"degrees?|feet|foot|inches|inch|metres?|meters?|kilometres?|kilometers?|"
        r"miles|nautical miles|seconds?|minutes?|hours?|days?|years?|"
        r"kilograms?|pounds?|tons?|nanoseconds?|milliseconds?|microseconds?)\b"
    )),
    ("measurement", re.compile(r"\$[^$]*\\qty|\\SI\{|\\num\{")),
    ("superlative", re.compile(
        r"\b(?:the first|the last|the largest|the smallest|the longest|"
        r"the shortest|the only|the best|the earliest|the greatest|"
        r"for the first time|never before|unprecedented)\b", re.I)),
    ("attribution", re.compile(
        r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+"
        r"(?:showed|proved|discovered|invented|designed|built|published|"
        r"observed|measured|calculated|argued|proposed|reported|announced|"
        r"appointed|founded|established|demonstrated|concluded|determined)\b")),
]

# LaTeX constructs to remove entirely, innermost content included.
DROP_ENVIRONMENTS = (
    "figure", "table", "tabular", "tabularx", "longtable", "equation",
    "align", "gather", "itemize", "enumerate", "description", "verbatim",
    "sidewaystable", "styledtable", "tablenotes",
)


def clean_cell(text: str) -> str:
    """Reduce a single table cell or list item to readable plain text."""
    for _ in range(4):
        text = re.sub(r"\\(?:emph|textit|textbf|textsc|texttt|mathrm|text)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:label|index|cite[a-z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", text)
    text = re.sub(r"\$\\pm\s*([^$]*)\$", r"±\1", text)
    text = re.sub(r"\$([^$]*)\$", r"\1", text)
    text = re.sub(r"\\times", "x", text)
    text = text.replace(r"\&", "&").replace(r"\%", "%").replace(r"\$", "$")
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])*", " ", text)
    text = re.sub(r"[{}~]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def table_claims(raw: str) -> list[tuple[str, str]]:
    """One claim per data row of every tabular environment.

    Reference tables carry the densest factual content in the book -- an
    instrument's date, maker, aperture and accuracy are four checkable
    assertions on one line -- and stripping the environments would drop all
    of them. The row is emitted with its column headers so a checker can see
    what each value means.
    """
    out = []
    pattern = re.compile(
        r"\\begin\{(tabular|tabularx|longtable)\*?\}(?:\[[^\]]*\])?"
        r"(?:\{[^{}]*\})?\s*\{[^{}]*\}(.*?)\\end\{\1\*?\}",
        re.S,
    )
    for _, body in pattern.findall(raw):
        rows = []
        for line in re.split(r"\\\\", body):
            line = re.sub(r"\\(?:top|mid|bottom)rule|\\hline|\\cmidrule(?:\([^)]*\))?\{[^}]*\}", " ", line)
            # Split on column separators only. An escaped \& is a literal
            # ampersand inside a cell ("Troughton \& Simms") and splitting on
            # it shifts every column to its right.
            if not re.search(r"(?<!\\)&", line):
                continue
            cells = [clean_cell(c) for c in re.split(r"(?<!\\)&", line)]
            if any(cells):
                rows.append(cells)
        if len(rows) < 2:
            continue
        header, data = rows[0], rows[1:]
        for cells in data:
            filled = [(header[i] if i < len(header) else f"col{i+1}", c)
                      for i, c in enumerate(cells) if c and c not in "-\u2014\u2013"]
            if len(filled) < 2:
                continue
            subject = filled[0][1]
            rest = "; ".join(f"{name}: {value}" for name, value in filled[1:] if name)
            if not rest:
                continue
            out.append(("tabular", f"{subject} \u2014 {rest}"))
    return out


def item_claims(raw: str) -> list[tuple[str, str]]:
    """One claim per \\item[label] entry, as used by the chronologies."""
    out = []
    for label, body in re.findall(r"\\item\[([^\]]*)\]((?:[^\\]|\\(?!item|end\{))*)", raw):
        label = clean_cell(label)
        body = clean_cell(body)
        if not body or len(body) < 25:
            continue
        out.append(("chronology", f"{label}: {body}" if label else body))
    return out


def strip_latex(text: str) -> str:
    """Reduce LaTeX to plain sentences, keeping character offsets irrelevant."""
    text = re.sub(r"(?<!\\)%.*", "", text)
    for env in DROP_ENVIRONMENTS:
        text = re.sub(rf"\\begin\{{{env}\*?\}}.*?\\end\{{{env}\*?\}}", " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " MATH ", text, flags=re.S)
    # Footnotes carry their own claims; pull their prose up into the body.
    for _ in range(4):
        text = re.sub(r"\\footnote\{((?:[^{}]|\{[^{}]*\})*)\}", r" (\1) ", text)
    text = re.sub(r"\\(?:text|paren|foot|auto)?cite[a-z]*\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", text)
    text = re.sub(r"\\(?:label|ref|cref|Cref|index|gls|glsadd|includegraphics|caption)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", text)
    text = re.sub(r"\\(?:chapter|section|subsection|subsubsection)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", text)
    # Keep the words inside emphasis and small caps.
    for _ in range(4):
        text = re.sub(r"\\(?:emph|textit|textbf|textsc|texttt|underline)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])*", " ", text)
    text = text.replace("---", "\u2014").replace("--", "\u2013")
    text = re.sub(r"[{}]", " ", text)
    text = re.sub(r"~", " ", text)
    return re.sub(r"[ \t]+", " ", text)


ABBREV = re.compile(r"\b(?:Mr|Mrs|Dr|St|Prof|Rev|Sir|vs|i\.e|e\.g|cf|ca|c|fig|Fig|No|Vol|pp|approx)\.$")


def sentences(text: str):
    for block in re.split(r"\n\s*\n", text):
        block = re.sub(r"\s+", " ", block).strip()
        if not block:
            continue
        parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\u201c\"(])", block)
        buffer = ""
        for part in parts:
            candidate = (buffer + " " + part).strip() if buffer else part
            if ABBREV.search(candidate) or re.search(r"\b\d\.$", candidate):
                buffer = candidate
                continue
            buffer = ""
            yield candidate


def classify(sentence: str) -> str | None:
    for name, pattern in CLAIM_PATTERNS:
        if pattern.search(sentence):
            return name
    return None


def parse_existing(path: Path) -> dict[str, dict]:
    """Read a previous ledger so verification work survives re-extraction."""
    if not path.exists():
        return {}
    records, current = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- id:"):
            current = {"id": line.split(":", 1)[1].strip()}
        elif current is not None and re.match(r"\s+\w+:", line):
            name, _, value = line.strip().partition(":")
            value = value.strip()
            if value.startswith('"') and value.endswith('"') and len(value) > 1:
                value = value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            current[name] = value
            if name == "text":
                records[value] = current
    return records


def yq(value: str) -> str:
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def process(tex: Path, prefix: str) -> tuple[int, int]:
    raw = tex.read_text(encoding="utf-8", errors="ignore")
    raw_nocomment = re.sub(r"(?<!\\)%.*", "", raw)
    text = strip_latex(raw)
    out_path = OUT_DIR / f"{prefix}.yaml"
    previous = parse_existing(out_path)

    claims, seen = [], set()
    for sentence in sentences(text):
        if len(sentence) < MIN_CHARS or sentence in seen:
            continue
        kind = classify(sentence)
        if not kind:
            continue
        seen.add(sentence)
        claims.append((kind, sentence))

    # Tables and dated lists hold the reference data and are always checkable,
    # so they bypass the prose classifier.
    for kind, claim in table_claims(raw_nocomment) + item_claims(raw_nocomment):
        if claim in seen:
            continue
        seen.add(claim)
        claims.append((kind, claim))

    lines = [
        f"# Claim ledger for {tex.relative_to(PROJECT_ROOT)}",
        "# Generated by scripts/claims/extract_claims.py; re-running preserves",
        "# status/source/note for claims whose text is unchanged.",
        "# status: unverified | verified | corrected | removed | stale",
        "",
    ]
    for index, (kind, sentence) in enumerate(claims, 1):
        record = previous.get(sentence, {})
        lines.append(f"- id: {prefix}-{index:03d}")
        lines.append(f"  type: {kind}")
        lines.append(f"  status: {record.get('status', 'unverified')}")
        lines.append(f"  text: {yq(sentence)}")
        lines.append(f"  source: {yq(record.get('source', ''))}")
        lines.append(f"  note: {yq(record.get('note', ''))}")
        lines.append("")

    carried = 0
    for sentence, record in previous.items():
        if sentence in seen or record.get("status", "unverified") == "unverified":
            continue
        carried += 1
        lines.append(f"- id: {record['id']}")
        lines.append(f"  type: {record.get('type', 'unknown')}")
        lines.append("  status: stale")
        lines.append(f"  text: {yq(sentence)}")
        lines.append(f"  source: {yq(record.get('source', ''))}")
        lines.append(f"  note: {yq('sentence no longer present; was ' + record.get('status', ''))}")
        lines.append("")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return len(claims), carried


def targets() -> list[tuple[Path, str]]:
    out = []
    for tex in sorted((PROJECT_ROOT / "src" / "chapters").glob("*.tex")):
        out.append((tex, f"ch{tex.stem}"))
    for tex in sorted((PROJECT_ROOT / "src" / "appendices").glob("*.tex")):
        out.append((tex, tex.stem.replace("appendix-", "app")))
    return out


def main() -> int:
    wanted = set(sys.argv[1:])
    total = 0
    for tex, prefix in targets():
        if wanted and prefix not in wanted:
            continue
        count, carried = process(tex, prefix)
        total += count
        extra = f"  (+{carried} stale)" if carried else ""
        print(f"{prefix:8s} {count:4d} claims{extra}")
    print(f"\n{total} claims across the selected files")
    print(f"written to {OUT_DIR.relative_to(PROJECT_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
