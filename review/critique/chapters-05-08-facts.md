# Chapters 5–8: fact-check

Scope: `src/chapters/05.tex`, `06.tex`, `07.tex`, `08.tex`.
Ledgers: `review/claims/ch05.yaml`, `ch06.yaml`, `ch07.yaml`, `ch08.yaml`.

93 claims were extracted by `scripts/claims/extract_claims.py`. I added 33 more by
hand for claims the extractor missed that carry the worst errors (worked-example
arithmetic, timeline entries, the Whiston–Ditton scheme, the gridiron algebra).
Added ids continue each chapter's sequence and follow the same format; note that
re-running the extractor will drop them, so they need folding into the extractor
patterns or into the chapter fixes before that happens.

| | claims | wrong | verified | could not source |
|---|---|---|---|---|
| ch05 | 30 | 16 | 8 | 6 |
| ch06 | 18 | 12 | 4 | 2 |
| ch07 | 32 | 14 | 11 | 7 |
| ch08 | 46 | 28 | 14 | 4 |
| **total** | **126** | **70** | **37** | **19** |

Numerical work was done with `scripts/verify/derivations.py` plus a
scratch ephemeris implementing a truncated Meeus ELP-2000/82 lunar theory,
validated against Meeus *Astronomical Algorithms* example 47.a (agrees to
1e-5 degrees) and against the published time of the 2024-01-25 full moon
(agrees to 2 minutes).

---

## Must fix, in order of severity

**1. The chapter 8 worked example is set on a date when the observation it
describes was impossible.** The chapter opens on the evening of 1770 July 21
with the Moon "two days past full" hanging bright beside Regulus at a distance
of 87°22′. At 18:30 UT that day the Moon was 13.0° from the Sun — a waning
crescent about 21 hours before new moon. The nearest full moon was 1770 July 7.
The Moon–Regulus distance was 40.5° and closing, not 87°22′ and opening. At the
position the chapter itself derives (45°N, 1°07′E) the Sun was still 9.5° above
the horizon at 18:34 local, the Moon was on the horizon at −0.4°, and Regulus,
1.9 hours of right ascension from the Sun, was invisible in daylight. Every
number in the observation table and in the "extract from Mayer's tables" is
invented. The example needs rebuilding on a real date and a real star.

**2. Chapter 8's refraction formula is corrupted.** It prints
`R(h) ≈ 58.3″ tan((90° − h)/7.5)`. The correct form, used correctly twice
elsewhere in this book (`src/chapters/04.tex:53`, `src/appendices/appendix-a.tex:96`)
and checked by `derivations.py`, is `R = 58.3″ cot h`. At 35° altitude the
printed formula gives 7.5″ against a true 83″, eleven times too small.

**3. Chapter 7 misstates what £20,000 was worth by a factor of about 30.** The
chapter calls it "roughly twenty years' wages for a skilled tradesman". A
building craftsman's day wage in 1710–19 was 22.1 pence, about £23–28 a year, so
£20,000 is 700–850 years of such wages. Chapter 1 already says "several thousand
working people", so the book contradicts itself as well.

**4. Chapter 6 lists Harrison's H4 Jamaica result as a daily error.** The
performance table gives "Harrison H4 trial, 1761, ±5.1 s, Daily Error". The 5.1
seconds was the total error accumulated over the whole 81-day voyage, a daily
rate of about 0.06 s. The table overstates H4 by roughly eighty-fold, and
contradicts `src/chapters/09.tex`, which states the 81-day figure correctly.

**5. Chapter 5's Vega worked example does not compute.** The declination step
prints 51°28′40″ − 33°18′35″ = +38°10′05″; the subtraction is +18°10′05″. The
sidereal-time step prints 19h52m38s where the stated inputs give 19h51m31s. The
"final catalog position" of 18h36m41s follows from none of the preceding steps.
And the inputs are impossible: Vega at epoch 1690 had declination +38°31′, so
its meridian altitude at Greenwich was 77°03′, not the 56°42′ assumed.

**6. Chapter 6 states the thermal error as 1 s/day immediately after correctly
deriving 8 s/day.** `derivations.py` confirms 8.21 s/day for a 10 K swing on a
brass seconds pendulum. The sentence following the derivation says "roughly one
second per day".

