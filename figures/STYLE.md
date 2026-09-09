# Figure style

The rules every figure in *The Measure of the World* follows. They exist so
that 116 figures drawn over months read as one set, and so that a figure
that passes review on screen also works on paper.

`scripts/figures/common.py` implements what can be implemented. The rest is
judgement, checked by `scripts/figures/qa.py` and by eye at printed size.

## The constraint everything else follows from

The text block is **4.5 inches wide**. Figures are placed at 0.5 to 0.85 of
that, so most are printed **2.2 to 3.8 inches wide**, and several are under
2.5. A figure drawn 7 inches wide and printed at 3 is reduced to 43 percent,
which takes a 10 point label down to 4.3 points. That is below the threshold
where small type stays legible in print.

**Every label must reach the page at 7 points or larger.** The quality
checker computes the effective size from the width each figure is actually
placed at in its chapter and fails anything under the floor.

Two ways to satisfy it, in order of preference:

1. **Draw at the printed size.** A figure destined for 3 inches should be
   drawn 3 inches wide with 8 point text, not 7 inches wide with 8 point
   text. This is the honest fix and it forces the right decisions about how
   much can fit.
2. **Scale the type up to compensate.** What `common.py` currently does, as
   a stopgap for 116 figures drawn before the trim size was chosen.

## Colour

Assume the printed interior is **greyscale** until the printer quote says
otherwise. A 456 page colour interior costs several times a black and white
one, and almost every figure here is a line diagram.

**No figure may depend on colour to be understood.** Distinguish series by
line style, weight, marker shape, fill pattern and direct labelling.
Colour is a second, redundant channel. A reader with the black and white
book and a reader with the colour download must get the same information.

The palette, applied consistently:

| Role | Value | Greyscale |
|---|---|---|
| Ink, primary marks and all text | `#14181f` | black |
| Secondary marks, gridlines, construction lines | `#8b93a1` | 45% grey |
| Faint fills, shaded regions | `#dfe3ea` | 12% grey |
| Accent, the one thing the figure is about | `#17456b` | 70% grey |
| Warning or error, used sparingly | `#9b3526` | 55% grey |

Five values. Not one figure needs more. The current set uses matplotlib's
default cycle plus named colours (`red`, `green`, `blue`, `orange`,
`purple`, `gold`), several of which are indistinguishable once converted.

Direct-label series on the plot instead of using a legend wherever there is
room. A legend forces the reader to look away and match by colour, which is
exactly what greyscale breaks.

## Type

The book is set in Latin Modern. Figures render their text through LaTeX via
SciencePlots, so they already match. Do not introduce another face.

| Element | Size at printed width |
|---|---|
| Axis labels | 9 pt |
| Tick labels | 8 pt |
| Annotations and callouts | 8 pt |
| Series labels on the plot | 8 pt |
| Minimum anything | 7 pt |

No titles inside figures. The caption carries the title, it is set in the
book's own type, and a title inside the image duplicates it at the wrong
size. Several current figures have both.

Units always appear in the axis label, in parentheses: `Positional error
(arc-seconds)`. Never in the tick labels.

## Lines and marks

- Data lines 1.2 pt. Construction and reference lines 0.6 pt, dashed.
- Axis spines 0.8 pt. Only left and bottom; drop top and right.
- Gridlines only where the reader must read a value off the plot, at 0.5 pt
  and 20 percent opacity.
- Markers 4 pt, filled, with a white edge where they overlap.
- Arrows with a single consistent head: 6 pt long, 3 pt wide, solid.

## Captions

The caption says **what to look at and why it matters**, not what the figure
is. `Refraction against altitude` is the title, and the reader can see it.
`Near the zenith refraction is negligible; near the horizon it exceeds five
arc-minutes, which is why Flamsteed preferred high altitudes` is a caption.

Captions end with a full stop. A figure asserting measured data cites its
source in the caption, exactly as a sentence in the text would.

## Forms

| Form | Use when | Tool |
|---|---|---|
| Plot | There are real numbers with a scale | matplotlib |
| Schematic | Showing how an instrument is arranged | TikZ |
| Timeline | Events are ordered and dates carry meaning | TikZ template |
| Flowchart | A procedure has steps with a fixed order | TikZ template |
| Map | Position on the Earth is the point | TikZ over open data |
| Photograph | The object itself is the evidence | manifest, see IMAGES.md |

Instrument schematics are currently drawn with matplotlib primitives:
rectangles, circles and lines positioned by hand in data coordinates. That
is what produces most of the label collisions, because nothing keeps text
out of the way of the drawing. TikZ places text in the book's own typeface
and its node system keeps labels attached to what they label.

**A bar chart of four hand-assigned ratings is not data.** Several figures
score methods one to five on invented axes such as "practicality" and
"skill required". Those are opinions drawn as measurements, which is the one
thing a book about the honest representation of error should not do. They
become tables, or prose, or they go.

## Checklist before a figure is approved

- [ ] Its specification in `figures/spec/` states the question it answers
- [ ] Every label reaches the page at 7 pt or larger
- [ ] No text overlaps other text or is clipped by the axes
- [ ] Legible and complete in greyscale
- [ ] No information carried by colour alone
- [ ] No title inside the image
- [ ] Units in axis labels
- [ ] Any asserted number has a source
- [ ] Reviewed at printed size on a rendered page, not on screen at 200 percent
