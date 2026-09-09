"""Resolve every bibliography entry against public catalogues.

Writes review/refs/verification.yaml with one record per key:

    status: resolved | ambiguous | not-found
    match:  what the catalogue returned, when a match was found
    checks: which fields agreed and which did not

Nothing here decides that an entry is wrong. It reports what the catalogues
say so a person can judge. An entry no catalogue knows about is not proof of
fabrication (obscure and very old works exist), but it is the shortlist that
has to be checked by hand.

Sources, all free and unauthenticated:
  Crossref     https://api.crossref.org       journal articles, some books
  OpenLibrary  https://openlibrary.org        books
  Google Books https://www.googleapis.com     books, good on older imprints

NASA ADS would be the right source for the historical astronomy journals but
needs an API key. Set ADS_TOKEN in the environment to enable it.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bib import BIB_PATH, PROJECT_ROOT, Entry, cited_keys, load  # noqa: E402

OUT_PATH = PROJECT_ROOT / "review" / "refs" / "verification.yaml"
USER_AGENT = "measure-of-the-world-bib-check/1.0 (academic bibliography verification)"

# Two titles count as the same work above this ratio. Set high enough that a
# different book by the same author does not match, low enough to tolerate
# subtitle and punctuation differences.
TITLE_MATCH = 0.72


def norm(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    text = re.sub(r"\b(the|a|an|of|and|on|in|for|to|its|his|her)\b", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def fetch(url: str, tries: int = 3) -> dict | None:
    for attempt in range(tries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=25) as response:
                return json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503):
                time.sleep(2 * (attempt + 1))
                continue
            return None
        except Exception:
            time.sleep(1 + attempt)
    return None


def query_crossref(entry: Entry) -> dict | None:
    params = {"query.bibliographic": entry.search_string(), "rows": "5"}
    if entry.get("journal"):
        params["query.container-title"] = entry.get("journal")
    data = fetch("https://api.crossref.org/works?" + urllib.parse.urlencode(params))
    if not data:
        return None
    best = None
    for item in data.get("message", {}).get("items", []):
        title = (item.get("title") or [""])[0]
        if not title:
            continue
        score = similarity(entry.get("title"), title)
        if best is None or score > best["score"]:
            issued = item.get("issued", {}).get("date-parts", [[None]])[0]
            best = {
                "source": "crossref",
                "score": round(score, 3),
                "title": title,
                "year": str(issued[0]) if issued and issued[0] else "",
                "authors": [
                    a.get("family", "") for a in item.get("author", []) if a.get("family")
                ],
                "doi": item.get("DOI", ""),
                "container": (item.get("container-title") or [""])[0],
            }
    return best


def query_openlibrary(entry: Entry) -> dict | None:
    params = {"q": entry.search_string(), "limit": "5", "fields": "title,author_name,first_publish_year,isbn,key"}
    data = fetch("https://openlibrary.org/search.json?" + urllib.parse.urlencode(params))
    if not data:
        return None
    best = None
    for item in data.get("docs", []):
        title = item.get("title", "")
        if not title:
            continue
        score = similarity(entry.get("title"), title)
        if best is None or score > best["score"]:
            best = {
                "source": "openlibrary",
                "score": round(score, 3),
                "title": title,
                "year": str(item.get("first_publish_year") or ""),
                "authors": item.get("author_name", [])[:4],
                "isbn": (item.get("isbn") or [""])[0],
                "url": "https://openlibrary.org" + item.get("key", ""),
            }
    return best


def query_googlebooks(entry: Entry) -> dict | None:
    params = {"q": entry.search_string(), "maxResults": "5"}
    data = fetch("https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode(params))
    if not data:
        return None
    best = None
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        title = info.get("title", "")
        if not title:
            continue
        if info.get("subtitle"):
            title_full = f"{title}: {info['subtitle']}"
        else:
            title_full = title
        score = max(
            similarity(entry.get("title"), title),
            similarity(entry.get("title"), title_full),
        )
        if best is None or score > best["score"]:
            best = {
                "source": "googlebooks",
                "score": round(score, 3),
                "title": title_full,
                "year": (info.get("publishedDate") or "")[:4],
                "authors": info.get("authors", [])[:4],
                "publisher": info.get("publisher", ""),
                "url": info.get("infoLink", ""),
            }
    return best


def query_ads(entry: Entry) -> dict | None:
    token = os.environ.get("ADS_TOKEN")
    if not token:
        return None
    params = {"q": f'title:"{entry.get("title")}"', "fl": "title,author,year,bibcode,doi", "rows": "5"}
    url = "https://api.adsabs.harvard.edu/v1/search/query?" + urllib.parse.urlencode(params)
    try:
        request = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT, "Authorization": f"Bearer {token}"}
        )
        with urllib.request.urlopen(request, timeout=25) as response:
            data = json.loads(response.read().decode("utf-8", "replace"))
    except Exception:
        return None
    best = None
    for doc in data.get("response", {}).get("docs", []):
        title = (doc.get("title") or [""])[0]
        score = similarity(entry.get("title"), title)
        if best is None or score > best["score"]:
            best = {
                "source": "ads",
                "score": round(score, 3),
                "title": title,
                "year": str(doc.get("year", "")),
                "authors": [a.split(",")[0] for a in doc.get("author", [])[:4]],
                "bibcode": doc.get("bibcode", ""),
                "doi": (doc.get("doi") or [""])[0],
            }
    return best


def check_agreement(entry: Entry, match: dict) -> list[str]:
    """Note where the entry and the catalogue record disagree."""
    problems = []
    entry_year, match_year = entry.get("year"), match.get("year", "")
    if entry_year and match_year and entry_year.isdigit() and match_year.isdigit():
        gap = abs(int(entry_year) - int(match_year))
        if gap > 2:
            problems.append(f"year: bib says {entry_year}, catalogue says {match_year}")
    surnames = {a.lower() for a in entry.authors}
    found = {a.split()[-1].lower() for a in match.get("authors", []) if a}
    if surnames and found and not (surnames & found):
        problems.append(
            f"author: bib says {'/'.join(sorted(surnames))}, "
            f"catalogue says {'/'.join(sorted(found))}"
        )
    return problems


def classify(entry: Entry, candidates: list[dict]) -> tuple[str, dict | None, list[str]]:
    candidates = [c for c in candidates if c]
    if not candidates:
        return "not-found", None, ["no catalogue returned any candidate"]
    best = max(candidates, key=lambda c: c["score"])
    if best["score"] < 0.55:
        return "not-found", best, [
            f"closest candidate scored {best['score']} ({best['source']}): {best['title']!r}"
        ]
    problems = check_agreement(entry, best)
    if best["score"] < TITLE_MATCH or problems:
        return "ambiguous", best, problems or [f"title similarity {best['score']}"]
    return "resolved", best, []


def yaml_escape(value: str) -> str:
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    entries = load(BIB_PATH)
    citations = cited_keys()
    only = sys.argv[1:] or None
    if only:
        entries = [e for e in entries if e.key in only]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Bibliography verification, generated by scripts/refs/verify_bib.py",
        "# status: resolved | ambiguous | not-found",
        "# 'not-found' is a shortlist for manual checking, not proof of error.",
        "",
    ]
    tally = {"resolved": 0, "ambiguous": 0, "not-found": 0}

    for index, entry in enumerate(entries, 1):
        candidates = [query_crossref(entry), query_googlebooks(entry)]
        if entry.kind == "book":
            candidates.append(query_openlibrary(entry))
        else:
            candidates.append(query_ads(entry))
        status, match, problems = classify(entry, candidates)
        tally[status] += 1

        lines.append(f"{entry.key}:")
        lines.append(f"  status: {status}")
        lines.append(f"  kind: {entry.kind}")
        lines.append(f"  title: {yaml_escape(entry.get('title'))}")
        lines.append(f"  bib_year: {yaml_escape(entry.get('year'))}")
        lines.append(f"  bib_author: {yaml_escape(', '.join(entry.authors))}")
        if entry.get("publisher"):
            lines.append(f"  bib_publisher: {yaml_escape(entry.get('publisher'))}")
        if entry.get("journal"):
            lines.append(f"  bib_journal: {yaml_escape(entry.get('journal'))}")
        cites = citations.get(entry.key, [])
        lines.append(f"  cited_in: {len(cites)}")
        if match:
            lines.append("  match:")
            for name, value in match.items():
                if isinstance(value, list):
                    value = ", ".join(value)
                lines.append(f"    {name}: {yaml_escape(value)}")
        if problems:
            lines.append("  problems:")
            for problem in problems:
                lines.append(f"    - {yaml_escape(problem)}")
        lines.append("")

        print(f"[{index}/{len(entries)}] {entry.key}: {status}", flush=True)
        time.sleep(0.35)  # be polite to the free endpoints

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print()
    print(f"resolved  {tally['resolved']}")
    print(f"ambiguous {tally['ambiguous']}")
    print(f"not-found {tally['not-found']}")
    print(f"written to {OUT_PATH.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