**7. Chapter 6's gridiron algebra is wrong in magnitude and in direction.** Three
printed products are off by a factor of ten (`5 × 0.1 × 19e-6` is given as
9.5e-7, `5 × 0.11 × 19e-6` as 1.045e-6) and one by a factor of five
(`5 × 0.1 × 11e-6` given as 1.1e-6 instead of 5.5e-6). Worse, the compensation
condition requires L_brass/L_steel = 11/19 = 0.58, so the steel rods must be
*longer* than the brass. The chapter makes the brass longer and then claims the
numbers nearly balance. They differ by 90 per cent.

**8. Chapter 7's timeline has Harrison completing H1 five years early and
invents a £4,400 award.** H1 was built 1730–1735 and brought to London in 1735;
1730 is when Harrison first came to London with his proposal. `ch09` says 1735
correctly. No £4,400 Board "gift" of 1773 appears in the 1773 statute or in the
transcripts of the 23 Longitude Acts; the £8,750 was awarded by Act of
Parliament (13 Geo. 3 c. 77 s. XXIX), over the Board's head, not by the Board.

**9. Chapter 7 puts the chronometer requirement at 0.5 s/day and the lunar
requirement at 1 arcsecond.** Both are wrong. Two minutes of time over six weeks
is 2.86 s/day, conventionally three seconds a day — the figure `derivations.py`
itself uses. And two minutes of time at the Moon's rate is one *arcminute* of
lunar position, not one arcsecond; chapter 8 says arcminute.

**10. Chapter 5 gets Bradley's discoveries wrong.** It says Bradley discovered
"stellar aberration and precession by comparing his observations against
Flamsteed's". He discovered aberration (1728) and nutation (1748), from his own
zenith-sector observations of γ Draconis with Molyneux, and precession was known
from Hipparchus — as this same chapter says three pages earlier. `ch12` and
appendix H tell the story correctly.

**11. The "six-week voyage" in chapter 7's prize tiers is not in the statute.**
"Six weeks" appears nowhere in the 1714 Act, nor in the transcripts of any of the
23 Longitude Acts. The Act required a ship to "actually sail over the Ocean, from
Great-Britain to any Port in the West-Indies" chosen by the Commissioners. The
phrase appears three times in the chapter and should be marked as a gloss.

**12. Chapter 5 misdates and misdescribes the burning of the 1712 edition.**
Flamsteed obtained 300 of 400 copies by royal order in March 1715/16 and burned
them in late April 1716 — and he burned the *sheets* he objected to (Halley's
preface, the catalogue, the mural-arc observations, about 13,500 sheets) after
first extracting the sextant observations, which he kept and reused in the 1725
edition. The chapter has him burning whole copies page by page in 1712.

---

## Chapter 5 — Building the Historia Coelestis Britannica

