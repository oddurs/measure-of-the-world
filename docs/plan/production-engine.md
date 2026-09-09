# Production Engine

A plan for taking *The Measure of the World* from a January 2026 draft to a
print-ready first edition, and for the tooling that makes each pass
repeatable. Written 2026-09-08.

## 1. Where the manuscript actually stands

The audit on 2026-09-08 found the following. It sets the priorities below.

| Area | State | Evidence |
|---|---|---|
| Text | 25 chapters, ~72k words; 9 appendices, ~15k words. Complete draft, never proofread. | word counts |
| Facts | **Fabrications present.** Appendix C listed five people who were never Astronomer Royal, one of whom does not exist. Appendix H repeated them. Appendix C also had 175 lines of spectroscopy text glued onto its end. | fixed 2026-09-08 |
| References | 167 BibTeX entries, 142 in-text citations, 119 footnotes. None verified. The editorial guide even says "do not independently verify citations." Given the Appendix C finding, that rule is unsafe. | `docs/quality.md` |
| Figures | 116 matplotlib figures, all AI-drafted in one January session. Roughly 40 are data plots; roughly 75 are schematics, flowcharts, and timelines drawn with matplotlib primitives. Around 25 have overlapping labels; 2 were structurally broken. All use color. | contact-sheet review |
| Photos | 6, all in chapters 1 to 3. No source or license recorded. One is a private 2010 snapshot of unknown ownership; one carries Royal Society metadata. | EXIF |
| Index | 68 entries across 11 chapters; 14 chapters have none. | grep |
| Layout | Now 6 x 9 with Mixam bleed and trim box; 11pt Latin Modern; about 460 pages. | build |
| Pipeline | Local TeX Live and Python venv work; CI fixed; Makefile now fails on LaTeX errors. | `make build` |

The single most important conclusion: **every factual claim, quotation, and
reference in this book has to be treated as unverified until a person or a
tool has checked it against a source.** The engine below is organized
around making that tractable.

## 2. Principles

1. **Everything is a file in git.** Claims, verification status, figure
   specs, image licenses, review findings. No state lives only in a chat
   or a spreadsheet. A PR per chapter per stage keeps every change reviewable.
2. **Tools find, people decide.** Scripts and AI agents extract claims,
   look up sources, lint style, render proofs, and flag problems. The author
   signs off on every factual correction and every figure.
3. **Gates, not vibes.** A chapter is "done" when it passes a fixed list of
   checks (Section 8), and `make status` shows where every chapter is.
4. **Sources over memory.** An agent may not "fix" a fact from its own
   knowledge. It records the claim, the source it found, and the proposed
   change; the source must be a citable document (ADS record, book page,
   archive scan), and it goes into the bibliography.

## 3. Repository layout for the engine

```
review/
  claims/chNN.yaml          # every checkable claim in the chapter, with status
  refs/verification.yaml    # per-BibTeX-key: resolved? DOI/ISBN/ADS bibcode, notes
  critique/chNN.md          # editorial findings per pass (rubric in Section 6)
  layout/pages.md           # typesetting defects by page
figures/
  spec/chNN-<name>.md       # one spec per figure: purpose, data source, form, status
  manifest.yaml             # every image: file, source URL, creator, license, credit line
scripts/
  refs/     verify_bib.py, enrich_bib.py (DOI/ADS lookup), lint_bib.py
  claims/   extract_claims.py, report.py
  verify/   chNN_math.py (numeric re-derivations), run_all.py
  figures/  chNN.py (data plots), qa.py (overlap, size, dpi, grayscale checks), sheets.py
  proof/    render_pages.py, log_report.py (overfull boxes by file), pdfx_check.sh
  status.py                 # builds docs/status.md from the files above
```

Make targets: `make verify` (refs + claims + math), `make lint` (style),
`make figure-qa`, `make proof`, `make status`. CI runs all of them on every
PR and uploads the reports as artifacts.

## 4. Reference engine

**Goal:** every one of the 167 entries resolves to a real, locatable work,
and every citation supports the sentence it is attached to.

