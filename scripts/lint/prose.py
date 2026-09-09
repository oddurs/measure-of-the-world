"""Check the manuscript against the rules in docs/styleguide.md and quality.md.

These are mechanical checks only. They find violations of rules the project
has already decided on; they do not judge whether a paragraph is any good.
That is the structural critique's job.

Every finding names a file, a line and the rule it breaks, so the report can
be worked through top to bottom.

Run: .venv/bin/python3 scripts/lint/prose.py [chapters/04.tex ...]
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SRC = PROJECT_ROOT / "src"
OUT = PROJECT_ROOT / "review" / "critique" / "prose-lint.md"

# Rules the style guide states outright.
CONTRACTIONS = re.compile(
    r"\b(?:don't|doesn't|didn't|isn't|aren't|wasn't|weren't|can't|couldn't|"
    r"won't|wouldn't|shouldn't|hasn't|haven't|hadn't|it's|that's|there's|"
    r"we're|we've|we'll|they're|they've|you're|I'm|let's)\b", re.I)

# The guide names these explicitly: always spell the concept out.
BANNED_ABBREVIATIONS = {
    r"\bRA\b": "right ascension",
    r"\bDec\.?\b(?!ember)": "declination",
    r"\bLST\b": "local sidereal time (define once, then use consistently)",
}

HEDGES = re.compile(
    r"\b(?:arguably|somewhat|rather|quite|fairly|relatively|perhaps|possibly|"
    r"presumably|seemingly|apparently|essentially|basically|virtually|"
    r"more or less|to some extent)\b", re.I)

THROAT_CLEARING = re.compile(
    r"^(?:It (?:is|was) (?:important|worth|interesting|notable|clear|"
    r"significant)[^.]*(?:that|to)\b|"
    r"(?:Of course|Indeed|In fact|Notably|Importantly|Needless to say)\b|"
    r"There (?:is|are|was|were) (?:a |an |some |no )?\w+ (?:that|which)\b)", re.I)

# "see Chapter 12" with no local explanation is the guide's named failure mode.
BARE_FORWARD_REF = re.compile(r"\(?\s*see\s+(?:also\s+)?(?:\\cref\{[^}]*\}|Chapter~?\s*\d+)\s*\)?[.,;]")

VAGUE_QUANTIFIER = re.compile(
    r"\b(?:many|several|numerous|various|a number of|countless|"
    r"a great deal of|substantial|significant)\s+"
    r"(?:years|observations|astronomers|instruments|measurements|errors|times)\b", re.I)

LONG_SENTENCE = 35
VERY_LONG_SENTENCE = 45

PASSIVE = re.compile(
    r"\b(?:was|were|is|are|been|being|be)\s+(?:\w+ly\s+)?"
    r"(?:\w+(?:ed|en))\b(?:\s+by\b)?", re.I)


def strip(text: str) -> list[tuple[int, str]]:
    """Return (line number, prose) pairs, with LaTeX machinery removed."""
    out = []
    in_env = 0
    in_display = False
    skip = re.compile(r"\\begin\{(figure|table|tabular|tabularx|longtable|equation|align|gather|verbatim|sidewaystable)")
    end = re.compile(r"\\end\{(figure|table|tabular|tabularx|longtable|equation|align|gather|verbatim|sidewaystable)")
    for number, raw in enumerate(text.splitlines(), 1):
        line = re.sub(r"(?<!\\)%.*", "", raw)
        if skip.search(line):
            in_env += 1
        if in_env:
            if end.search(line):
                in_env -= 1
            continue
        # Display math often spans several lines, so it has to be tracked
        # across them. Symbol names inside it are notation, not prose, and
        # linting them produces nothing but false positives.
        line = re.sub(r"\\\[.*?\\\]", " ", line)
        if in_display:
            if r"\]" in line:
                in_display = False
                line = line.split(r"\]", 1)[1]
            else:
                continue
        if r"\[" in line:
            before, _, _ = line.partition(r"\[")
            in_display = True
            line = before
        if re.match(r"\s*\\(?:chapter|section|subsection|label|index|input)", line):
            continue
        line = re.sub(r"\$[^$]*\$", " NUM ", line)
        for _ in range(3):
            line = re.sub(r"\\(?:emph|textit|textbf|textsc|texttt)\{([^{}]*)\}", r"\1", line)
        line = re.sub(r"\\(?:footnote|cite[a-z]*|textcite|label|index|ref|cref|Cref)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", line)
        line = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])*", " ", line)
        line = re.sub(r"[{}~]", " ", line)
        line = re.sub(r"\s+", " ", line).strip()
        if len(line) > 20:
            out.append((number, line))
    return out


def sentences_of(line: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", line) if s.strip()]


def check_file(path: Path) -> list[tuple[int, str, str, str]]:
    findings = []
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = strip(text)

    openers = Counter()
    for number, line in lines:
        for match in CONTRACTIONS.finditer(line):
            findings.append((number, "contraction",
                             f"'{match.group(0)}' — the guide forbids contractions", line))
        for pattern, expansion in BANNED_ABBREVIATIONS.items():
            for match in re.finditer(pattern, line):
                findings.append((number, "abbreviation",
                                 f"'{match.group(0)}' — write {expansion}", line))
        for match in HEDGES.finditer(line):
            findings.append((number, "hedge",
                             f"'{match.group(0)}' — cut or replace with a figure", line))
        for match in VAGUE_QUANTIFIER.finditer(line):
            findings.append((number, "vague quantity",
                             f"'{match.group(0)}' — a book about measurement should say how many", line))
        if BARE_FORWARD_REF.search(line):
            findings.append((number, "bare cross-reference",
                             "'see Chapter N' with no local explanation; the guide "
                             "asks for enough context that the reader need not turn", line))

        for sentence in sentences_of(line):
            words = len(sentence.split())
            if words > VERY_LONG_SENTENCE:
                findings.append((number, "very long sentence",
                                 f"{words} words", sentence))
            elif words > LONG_SENTENCE:
                findings.append((number, "long sentence", f"{words} words", sentence))
            if THROAT_CLEARING.match(sentence):
                findings.append((number, "throat-clearing",
                                 "opens without advancing the argument", sentence))
            first = sentence.split()[:1]
            if first:
                openers[first[0].lower()] += 1

    for word, count in openers.most_common(4):
        if count >= 12 and word not in {"the", "a", "an", "this", "in", "it"}:
            findings.append((0, "repeated opener",
                             f"{count} sentences begin with '{word}'", ""))

    passive_hits = sum(len(PASSIVE.findall(line)) for _, line in lines)
    total_sentences = sum(len(sentences_of(line)) for _, line in lines)
    if total_sentences and passive_hits / total_sentences > 0.42:
        findings.append((0, "passive density",
                         f"{passive_hits} passive constructions in ~{total_sentences} "
                         f"sentences ({passive_hits / total_sentences:.0%})", ""))
    return findings


def main() -> int:
    wanted = sys.argv[1:]
    paths = []
    for pattern in ("chapters/*.tex", "appendices/*.tex", "frontmatter/*.tex"):
        paths.extend(sorted(SRC.glob(pattern)))
    if wanted:
        paths = [p for p in paths if any(w in str(p) for w in wanted)]

    report = ["# Prose lint", "",
              "Mechanical checks against `docs/styleguide.md`. Generated by "
              "`scripts/lint/prose.py`; do not edit by hand.", ""]
    grand_total = 0
    by_rule: Counter = Counter()

    for path in paths:
        findings = check_file(path)
        grand_total += len(findings)
        for _, rule, _, _ in findings:
            by_rule[rule] += 1
        if not findings:
            continue
        report.append(f"## {path.relative_to(PROJECT_ROOT)} — {len(findings)} findings")
        report.append("")
        for number, rule, detail, context in sorted(findings):
            where = f"line {number}" if number else "file"
            report.append(f"- **{rule}** ({where}): {detail}")
            if context:
                snippet = context if len(context) < 190 else context[:187] + "..."
                report.append(f"  > {snippet}")
        report.append("")

    summary = ["## Summary", "", "| Rule | Count |", "|---|---:|"]
    for rule, count in by_rule.most_common():
        summary.append(f"| {rule} | {count} |")
    summary += [f"| **total** | **{grand_total}** |", ""]
    report[3:3] = summary

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(report), encoding="utf-8")

    for rule, count in by_rule.most_common():
        print(f"{count:5d}  {rule}")
    print(f"{grand_total:5d}  total across {len(paths)} files")
    print(f"written to {OUT.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
