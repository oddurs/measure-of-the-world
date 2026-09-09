"""Minimal BibTeX reader and writer for references.bib.

Deliberately not a general BibTeX parser. It handles the subset this project
uses: @book and @article entries with brace-delimited field values, one
field per line. It preserves entry order and unknown fields so a rewrite is
a small diff rather than a reformat of the whole file.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BIB_PATH = PROJECT_ROOT / "src" / "bibliography" / "references.bib"

ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", re.S)
FIELD_RE = re.compile(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*(?=\n\s*\w+\s*=|\s*$)", re.S)


@dataclass
class Entry:
    key: str
    kind: str
    fields: dict = field(default_factory=dict)

    def get(self, name: str, default: str = "") -> str:
        value = self.fields.get(name, default)
        # Collapse the whitespace introduced by wrapped field values.
        return re.sub(r"\s+", " ", value).strip()

    @property
    def authors(self) -> list[str]:
        """Author surnames, in order. Handles 'Last, First and Last, First'."""
        raw = self.get("author") or self.get("editor")
        if not raw:
            return []
        out = []
        for part in re.split(r"\s+and\s+", raw):
            part = part.strip()
            if not part:
                continue
            out.append(part.split(",")[0].strip() if "," in part else part.split()[-1])
        return out

    def search_string(self) -> str:
        bits = [self.get("title")]
        if self.authors:
            bits.append(self.authors[0])
        if self.get("year"):
            bits.append(self.get("year"))
        return " ".join(b for b in bits if b)


def load(path: Path = BIB_PATH) -> list[Entry]:
    text = path.read_text(encoding="utf-8")
    entries = []
    for kind, key, body in ENTRY_RE.findall(text):
        fields = {name.lower(): value for name, value in FIELD_RE.findall(body)}
        entries.append(Entry(key=key, kind=kind.lower(), fields=fields))
    return entries


def cited_keys(project_root: Path = PROJECT_ROOT) -> dict[str, list[str]]:
    """Map each cited key to the source files that cite it."""
    cite_re = re.compile(r"\\(?:text|paren|foot|auto)?cite[a-z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}")
    out: dict[str, list[str]] = {}
    for tex in sorted((project_root / "src").rglob("*.tex")):
        text = tex.read_text(encoding="utf-8", errors="ignore")
        for group in cite_re.findall(text):
            for key in group.split(","):
                key = key.strip()
                if key:
                    out.setdefault(key, []).append(
                        str(tex.relative_to(project_root))
                    )
    return out