1. **Resolve every entry.** `verify_bib.py` queries Crossref (DOI),
   NASA ADS (all historical astronomy journals: *Philosophical Transactions*,
   *MNRAS*, *Astronomische Nachrichten*), Open Library and WorldCat (books),
   and Google Books. Output: `review/refs/verification.yaml` with one of
   `resolved`, `ambiguous`, `not-found` per key. `not-found` after a human
   look means the entry is removed and every citation of it is re-sourced.
2. **Enrich.** Add DOI, ADS bibcode, ISBN, and a stable URL to each entry so
   a reader can find it, and so the bibliography can print them.
3. **Lint.** Required fields per entry type, consistent name forms, no
   duplicate works under two keys, page numbers on every `\textcite` that
   supports a specific number or quotation.
4. **Citation-to-claim link.** In the claims ledger (Section 5) each
   verified claim names the BibTeX key and page that supports it. A citation
   that supports nothing is flagged for removal.
5. **Reading list for gaps.** Standard scholarly works the book should be
   drawing on where it currently cites nothing: Howse (*Greenwich Time and
   the Discovery of the Longitude*), Forbes/Meadows/Howse (*Greenwich
   Observatory*, 3 vols), Chapman (*Dividing the Circle*), Sobel/Andrewes
   (*The Quest for Longitude*), Baily (*An Account of the Revd. John
   Flamsteed*), Betts on chronometers, Bennett on instruments.

Tooling choice: keep `references.bib` in git as the source of truth. Zotero
is optional for the author's own reading; if used, export with Better
BibTeX to the same file rather than maintaining two libraries.

## 5. Fact-check engine

**Goal:** a ledger of every checkable statement, each marked verified,
corrected, or removed, with its source.

1. **Extract.** `extract_claims.py` splits each chapter into sentences and
   keeps those containing a date, a number with a unit, a proper name, a
   quotation, or a superlative ("first", "largest", "longest"). Expect
   roughly 150 to 250 per chapter. Output `review/claims/chNN.yaml`:
   ```yaml
   - id: ch04-017
     text: "The mural arc ... radius of approximately 6.75 feet."
     type: measurement
     status: unverified      # unverified | verified | corrected | removed
     source: ""              # bibkey + page, or URL
     note: ""
   ```
2. **Check, in priority order.**
   - Appendix G (primary-source excerpts). Quotations must match the
     original text verbatim. Highest fabrication risk. Every excerpt needs a
     scan or transcription link.
   - Appendix C, H, B (people, dates, tenures, instrument specifications).
   - Numbers inside derivations and worked examples (see math below).
   - Narrative chapters, in order.
3. **Math.** Each derivation and worked example gets a small script under
   `scripts/verify/` that recomputes the result with `numpy`/`sympy`
   (aberration constant, refraction table, lunar-distance clearing example,
   equation of time, pendulum temperature error, chronometer trial rates).
   `make verify` runs them; a mismatch between script and text is a defect.
4. **Who checks.** AI agents with web access do the first pass and fill the
   ledger with sources. The author reviews every `corrected` and `removed`
   item. Anything the agent cannot source stays `unverified` and is
   rewritten or cut before print. Wikipedia is a lead, never a source.
5. **Report.** `make status` shows per chapter: claims total, verified,
   corrected, unverified. A chapter cannot leave the fact-check stage with
   any `unverified` claim.

## 6. Editorial and critique engine

1. **Mechanical lint** (Vale with a LaTeX filter, custom rules from
   `docs/styleguide.md`): contractions, abbreviations the guide forbids
   ("RA" for right ascension), sentences over 35 words, passive voice
   density, "see Chapter X" without local context, undefined jargon on
   first use (checked against the glossary), hedge words, and repeated
   sentence openers.
2. **Structural critique per chapter**, one agent pass with a fixed rubric,
   output to `review/critique/chNN.md`: (a) does the opening scene earn its
   place, (b) does every section advance the argument, (c) where does the
   math arrive without motivation, (d) where does the text assert precision
   it does not demonstrate, (e) what does a reader need that is missing,
   (f) what should be cut. Findings are numbered so the author can accept or
   reject each.
3. **Consistency pass across chapters**: terminology (one term per concept),
   spelling of names, units, date formats, how instruments are named,
   cross-references. One script builds a term index; one agent pass reads it.