| id | claim | correction | source |
|---|---|---|---|
| ch05-001 | Informed spring 1712 that Newton and Halley had seized his books | Catalogue sealed and delivered to Newton 1706; 175 further sheets March 1707/8; Flamsteed learned it was in the press from Arbuthnot's letter of 14 March 1710/11 | Baily 1835, [archive.org](https://archive.org/stream/anaccountrevdjo00bailgoog/anaccountrevdjo00bailgoog_djvu.txt) |
| ch05-002 | Historia 1725, "occupy him until his death" | 1725 and three volumes correct; completed posthumously by Margaret Flamsteed with Crosthwait and Sharp; 2,935 entries | [ROG 932](https://www.royalobservatorygreenwich.org/articles.php?article=932) |
| ch05-011 | Star at α=0,δ=0 shifts 3.3s and 15″ from 1680 to 1700 | Over 20 years: 61.5s of time (922″) in RA, 401″ in declination. The printed values are one-year figures | recomputed |
| ch05-012 | m = 46.1″, n = 20.0″ "per century" | Annual values. Per century they are 4610″ and 2004″, and the formula divides by 36525 days = one century | recomputed |
| ch05-014 | Obliquity ≈ 23°27′ | 23°28′46″ at 1690; 23°26′21″ at J2000. Printed value matches neither | recomputed |
| ch05-015 | Sidereal time at midnight 1690 June 12 = 17h58m42s | GMST is 17h22m50s (Gregorian) or 18h02m16s (Old Style). Chapter does not say which calendar | recomputed |
| ch05-016 | α = 13h51m20s | 13h50m13s from the chapter's own inputs; and the result is then discarded for an unexplained 18h36m41s | recomputed |
| ch05-018 | Vega J2000 = 18h36m55.8s, +38°47′05.3″ | 18h36m56.34s, +38°47′01.28″. Vega at 1690 was 18h26m28s, +38°31′18″, so 1690→2000 is 10.5 minutes of RA, not 15 seconds | [SIMBAD](https://simbad.u-strasbg.fr/simbad/sim-id?Ident=vega) |
| ch05-020 | ±10–20″ vs Tycho 1–3′, "a threefold improvement" | Tycho is 1–2′ (rms 2′). On the chapter's own numbers this is 3× to 18×; `ch02` calls it an order of magnitude. The ±10–20″ figure is unsourced | [Verbunt & van Gent 2010](https://arxiv.org/pdf/1003.3836) |
| ch05-022 | Burned 300 of 400 copies, page by page, 1712 | Obtained them March 1715/16, burned the objectionable sheets late April 1716, kept the sextant observations | Baily 1835; [Linda Hall](https://www.lindahall.org/about/news/new-acquisition-john-flamsteed-historia-coelestis/) |
| ch05-024 | The 1712 edition "faded from use within decades" | Three quarters of the print run was destroyed in 1716, nine years before the authorised edition | ROG 932 |
| ch05-025 | Bradley discovered aberration and precession from Flamsteed's data | Aberration 1728, nutation 1748, from his own γ Draconis observations | [Phil. Trans. 35 (1728)](https://doi.org/10.1098/rstl.1727.0064); [45 (1748)](https://doi.org/10.1098/rstl.1748.0002) |
| ch05-026 *(added)* | "Halley, as Secretary of the Royal Society" in 1712 | Halley became Secretary 13 November 1713. In 1712 he was Savilian Professor; Newton held the Royal Society office, as President | DNB, Halley |
| ch05-028 *(added)* | ~3,000 stars, "nearly three times" Tycho | 2,935 entries (22 duplicates, ≥61 non-existent). Tycho: 777 printed 1602, 1,004 in the Rudolphine Tables. Say which Tycho catalogue | Baily; Verbunt & van Gent |
| ch05-029 *(added)* | Greenwich latitude 51°28′40″ | 51°28′38″ for the Airy Transit Circle. Flamsteed's own value was 51°28′30″ by 1690 | [MPC obs code 000](https://www.minorplanetcenter.net/iau/lists/ObsCodes.html) |
| ch05-030 *(added)* | δ = 51°28′40″ − 33°18′35″ = +38°10′05″ | +18°10′05″. And the input altitude is impossible for Vega | arithmetic; SIMBAD |

Could not source: the "approximately 50,000 individual measurements" (ch05-027)
appears in none of Baily 1835, the RMG or ROG Flamsteed pages, the Linda Hall
account, or Crossref. Also unsourced: "dozens of times" per bright star
(ch05-019), and the claim that the clock readings were in mean solar time
(ch05-005), which matters because the reduction multiplies by 1.0027379.

**Citation:** `WilmothFlamsteeds2002` is wrong in title, year and role. The real
book is Frances Willmoth (**ed.**), *Flamsteed's Stars: New Perspectives on the
Life and Work of the First Astronomer Royal, 1646–1719*, Boydell Press in
association with the National Maritime Museum, **1997**
([OpenLibrary](https://openlibrary.org/books/OL679739M)). `review/refs/verification.yaml`
flags it `ambiguous`; it should be `corrected`. The key spelling ("Wilmoth")
also differs from the author's name ("Willmoth").

## Chapter 6 — The Clock Problem, Part One

| id | claim | correction | source |
|---|---|---|---|
| ch06-001 | Huygens set a timepiece running in his workshop on 25 Dec 1656 | He made the first *model*, i.e. the design, that day. He was not a clockmaker and had no workshop; Coster built the clocks. A working clock was being rated by 31 May 1657; privilege granted 16 June 1657 | [antique-horology](http://www.antique-horology.org/Invention/Coster-the-Clockmaker-of-Huygens.HTM) |
| ch06-005 | Huygens pendulum, 1656, ±15 s | Year should be 1657. Documented accuracy ranges from ~8 s/day (Science Museum) to ~20 s/day (Huygens's own 1657 rating note) | [Science Museum](https://web.archive.org/web/20071010034250/http://www.sciencemuseum.org.uk/onlinestuff/stories/huygens_clocks.aspx) |
| ch06-006 | Tompion regulator 1676, ±5 s, "constant-force escapement" | `ch02` and `ch03` say 10–15 s/day. No source names the escapement; RMG says only "innovative escapement design to reduce friction". Documented: 13-foot pendulum beating 2 seconds, year-going | [RMG](https://www.rmg.co.uk/collections/objects/rmgc-object-202113); Baily p.45 |
| ch06-007 | Tompion regulator 1710, ±3 s, "improved thermal compensation" | Delete. No compensated pendulum existed before Graham (1721) and Harrison (1726). Contradicts `ch02`'s footnote, "no temperature compensation of any sort" | [Marrison 1948](https://web.archive.org/web/20070513175811/http://www.ieee-uffc.org/freqcontrol/marrison/Marrison.html) |
| ch06-008 | Graham mercury, 1720 | 1721; published *Phil. Trans.* 34 (1726) 40–44. Gould gives 1725. Nothing supports 1720 | Marrison; [Graham 1726](https://doi.org/10.1098/rstl.1726.0006) |
| ch06-009 | H4, ±5.1 s **daily** | 5.1 s total over 81 days, ≈0.06 s/day | [Gould 1923 p.56](https://archive.org/details/the-marine-chronometer) |
| ch06-010 *(added)* | 10 °C swing gives "roughly one second per day" | 8 s/day, as the chapter's own calculation shows | `derivations.py` |
| ch06-011 *(added)* | 15° amplitude gives "about 0.1%" period correction | 0.43%. 0.1% corresponds to 7.5° amplitude, so amplitude may have been confused with total swing. `ch21` gives 0.19% for 10°, which is right and inconsistent with this | recomputed |
| ch06-012/013 *(added)* | Gridiron arithmetic | Three exponents wrong; and steel must be longer than brass, not shorter (L_b/L_s = 11/19) | arithmetic |
| ch06-014 *(added)* | 15 min/day → 15 s/day is "a hundredfold improvement" | Sixtyfold | arithmetic |
| ch06-015 *(added)* | Tompion used "a remontoire escapement" for Flamsteed | Could not source. Not in RMG's object record, RMG's account, Flamsteed's own description, or Gould's index of remontoires. `ch02` calls it a dead-beat, a different claim again | RMG; Baily |

Verified: the equatorial bulge (21.4 km), centrifugal acceleration at the equator
(0.0339 m/s²), g at equator and pole (9.780/9.832, 0.53%), the London-to-Jamaica
rate change (123 s/day ≈ 2 minutes), the seconds-pendulum length and the 8 s/day
brass thermal error (both already in `derivations.py`), and the attribution of the
gridiron to Harrison in 1726.

Could not source: the claim that a gridiron reduced thermal error to ~0.1 s/day
(ch06-018).

## Chapter 7 — The Longitude Act and Its Incentives

| id | claim | correction | source |
|---|---|---|---|
| ch07-002 | £20,000 ≈ twenty years' wages for a skilled tradesman | 700–850 years. Craftsman's day wage 1710–19 was 22.1d, ≈£23–28/yr | [Clark, Table 3](https://faculty.econ.ucdavis.edu/faculty/gclark/papers/Working%20Class.pdf); [Stephenson 2016](https://www.lse.ac.uk/asset-library/information/wp231.pdf) |
| ch07-006 | 30 nm requires the Moon's position to ~1 arcsecond | ~1 arcminute. `ch08` says arcminute | arithmetic |
| ch07-007 | 2 minutes over six weeks = "roughly 0.5 seconds per day" | 2.86 s/day, conventionally 3 s/day — the figure `derivations.py` already uses | arithmetic |
| ch07-009 | Moon moves ~0.5°/hour | 0.549°/hour, about 33′, roughly one lunar diameter. `ch10` uses 0.55 | NASA Moon Fact Sheet |
| ch07-012 | London 12°W, Jamaica 3°E | gufm1: London 10.3°W in 1714 (7.5°W in 1700, 11.8°W in 1720); Kingston 5.3°E in 1714 | [NOAA/NCEI gufm1](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml) |
| ch07-018 | Lunar distances gave 1–2° at sea | Half a degree to one degree (30–60 nm). Maskelyne's preface: "within a Degree"; the 1779 preface gives ~50′ of longitude | [Nautical Almanac prefaces](https://archive.org/details/nauticalalmanac00admigoog); [ROG 1290](https://www.royalobservatorygreenwich.org/articles.php?article=1290) |
| ch07-023 *(added)* | "In the summer" / timeline "1714 (June)" | Commons 3 July, Lords 7 July, royal assent 9 July 1714. Bill introduced 16 June | [ROG 1312](https://www.royalobservatorygreenwich.org/articles.php?article=1312) |
| ch07-024 *(added)* | Whiston and Ditton: "signal fires and rockets visible from heights of forty miles" | Hulls moored at known stations firing a shell timed to burst at 6,440 feet, visible "about 100 measured, or 85 Geographical Miles: i.e. one whole degree" | [the pamphlet](https://archive.org/details/bim_eighteenth-century_a-new-method-for-discove_whiston-william-ma_1714) |
| ch07-025 *(added)* | "at the end of a 6-week voyage" (×3) | Not in the statute. The Act requires a voyage from Great Britain to a West Indies port chosen by the Commissioners | [1714 Act text](https://archive.org/details/1714-longitude-act-1755-a-collection-of-all-such-statutes-and-pa) |
| ch07-026 *(added)* | 1730: Harrison completes H1; Board provides funding | H1 built 1730–1735, brought to London 1735. 1730 is when Harrison came to London with his proposal. First Board payment (£500) voted 30 June 1737 | [RMG](https://www.rmg.co.uk/stories/time/harrisons-clocks-longitude-problem) |
| ch07-028 *(added)* | 1772: H5 error of 4.5 seconds over ten weeks | Could not source. The documented result is "within one third of one second per day" over ten weeks of daily observation at Richmond, May–July 1772 — about 23 s in total | [AHS](https://antiquarian-horology.com/john-harrison-3-4-1693-24-3-1776/) |
| ch07-029 *(added)* | 1773: Board awards £4,400 as a "gift"; Parliament adds £8,750 | No £4,400 award found anywhere. £8,750 was awarded by Act of Parliament (13 Geo. 3 c. 77 s. XXIX), not by the Board. Lifetime total ≈£23,065 | [ROG 1311](https://www.royalobservatorygreenwich.org/articles.php?article=1311) |
| ch07-031 *(added)* | Gellibrand "attempted to map magnetic variation" | Gellibrand discovered *secular* variation (1634, published 1635). The isogonic charts were Halley's: Atlantic 1701, world 1702 | [MacTutor](https://mathshistory.st-andrews.ac.uk/Biographies/Gellibrand/); [RMG chart](https://www.rmg.co.uk/collections/objects/rmgc-object-540213) |

Verified: the three prize tiers (£10,000 for one degree or sixty geographical
miles, £15,000 for two thirds, £20,000 for one half), the statute citation (both
12 Ann. St. 2 c. 15 and 13 Ann. c. 14 circulate; the chapter uses the Statutes at
Large form), the Astronomer Royal as an ex officio commissioner, Maskelyne
becoming Astronomer Royal in February 1765, the 1736 Lisbon trial, the 1828
dissolution (Nautical Almanack Act 1828, 9 Geo. 4 c. 66, assent 15 July), and
the Sobel and Andrewes citations.

Could not source: the "30 minutes of mental arithmetic" (ch07-010, and three
more times in ch08). ROG documents Maskelyne taking *up to four hours* before
the Almanac; after 1767 he called what remained "an Operation equal to that of
an Azimuth". Also unsourced: the claim that parliamentary testimony established
60 nautical miles as the risk threshold (ch07-008).

## Chapter 8 — The Lunar Distance Method

| id | claim | correction | source |
|---|---|---|---|
| ch08-001, 024, 026–031 | The 1770 July 21 observation | See must-fix 1. Moon 13° from the Sun, one day before new; Moon–Regulus 40.5° and closing; Sun 9.5° above the horizon; latitude and longitude mutually contradictory | recomputed (Meeus ELP-2000/82) |
| ch08-003 | 360°/27.3 days ≈ 0.5°/hour | 0.549°/hour. The equation asserts a value its own left side does not give | arithmetic |
| ch08-004 | The Moon is "the only celestial body that advances noticeably" | The Sun advances ~1°/day and the planets move over days. Say the Moon is the fastest, ~13°/day | arithmetic |
| ch08-005 | Horizontal parallax ≈ 57.3′ ("about one degree") | Mean 57.04′, range 54.1′–60.4′. 57.3 looks like a slip for 57.2958, degrees per radian. The chapter then uses 57.0′ and 56.8′ elsewhere — three values for one quantity | NASA Moon Fact Sheet |
| ch08-011 | "Longitude accurate to within 30 nautical miles or better" | The Commissioners claimed "within a Degree" (60 nm); the 1779 preface gives ~50′ of longitude | Nautical Almanac prefaces |
| ch08-012 | Mayer's tables gave the Moon's position "every 12 hours ... for 1750 to 1800" | Wrong in kind. Mayer's were tables of mean motions and equations, not a time-indexed ephemeris; no 12-hour interval and no date range. The 12 hours comes from Maskelyne's 1763 proposal | [Mayer 1770](https://archive.org/details/bim_eighteenth-century_tabulae-motuum-solis-et-_mayer-tobias_1770); [British Mariner's Guide 1763](https://archive.org/details/bim_eighteenth-century_the-british-mariners-gu_maskelyne-nevil_1763) |
| ch08-015, 018 | "typically every 3 hours" | Right for the *Nautical Almanac*, wrong for Mayer's tables, and the chapter states 12 hours, 3 hours and 30 minutes for the same tables | [ROG 935](https://www.royalobservatorygreenwich.org/articles.php?article=935) |
| ch08-032–037 | The "extract from Mayer's tables" | The tabulated distances advance 0.25°/hour while the table's own rate column says 0.497. The true rate was 0.63°/hour and the distance was *decreasing* | recomputed |
| ch08-038 *(added)* | R(h) ≈ 58.3″ tan((90−h)/7.5) | R = 58.3″ cot h. At 35° the printed formula gives 7.5″ against 83″ | ch04, appendix A, `derivations.py` |
| ch08-039 *(added)* | Δρ = HP(sin h_moon − sin h_star cos α) | Inconsistent with the chapter's own p_alt = HP cos h six paragraphs earlier. The correction must go as cos h_moon. Also called valid "for small distances (a few degrees)" and then applied at 87° | clearing theory |
| ch08-041 *(added)* | Refraction 2.5′ at 35°, 3.1′ at 28° | 1.4′ and 1.8′ | R = 58.3″ cot h |
| ch08-042 *(added)* | Interpolation to 18:29:48 | Dimensionally wrong (degrees ÷ degrees-per-hour is already hours, then multiplied by 30 minutes). Correct interpolation on the chapter's own table gives −0.60 min = 18:29:24; the chapter states −0.3 min and then writes 18:29:48, which is −0.2 min | arithmetic |
| ch08-043 *(added)* | Figure caption: 4′ RSS error → ~30 nm | The chapter establishes 1′ → 30 nm, so 4′ → ~120 nm. Caption and text disagree | arithmetic |
| ch08-044 *(added)* | "A star-catalogue (Chapter 3)" | Chapter 5. The chapter also hardcodes "Chapter 9" and "Chapter 10" instead of using `\cref` | `src/main.tex` |
| ch08-002 | Bringing the Moon's limb to the star | Correct practice, but the clearing procedure never applies the semi-diameter correction it makes necessary, though `tab:mayer-data` lists the semi-diameter. Worth ~15′ | British Mariner's Guide |

Two facts the chapter could usefully add, both verified: the 1770 *Tabulae* was
edited by Nevil Maskelyne (preface signed Greenwich, 23 February 1770), and in
May 1765 the Board awarded Mayer's widow £3,000, with £300 to Euler for the
underlying theorems ([ROG 1290](https://www.royalobservatorygreenwich.org/articles.php?article=1290)).

---

## Contradictions across chapters

1. **H4's Jamaica error.** `ch06` table lists 5.1 s as a *daily* error; `ch09`
   correctly gives 5.1 s over 81 days and even computes 0.063 s/day from it.
2. **Tompion's clock accuracy.** `ch02:43` and `ch03:76` say ten to fifteen
   seconds a day; `ch06`'s table says ±5 s in 1676 and ±3 s in 1710.
3. **Thermal compensation at Greenwich.** `ch02`'s footnote says the Tompion
   clocks "had no temperature compensation of any sort"; `ch06`'s table credits a
   1710 Tompion regulator with "improved thermal compensation".
4. **Flamsteed vs Tycho.** `ch02:83` calls it "an order of magnitude
   improvement"; `ch05` calls the same comparison "a threefold improvement".
5. **The Moon's rate.** `ch10:10` and `ch10:99` use 0.55°/hour; `ch07:48` and
   `ch08:15` use 0.5°/hour, and `ch08`'s error budget depends on 30′/hour.
6. **Lunar-distance accuracy at sea.** `ch07` says 1–2 degrees; `ch08` says
   ±0.5 degrees. The sources support half a degree to one degree.
7. **Lunar precision required for the prize.** `ch07` says 1 arcsecond; `ch08`
   says 1 arcminute. Arcminute is right.
8. **Chronometer rate required for the prize.** `ch07` says 0.5 s/day;
   `derivations.py` checks 3 s/day over six weeks against the 30 nm threshold.
9. **When H1 was finished.** `ch07`'s timeline says 1730; `ch09:46` says 1735.
10. **The refraction formula.** `ch04:53` and `appendix-a:96` use 58.3″ cot h;
    `ch08:98` uses a corrupted variant.
11. **Steel's expansion coefficient.** `ch06` uses 11e-6; `ch21:69` uses 12e-6.
12. **The amplitude correction.** `ch06` gives 0.1% at 15° amplitude; `ch21:53`
    gives 0.19% at 10°, which is right and implies 0.43% at 15°.
13. **Flamsteed's tenure.** `ch05` says 1676–1719 (43 years); `appendix-h:137`
    says 1675–1719 (44 years).
14. **Catalogue accuracy.** `ch05` says ±10–20″; `ch22:208` says ±10–15″ for the
    mural arc.
15. **The value of £20,000.** `ch01:126` says "the annual salary of several
    thousand working people"; `ch07` says "roughly twenty years' wages for a
    skilled tradesman". These differ by a factor of about 30, and `ch01` is
    closer to right.
16. **Tabulation interval.** Within `ch08` alone: every 12 hours, every 3 hours,
    and every 30 minutes, all describing the same tables.
17. **H1's sea trials.** `ch09:46` says H1 was "tested at sea on voyages to
    Portugal and Jamaica". H1 went only to Lisbon; it never crossed the Atlantic.
    Outside my chapters, but it feeds `ch07`'s timeline.

## Citation keys

Only four keys are cited in these four chapters. `Sobel1995`, `Howse1980` and
`Andrewes1998` all resolve in `review/refs/verification.yaml`.
`WilmothFlamsteeds2002` is marked `ambiguous` and is genuinely wrong — see the
chapter 5 section above.

`Maskelyne1763` is not cited in chapters 5–8 (it is used in `ch10`), but since
`verification.yaml` marks it `not-found` five times: **the book is real and the
"not-found" is a false alarm.** Crossref does not index eighteenth-century
books. Full title from the title page: *The British Mariner's Guide. Containing,
Complete and Easy Instructions for the Discovery of the Longitude at Sea and
Land, within a Degree, by Observations of the Distance of the Moon from the Sun
and Stars, taken with Hadley's Quadrant*, London, "Printed for the Author; and
sold by J. Nourse in the Strand", 1763. Full scan:
<https://archive.org/details/bim_eighteenth-century_the-british-mariners-gu_maskelyne-nevil_1763>;
also [WorldCat 722432495](https://search.worldcat.org/oclc/722432495). The bib
entry's publisher "John Nourse" should be "printed for the author; sold by J.
Nourse". Note `verification.yaml` holds two conflicting entries for this key,
with different titles and publishers.

## Method note

The four ledgers now carry a source URL for every `verified` and `corrected`
entry, and an account of what was tried for every `unverified` one. Numerical
claims were recomputed rather than looked up; the ephemeris used for chapter 8
is a truncated Meeus ELP-2000/82 implementation validated against Meeus's own
worked example and against a published modern full-moon time. Nothing in these
chapters was accepted because it sounded plausible.

No `.tex` file was modified.
