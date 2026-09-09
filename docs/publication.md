# Print Edition Checklist

Target: **v2.0.0**, a perfect-bound US Trade paperback (6 × 9 in) printed by
[Mixam](https://mixam.com). Earlier tags (v1.0.0–v1.3, January 2026) were PDF-only
drafts on US Letter and remain on GitHub as-is.

Status key: `[x]` done · `[ ]` open · `[~]` in progress / partially done

## Printer specification (Mixam)

Source: [mixam.com/support/bleed](https://mixam.com/support/bleed),
[mixam.com/support/filesetup](https://mixam.com/support/filesetup)

| Item | Requirement | Where it is set |
|---|---|---|
| Trim size | 6 × 9 in (US Trade) | `src/preamble.tex` Section 1 |
| Bleed | 0.125 in on every edge → PDF page 6.25 × 9.25 in | `\setstocksize` / `\settrims` |
| Quiet area | Nothing closer than 0.25 in to the trim edge | margins ≥ 0.625 in, folio 0.5 in from edge |
| Trim box | PDF TrimBox = finished 6 × 9 page | `\pdfpageattr` |
| Color | CMYK-ready; Mixam converts RGB. Profile GRACoL2006_Coated1v2 | pdflatex emits gray text, RGB figures |
| Resolution | 300 dpi images | figures saved at 300 dpi; photos checked below |
| Cover | Separate spread: front + spine + back, 0.125 in bleed; spine width from Mixam's cart after page count is known | not started |

## Build pipeline

- [x] Python venv + `requirements.txt` documented (`docs/build.md`, README)
- [x] CI installs Python venv before `make build`; builds on push/PR, releases only on `v*` tags
- [ ] Clean local build with zero undefined references and citations
- [ ] All 116 generated figures render; none referenced but missing
- [ ] Figure text legible at print scale (figures are drawn 6–8 in wide, printed at ≤ 4.5 in)
- [ ] Decide: color interior or grayscale. Figures currently use red/green/blue/orange/purple.
      Grayscale printing is far cheaper but the figure scripts would need a monochrome palette.

## Layout (6 × 9)

- [x] memoir stock/trim/margins set; geometry package removed
- [x] Body 11pt, headings, captions, footnotes, tables rescaled
- [ ] Review every `tabularx` / wide table at 4.5 in text width (chapters 19, 21, 22, 23; Appendix I sideways tables)
- [ ] Review long equations for overfull boxes
- [ ] Check widows/orphans and chapter openings (recto)
- [ ] Final page count → spine width → cover template from Mixam

## Front matter

- [ ] **ISBN** — set `\isbnprint` and `\isbnebook` in `src/metadata.tex` (currently "not yet assigned")
- [ ] **Edition date** — set `\editiondate` in `src/metadata.tex` (currently "2026"); also the foreword sign-off in `src/frontmatter/foreword.tex`
- [x] Copyright page reads ISBN/date/font from metadata; font statement corrected (Latin Modern)
- [ ] Acknowledgements: confirm the institutions and people thanked are accurate
- [ ] Add "About the Author" page (optional)
- [ ] Photo credits: add source and rights line for each of the six photographs
  - `ch01-admiral-shovell.jpg` — Dahl portrait, source unknown
  - `ch02-john-flamsteed.jpg` — file metadata points to royalsociety.org; check their reuse terms
  - `ch02-flamsteed-house.jpg` — source unknown
  - `ch02-tompion-clock.jpg` — a 2010 Canon PowerShot photo by an unnamed photographer; needs a license
  - `ch03-tycho-quadrant.jpg`, `ch03-uraniborg.jpg` — 1598 engravings, public domain; cite the scan source

## Content

- [ ] Index: only 68 entries across 11 chapters. Chapters 4–7, 10, 12, 13, 15–17, 20, 23–25 have none.
- [ ] Proofreading pass on all 25 chapters and 9 appendices
- [ ] Fact-check pass (dates, specifications, biographical details)
- [ ] README and back-cover copy match the actual chapter list (README fixed 2026-09-08)

## Release

- [ ] Tag `v2.0.0`; CI attaches the PDF to the GitHub release
- [ ] Upload interior PDF + cover PDF to Mixam; order a single proof copy before the run
- [ ] Update `docs/site/index.html` download link if the filename changes