4. **Author revision**, then **professional copyedit** of the final text.
   Budget for a human copyeditor; no tool replaces one for a 460-page book.
5. **Proofread on paper.** The Mixam proof copy is the last read.

## 7. Visual engine

### 7.1 Decisions to make first

- **Color or grayscale interior.** Grayscale print is a fraction of the cost
  of color at 460 pages, and most of these figures are line diagrams.
  Recommendation: design for grayscale with one accent color; produce a
  color PDF for the free download and a grayscale-safe interior for print.
  Every figure is checked in grayscale simulation either way.
- **Who draws.** Data plots stay in code. Schematics and diagrams should be
  redrawn as vector art with consistent typography: TikZ (code, reviewable,
  same font as the book) or a designer working in Illustrator/Affinity to
  a spec. TikZ is the recommendation for a one-author project.

### 7.2 Design system

One page, in `figures/STYLE.md`: the palette (ink black, two grays, one
accent), line weights, label sizes at printed width (minimum 7pt), arrow
style, how axes are labeled, how timelines are drawn, caption conventions.
`common.py` and a `tikz/style.tex` implement it so every figure is on-system
by default.

### 7.3 Re-doing the 116 figures

1. **Spec every figure** (`figures/spec/`): what question it answers, the
   data or geometry it shows, its source, its form (plot, schematic,
   timeline, flowchart, map), and which sentence in the text it supports.
   Figures that answer no question are cut. Expect the count to fall.
2. **Classify.** Roughly: 40 data plots (keep matplotlib, restyle), 45
   schematics (TikZ), 20 timelines and flowcharts (TikZ templates), a few
   maps (Scilly wreck site, Greenwich park, Herstmonceux, La Palma; drawn
   from Natural Earth data or redrawn from public-domain charts).
3. **Automated QA** (`scripts/figures/qa.py`, run by `make figure-qa`):
   text bounding-box overlap detection, minimum font size after scaling to
   the `\includegraphics` width actually used in the chapter, bounding box
   sanity, 300 dpi at printed size, grayscale contrast check, contact sheets
   for eyeballing.
4. **Review.** Each figure is viewed at print size (render the PDF page) by
   an agent against its spec, then by the author.

### 7.4 Photographs and historical images

1. **Wish list per chapter** (in `figures/manifest.yaml`, status `wanted`):
   portraits of every Astronomer Royal through Woolley, Flamsteed House and
   the Octagon Room, the mural arc, Bradley's zenith sector, Harrison's
   H1 to H5, the Airy transit circle, the Great Equatorial, the time ball,
   the 1884 conference, the Herstmonceux domes, Shovell's fleet, sextants
   and octants, Nautical Almanac pages, Flamsteed's *Historia Coelestis*
   title page, a Tompion clock. Roughly 40 to 60 images for a book this size.
2. **Sources that permit commercial reuse under CC BY:** Wikimedia Commons
   public-domain scans, Wellcome Collection (CC BY or PD), Library of
   Congress, Internet Archive and Google Books scans of pre-1900 books,
   NASA/ESA. **Sources that do not, without a license:** Royal Museums
   Greenwich (mostly CC BY-NC-ND), Science Museum Group (CC BY-NC-SA),
   Royal Society picture library. Those need a paid license or the image
   is replaced. Budget line: image licensing.
3. **Manifest is mandatory.** No image enters `src/figures/photos/` without
   a manifest entry: file, source URL, creator, date, license, credit line,
   pixel size. `scripts/figures/qa.py` fails on any image without one, and
   `frontmatter/credits.tex` is generated from the manifest.
4. **The six existing photos** are audited first; the Tompion clock snapshot
   and the Royal Society Flamsteed portrait are the two most likely to need
   replacing.

## 8. Typesetting and proof engine

1. `make proof` renders every page to PNG, writes `review/layout/pages.md`
   from the build log (overfull boxes by file and line, floats far from
   their reference, widows and orphans, blank pages, figures scaled below
   0.5 or above 1.0 of their natural size), and runs the print checks:
   fonts embedded (`pdffonts`), page boxes (`pdfinfo`), image resolution
   (`pdfimages -list`), and a PDF/X-1a conversion with Ghostscript for the
   Mixam upload.
2. An agent reviews spreads (facing pages) for layout defects and writes
   findings to the same file. The author reviews chapter openings, part
   pages, and every figure page.
3. Wide tables (chapters 19, 21, 22, 23; Appendix I) are reflowed for the
   4.5 in measure by hand; no automatic fix exists.
4. **Index:** `scripts/index/propose.py` lists names, instruments, and
   concepts per chapter; the author approves; entries are inserted. Target
   roughly 600 to 900 entries with see-also cross references.

## 9. Gates: what "done" means per chapter

A chapter moves to the next stage only when the prior gate is green in
`make status`.

| Stage | Gate |
|---|---|
| 1 Fact-checked | 0 `unverified` claims; every quotation sourced; math scripts pass |
| 2 Referenced | every citation resolved and linked to a claim; no `not-found` keys |
| 3 Figured | every figure has a spec, passes `figure-qa`, reviewed at print size; every image in the manifest |
| 4 Edited | critique findings resolved (accepted or rejected with reason); lint clean |
| 5 Typeset | no overfull box over 5pt; no layout finding open; index entries present |
| 6 Proofed | read on the physical proof; corrections merged |

## 10. Phases and estimate

| Phase | Work | Duration |
|---|---|---|
| 0 | Pipeline, layout, decisions (color, image budget, copyeditor). Mostly done 2026-09-08. | this week |
| 1 | Reference resolution; claims ledgers; appendices B, C, G, H first; math scripts | 3 weeks |
| 2 | Design system; figure specs; redraw; photo acquisition and manifest | 4 weeks, overlaps phase 1 |
| 3 | Critique passes; author revision; consistency pass; copyedit | 4 weeks |
| 4 | Index; front and back matter; credits; cover; PDF/X; Mixam proof; tag v2.0.0 | 2 weeks |

Roughly three months of steady work. Phases 1 and 2 are parallelizable
across agents by chapter; phase 3 depends on both.

## 11. Decisions needed from the author

1. Color or grayscale interior (drives the whole figure design system).
2. Image licensing budget, or accept only free-to-reuse images.
3. TikZ redraws by agents, or a human illustrator to a spec.
4. Hire a copyeditor for phase 3.
5. Whether Appendix D (visitor guide) and Appendix G (primary sources)
   survive; both are expensive to verify and Appendix D dates quickly.

## 12. Progress as of 9 September 2026

The engine described above is built and running. `make claims`, `refs`, `lint`,
`derivations`, `figure-qa`, `proof` and `status` all work, and every result is
tracked under `review/`.

What the first pass found, beyond the Appendix C fabrications that started it:

- **All six primary-source quotations in Appendix G were fabricated.** None
  appears in the work it was attributed to; one cited a paper by Airy that was
  never written. The appendix is rebuilt from scanned originals.
- **Appendix B: 32 of 34 instrument entries wrong**, corrected against sources.
- **Appendix H: 32 of 79 chronology entries wrong**, worst fixed.
- **The bibliography**: 21 of 167 entries resolve cleanly; 25 duplicate keys
  removed.
- **Figures**: 96 text collisions and 18 label overflows fixed, undersized type
  cut from 144 failures to a handful.
- **Images**: all six identified by hash, one replaced, two credited, four
  captions corrected, 53 more specified with verified licences.
- **Typesetting**: overfull lines cut from 122 to 43; every printer check passes.

Two things surfaced that are not defects but gaps. The 1919 eclipse, organised
from Greenwich and the Observatory's most famous single result, appears in no
chapter. And there is a sixteenth Astronomer Royal: Michele Dougherty, appointed
July 2025.

## 13. Immediate next steps

1. Send the clean 6x9 PDF; read it end to end for a first impression.
2. Fix the 25 figures with visible label collisions found in review.
3. Build `verify_bib.py` and run it: the not-found list decides how deep
   the reference problem goes.
4. Build `extract_claims.py`; run it on Appendices C, G, H and Chapter 1.
5. Audit the six photos and write the first `figures/manifest.yaml`.
6. Get a Mixam quote for 460 pages, 6 x 9, color vs black-and-white, to
   settle decision 1.
