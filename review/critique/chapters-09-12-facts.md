# Fact verification: chapters 9 to 12

Scope: `src/chapters/09.tex`, `10.tex`, `11.tex`, `12.tex`, against the ledgers
`review/claims/ch09.yaml`, `ch10.yaml`, `ch11.yaml`, `ch12.yaml`.

145 ledger claims checked. 58 corrected, 22 could not be sourced, 65 verified.
Beyond the ledger, 21 further errors were found in sentences the extractor did
not capture; they are listed in the per-chapter tables and flagged `(no ledger
entry)`.

Every correction below carries a source in the ledger `source` field. Where I
could not find a source I said so rather than confirming.

---

## Must fix before print

Ordered by severity. Each of these is wrong in a way a reviewer or reader will
catch, and several are the kind of invention the appendix audit already found.

### 1. Chapter 11 gets the astronomical unit wrong by a factor of 23, twice

`11.tex:49` and `11.tex:149-151`. The chapter divides 206265 by the solar
parallax and calls the answer astronomical units. It is a number of Earth
radii. It then converts to kilometres and lands on 3.5e9 and 3.524e9 km, and
calls 3.496e9 km the modern value of the astronomical unit. The astronomical
unit is 1.496e8 km. The same sentence contradicts itself: its own parenthesis
gives 1.496e11 m, which is 1.496e8 km. The formula the chain rests on
(`11.tex:39`) is also wrong: the chapter writes the solar distance as
1 AU divided by sin of the solar parallax; the correct relation divides the
Earth's radius, not one astronomical unit.

This is the single worst error in the four chapters. It is arithmetic anyone can
check, it appears twice, and it is self-contradictory within one line.

### 2. Chapter 11 sends the 1761 transit expeditions to two places that do not exist

`11.tex:147`. The expeditions are said to have gone to "Nortonshire (England)"
and "Nandi Island (Polynesia)". There is no county called Nortonshire and never
has been. There was no 1761 transit station called Nandi Island. The real 1761
stations include St Helena (Maskelyne), the Cape of Good Hope (Mason and Dixon),
Tobolsk (Chappe d'Auteroche), Rodrigues (Pingre), Madras, and St John's
Newfoundland (Winthrop). Given that the appendix audit found a person who does
not exist, two invented places should be treated as the same defect and
triggered the same way.

### 3. Chapter 9 sends H1 to Jamaica and invents its error

`09.tex:46`. H1 is said to have been "tested at sea on voyages to Portugal and
Jamaica", accumulating "less than 54 seconds" over several months. H1 had one
sea trial: Lisbon and back in 1736, out on HMS Centurion and home on HMS Orford.
It never went to Jamaica. No error figure in seconds survives for the Lisbon
trial. The documented result is navigational, not horological: on the return
Harrison identified a headland as the Lizard rather than the Start, putting the
ship about 60 miles from its reckoned position, and he was right. The Board
voted him 500 pounds on 30 June 1737 on that evidence. The 54 seconds is
fabricated and the Jamaica voyage belongs to H4 in 1761 to 1762.

### 4. Chapter 9 gives H4 a detent escapement

`09.tex:122`. Appendix B was corrected today to say H1 to H3 grasshopper, H4 and
H5 modified verge with diamond pallets, and that the spring detent is Arnold's
and Earnshaw's from about 1780. Chapter 9 still says H4's escapement "evolved
into a variant called the detent escapement". The book now contradicts itself
across two files. Chapter 21 line 4 carries the same error from the other
direction ("the detent mechanism that Harrison perfected") and should be fixed
in the same pass.

### 5. Chapter 12's worked example does not compute, and its data are backwards

`12.tex:88-124`. Two independent failures in one section.

The phase fit is wrong in every step. With the chapter's own model and its own
phase of -1.06 radians, June 1 comes out at +20.5 arcsec (the chapter needs
+10.1), December 1 at -17.9 (the chapter claims -20.5), and March 1 at +0.17
(the chapter claims +17.3). So -1.06 does not even satisfy the equation it was
derived from. The two phases that do satisfy that equation are -0.013 and
-2.124, and neither reproduces the other three points, which means the four
printed observations fit no single sinusoid of amplitude 20.5. The sentence
"These predictions match the observations almost exactly" is false as printed.

The four observations are also inverted in phase. As printed they put the star
farthest north in March and farthest south in December. Bradley found it
farthest south in March and farthest north in September. The figure caption
directly beneath the fit (`12.tex:128`) already states the correct phasing, so
the body text now contradicts its own caption on the page.

### 6. Chapter 10 cites a book that does not exist, five times, including a quotation

`10.tex:22, 37, 139, 156`. `Croarken2007` is entered in the bibliography as
"Computers for the People: Computing and Society in the Twentieth Century"
(Oxford University Press, 2007), with a note claiming its chapters 1 to 5 cover
eighteenth-century human computers. No such book exists, no catalogue holds it,
and a twentieth-century title could not carry eighteenth-century chapters. All
five locators are invented, including the quotation at `10.tex:156` ("The
Nautical Almanac was not the work of Nevil Maskelyne, but of Maskelyne and his
network"). The footnote at `10.tex:22` also names a computer, "Rupert Cotes near
Bristol", who appears in no record of the network.

Croarken's real work on this subject:

- "Mary Edwards: Computing for a Living in 18th-Century England", IEEE Annals of
  the History of Computing 25(4), 2003, 9-15.
- "Tabulating the Heavens: Computing the Nautical Almanac in 18th-Century
  England", IEEE Annals 25(3), 2003, 48-61.
- "Providing longitude for all: the eighteenth century computers of the Nautical
  Almanac", Journal for Maritime Research 4(1), 2002.

Every claim now resting on `Croarken2007` must be re-sourced to those or dropped.

### 7. Chapter 9 quotes a book that was published two years earlier under another key

`09.tex:229`. The quotation attributed to Andrewes 1998, Introduction, p. xxiii
could not be found. The book is the 1996 Longitude Symposium volume from
Harvard's Collection of Historical Scientific Instruments, and the bibliography
carries the same work twice, as `Andrewes1996` and `Andrewes1998`. The phrase
"and remains so today" is not language a 1996 editor's introduction uses. Treat
as fabricated, on the pattern of the six fabricated quotations in the appendices.

### 8. Chapter 10 breaks the Astronomer Royal succession twice in one clause

`10.tex:18`. "In 1765, Maskelyne was appointed Astronomer Royal, succeeding John
Flamsteed's successor James Bradley." Bradley was not Flamsteed's successor, and
Maskelyne did not succeed Bradley. The order is Flamsteed (1675-1719), Halley
(1720-1742), Bradley (1742-1762), Nathaniel Bliss (1762-1764), Maskelyne
(1765-1811). Maskelyne succeeded Bliss. Given that the appendix audit found five
people wrongly listed as Astronomer Royal, this sentence needs to go.

### 9. Chapter 11 credits Halley's comet perturbation to the wrong people, a century late

`11.tex:79`. The footnote says "A century later, more rigorous analysis by
Delaunay and Adams would refine these calculations." The perturbation
calculation was done before the return, in 1757 to 1758, by Alexis Clairaut with
Jerome Lalande and Nicole-Reine Lepaute, who worked for six months and found a
delay of 518 days from Jupiter plus 100 days from Saturn, predicting perihelion
on 13 April 1759. The comet reached perihelion on 13 March 1759, a month early.
Delaunay worked on lunar theory and Adams on Neptune; neither has any place
here. This erases the most celebrated computational achievement in the story the
chapter is telling, and it erases Lepaute specifically, in a book whose chapter
10 argues for crediting exactly that kind of unnamed labour.

### 10. Chapter 12 swaps the two nutation amplitudes

`12.tex:140`, `12.tex:153-155`, `12.tex:160`, `12.tex:192` (table). The chapter says nutation is
"roughly 9.2 arcseconds in longitude and 7.5 arcseconds in obliquity". The
principal nutation is 17.2 arcseconds in longitude and 9.2 arcseconds in
obliquity. The 9.2 has been moved to the wrong axis and the 7.5 is not a
nutation amplitude at all. The derivation, the figure caption and the summary
table all repeat the swap. Getting the labels right also gets the history right:
Bradley's announced figure of about 9 arcseconds is the obliquity term.

### 11. Chapter 9 prints a first-person false start

`09.tex:140`. "Wait---this seems too large. Let me recalculate." The final
numbers in that section are correct; the discarded attempt treated 1.3
arcminutes as 1.3 degrees. Cut the failed conversion and the recalculation aside
and keep only the correct chain. This cannot go to press in any form.

### 12. Chapter 10 is out by a factor of 27 on the lunar timing sensitivity

`10.tex:80`. "An error of 1 minute in the assumed time would produce an error of
about 15 minutes of arc in the Moon's position." The Moon moves 0.549 degrees
per hour, which is 0.55 arcminutes per minute of time. One minute of time
displaces the Moon by about half an arcminute. The 15 arcminutes figure is
Earth's rotation, 15 arcmin of longitude per minute of time, attached to the
wrong body. The chapter uses the correct 0.55 degrees per hour four lines later
at `10.tex:88`, so this contradicts itself as well.

### 13. Chapter 12 attributes Molyneux's instrument to the wrong maker and the wrong length

`12.tex:23` and `12.tex:36`. Molyneux's sector at Kew, the one used in December
1725, was made by **George Graham** and its telescope was about **24 feet**
long. The chapter says John Hadley built it and gives its radius as about 12
feet. Hadley built the reflecting telescope and the octant, not this. The
12.5-foot sector is a different instrument, also by Graham, made in 1727 for
Bradley's own use at Wanstead; Bradley later sold it to the Government for 45
pounds. Appendix G has already drawn this distinction; the chapter contradicts
it. The same paragraph's "telescope of short focal length" also has to go: 24
feet is not short.

---

## Chapter 9: Harrison's Chronometers

41 ledger claims: 17 corrected, 9 unsourced, 15 verified. Plus 6 findings with
no ledger entry.

| Where | Claim as printed | Correct value | Source |
|---|---|---|---|
| `09.tex:4` | Harrison "seventy-eight years old" at Kew, 1772 | Seventy-nine. Born 3 April 1693 NS; the trial ran May to July 1772 | RMG, Longitude found; Oxford DNB |
| `09.tex:4, 190` (ch09-002, -032) | "By God, Harrison, I will see you righted!" | Could not source. No contemporary document; family tradition, repeated by Sobel without a primary citation. Attribute as traditional or cut | none found |
| `09.tex:8` (ch09-004) | 1714 Act: two minutes over a voyage to the West Indies "and back" | The Act specifies half a degree of longitude (equivalently two minutes of time) on a voyage to a port in the West Indies. Not a round trip | Longitude Act 1714, 13 Anne c. 14 |
| `09.tex:23` (no ledger entry) | H1 had "two identical balance wheels mounted on the same axis" | Two dumbbell (bar) balances on separate arbors, linked together by wires and arcs. Not coaxial, not wheels | RMG collection record for H1, ZAA0034 |
| `09.tex:38` (no ledger entry) | Grasshopper escapement imparts energy "without physical contact" | It contacts the wheel teeth. It is nearly frictionless because the wooden pallets need no lubrication, not because contact is avoided | RMG, Longitude found |
| `09.tex:40` (no ledger entry) | The impulse lasts "microseconds" | Not credible for a mechanism beating at a few hertz. No source | none found |
| `09.tex:42` (no ledger entry) | H1 balance at "approximately 15 oscillations per second" | No source gives this. H4, far smaller and faster, runs at 5 beats per second. 15 Hz for a pair of large dumbbell balances is not plausible | RMG, Longitude found |
| `09.tex:46` (ch09-007, -008) | H1 tested to Portugal and Jamaica; under 54 seconds error | One trial only, Lisbon and back 1736 (HMS Centurion out, HMS Orford home). No seconds figure survives. See must-fix 3 | RMG; Society for Nautical Research |
| `09.tex:38 fn`, `09.tex:114 fn` (ch09-006, -014) | Harrison memorials to the Board of 1735 and 1757 | Neither is documented. The Commissioners first met on Harrison's business 30 June 1737. Harrison's papers are in RGO 14 | RGO 14, Cambridge Digital Library |
| `09.tex:46 fn` (ch09-009) | The 1735 memorial "reproduced in full in Sobel 1995, pp. 75-82" | Sobel 1995 has no documentary appendix and reproduces no memorial | Sobel, Longitude (1995) |
| `09.tex:56` (ch09-011) | H2 abandoned because its rate varied with amplitude | Abandoned because the ship's **yaw** disturbed the period of the bar balances. That is why H3 uses circular balances. H2 also missed its trial because of the war with Spain | RMG, Longitude found; Oxford DNB |
| `09.tex:69, 71` (ch09-012) | H3 "1740--1757", eighteen years | 1740 to 1759, nineteen years. The figure caption at `09.tex:17` repeats the 18-year figure | RMG, Longitude found |
| `09.tex:95` (ch09-013) | 50 K swing gives 0.0006 fractional change, about 50 s/day | The chapter's own formula gives 2.375e-3, which is 205 s/day. The moment-of-inertia step above it also double-counts the expansion: I scales as (1+aDT)^2, not (1+2aDT)^2 | recomputed |
| `09.tex:118` (ch09-015) | H4 begun in 1755 | Unsourced. RMG dates the Jefferys watch it grew from to about 1751-52 and says the first sea watch took six years, pointing to about 1753 | RMG, Longitude found |
| `09.tex:120` (ch09-016) | H4 5 inches diameter, 1.75 inches thick | 5.2 inches (13 cm) in silver pair cases. No source for the thickness | RMG; NMM record ZAA0037 |
| `09.tex:122` (no ledger entry) | H4 escapement is a detent; balance "about 20 Hz" | Modified verge with diamond pallets. Runs at 5 beats per second, so the balance frequency is 2.5 Hz. See must-fix 4 | Appendix B as corrected; RMG |
| `09.tex:126` (ch09-017) | Remontoire is "a small weighted wheel" | A spring remontoire, rewound every 7.5 seconds | RMG, Longitude found |
| `09.tex:140` (ch09-020) | "Wait---this seems too large. Let me recalculate." | Cut. See must-fix 11 | recomputed |
| `09.tex:175` (ch09-027) | Barbados 1764: 39.2 seconds "over five months" | 39.2 seconds over a voyage of **47 days**. The Board agreed in February 1765 that H4 had met the 1714 Act, three times over | RMG; Board minutes Feb 1765, RGO 14 |
| `09.tex:188` (ch09-030) | H5 "handed to the Board for official testing" | The Board would not test it. George III tested it himself over ten weeks in May to July 1772, and the Board still refused to recognise the trial. Harrison then petitioned Parliament, which voted 8,750 pounds in June 1773. The sentence inverts the point of the episode | RMG; Longitude Act 1773 |
| `09.tex:194, 196`, `09.tex:104` (ch09-033) | Temperature compensation improved "250-fold" | Three inconsistent numbers for one quantity: the stated coefficients give 50, the stated daily errors give 250, the figure caption says 25. And 2.5e-4/K over 50 K is 1080 s/day, not the 50 s/day the same paragraph asserts | recomputed |
| `09.tex:194` (no ledger entry) | Series runs at "15--20 Hz" | Follows from the two frequency errors above. No source supports either end | RMG, Longitude found |
| `09.tex:204-210` (ch09-035, -036, -037) | Thermal lag of 30-60 min; wear rates 1e-7 to 1e-6; 7-second error budget | Could not source any of it. The arithmetic is self-consistent but every input is invented, so the agreement with 5.1 s is circular | none found |
| `09.tex:239` (no ledger entry) | "Although \textcite{Maskelyne1763} would spend decades championing..." | A citation key used as the subject of a sentence. Renders as "Although Maskelyne (1763) would spend decades", which reads as a typo. Rewrite as prose with the citation in a footnote | n/a |
| `09.tex:245` (ch09-041) | "a substantial financial settlement" | Give the figures: 4,315 pounds in increments from the Board, 10,000 in 1765, 8,750 from Parliament in 1773, about 23,065 in all. He never got the 20,000-pound prize, which was never awarded to anyone | RMG; Longitude Act 1773 |

Citation keys used in this chapter that `review/refs/verification.yaml` marks
`not-found`: `Betts1978`, `Maskelyne1763`. `Betts1978` is cited three times
(`09.tex:23, 44, 114`) for page-specific technical detail. Jonathan Betts's
actual books are *Harrison* (NMM, 1993 and 2007) and *Marine Chronometers at
Greenwich* (2017); no 1978 NMM title of this name exists, and Betts would have
been about 25 in 1978. Treat the three page references as unsupported.

---

## Chapter 10: Maskelyne's Nautical Almanac

26 ledger claims: 9 corrected, 5 unsourced, 12 verified. Plus 5 findings with no
ledger entry.

| Where | Claim as printed | Correct value | Source |
|---|---|---|---|
| `10.tex:4` (ch10-001) | Mary Edwards computing at Ludlow in 1767 | She was not computing in 1767. Her husband, the Rev. John Edwards, was the computer of record; Mary did much of the work under his name and, after he died in 1784, was employed in her own right until her death in 1815. The vignette is about seventeen years early | Croarken, IEEE Annals 25(4) (2003) |
| `10.tex:4`, `10.tex:22` (ch10-010) | Maskelyne compared all submissions, rejected outliers, reassigned to a third computer | Each month was computed independently by **two** computers, and a third man, the **comparer**, reconciled the two sets and prepared press copy. Richard Dunthorne, then Malachy Hitchins (comparer 1767 to his death in 1809). Maskelyne administered and paid | Croarken, JMR 4(1) (2002); IEEE Annals 25(3) (2003) |
| `10.tex:12` (ch10-007) | Lunar theory "had occupied Jean-Baptiste Joseph Fourier, Leonhard Euler..." | Fourier was born in 1768, a year after the first Almanac, and never worked on lunar theory. The names are Newton, Euler, Clairaut, d'Alembert and above all Tobias Mayer, whose tables Maskelyne used | standard history of lunar theory |
| `10.tex:18` (ch10-008) | Maskelyne succeeded "John Flamsteed's successor James Bradley" | Wrong twice. He succeeded Nathaniel Bliss. See must-fix 8 | RMG, Astronomers Royal |
| `10.tex:22` (no ledger entry) | Computer "Rupert Cotes near Bristol" | Appears in no record of the network. The documented computers include Israel Lyons, George Witchell, William Wales and John Mapson | Croarken 2002, 2003 |
| `10.tex:24` (no ledger entry) | Stipend "typically £20--30 per annum, a working-class income" | The Board's rate was about **£70 a year** per computer. That is not a working-class income and the sentence's whole economic point changes | Croarken 2002; Bureau des Longitudes history of the Nautical Almanac |
| `10.tex:37` (no ledger entry) | Mary Edwards "a woman of independent means... motivated partly by intellectual interest rather than financial need" | Flatly contradicted. Computing was her **sole source of income** and supported her and her daughters after 1784. This inverts the one point about her that Croarken's article is written to make | Croarken, IEEE Annals 25(4) (2003) |
| `10.tex:80` (ch10-013) | 1 minute of time gives 15 arcmin of lunar error | About half an arcminute. Out by a factor of 27. See must-fix 12 | recomputed |
| `10.tex:117` (ch10-019) | "John Napier's 1617 work" on logarithms | Logarithms are *Mirifici Logarithmorum Canonis Descriptio*, **1614**. The 1617 work is *Rabdologiae*, on numbering rods, and 1617 is the year Napier died | MacTutor, John Napier |
| `10.tex:143` (no ledger entry) | Chronometer cost £100--200 in the late 18th century | Could not source. Kendall's K1 cost 450 pounds in 1769; Arnold and Earnshaw production chronometers sold for far less by 1800. The range needs a source or should go | none found |
| `10.tex:156` (ch10-022) | Croarken quotation | Fabricated. See must-fix 6 | n/a |
| `10.tex:174` (no ledger entry) | "Maskelyne envisioned the Royal Observatory as the source of standard time" in the 19th century, as railways and telegraphs spread | Anachronistic. Maskelyne died in 1811; the Greenwich time ball was not erected until 1833 (see `16.tex:4`) and telegraphic time distribution is later still. This is a claim about his successors | RMG; `src/chapters/16.tex` |
| `10.tex:184` (no ledger entry) | Lunar distance "faded from use by the early 19th century" | Too early, and it contradicts the chapter's own argument for the Almanac's endurance. Lunar distance tables ran in the Nautical Almanac until 1907 | HM Nautical Almanac Office history |

Citation keys used in this chapter that `verification.yaml` marks `not-found`:
`Croarken2007` (fabricated; see must-fix 6), `Maskelyne1763` (the British
Mariner's Guide of 1763 is real, but the page ranges at `10.tex:104`, pp. 112-125 and elsewhere, are unverified).

---

## Chapter 11: Edmond Halley's Broader Canvas

34 ledger claims: 17 corrected, 4 unsourced, 13 verified. Plus 7 findings with
no ledger entry.

| Where | Claim as printed | Correct value | Source |
|---|---|---|---|
| `11.tex:4` (ch11-001) | "the nineteen-year-old Edmond Halley" | Twenty. Born 29 October 1656, sailed late October or early November 1676. Verbunt and van Gent state it directly: "Halley was 20 years and a bachelor student when he left" | Verbunt and van Gent, A&A 530 (2011) A93 |
| `11.tex:4`, `11.tex:12` (ch11-006) | "nine months" on St Helena | Just over a year, roughly February 1677 to February 1678 | Verbunt and van Gent 2011; Ridpath, Star Tales |
| `11.tex:12` (no ledger entry) | St Helena at 5.83 deg west | 5.70 deg west (15 deg 57 min S, 5 deg 42 min W) | standard gazetteer |
| `11.tex:10` (ch11-003) | Equipped with "a telescope and a precision pendulum clock" | A large sextant with telescopic sights, a smaller quadrant and several refracting telescopes, paid for by his father. No pendulum clock is recorded | Ridpath, Star Tales |
| `11.tex:12` (ch11-005) | Halley used "the meridian method, identical to Flamsteed's technique" | He measured **angular distances** from stars in Tycho Brahe's catalogue, keeping Brahe's ecliptic positions, because bad weather stopped him fixing the obliquity. A different technique with a different error structure | Verbunt and van Gent 2011 |
| `11.tex:14` (ch11-006) | Catalogue accurate "to within a minute of arc"; "the most brilliant southern stars were absent... victims of cloud cover" | Error distributions are about **3 arcminutes** wide (systematic sextant deviation to 2 arcmin at 60 deg, random 0.7 arcmin). And the brightness claim is backwards: bad weather made Halley skip the **faint** stars of Piscis Austrinus and all of Indus in order to keep the brighter ones. Canopus, Achernar, Alpha Centauri and Fomalhaut are all in the catalogue | Verbunt and van Gent 2011 |
| `11.tex:34`, `11.tex:143` (no ledger entry) | Transit parallax of Venus is 0.72 times the solar parallax | Wrong in both direction and value. Venus at inferior conjunction is 0.277 AU from Earth, so its parallax is 3.6 times the solar parallax, and the quantity the method actually uses, the relative parallax, is about 2.6 times. The chapter has used Venus's **heliocentric** distance and multiplied where it should divide | standard transit geometry |
| `11.tex:39` (no ledger entry) | Solar distance = 1 AU / sin(solar parallax) | = Earth radius / sin(solar parallax) | standard parallax relation |
| `11.tex:44, 49`, `11.tex:149-151` (ch11-032) | 206265/8.8 = 23,440 AU = 3.5e9 km; modern AU 3.496e9 km | Both are Earth radii mislabelled as AU, and the modern AU is 1.496e8 km. Out by 23.4x, twice, and self-contradictory within `11.tex:151`. See must-fix 1 | Sigismondi and Oliveira, arXiv:1301.0296 |
| `11.tex:59` (ch11-011) | `Halley1693` cited for the transit method | Fabricated entry. Halley read the method to the Society on 23 September 1691 and published it as *Methodus singularis*, Philosophical Transactions **29** (1716), 454-464. The bibliography's "Phil Trans 18, 1-14, 1693" matches no paper | royalsocietypublishing.org 10.1098/rstl.1714.0056 |
| `11.tex:63` (ch11-012) | The 1677 Mercury transit "confirmed the feasibility of the method" | The opposite. Only Towneley at Burnley made another usable observation; Gallet at Avignon recorded only that it happened; the resulting 45-arcsecond solar parallax was one Halley rejected. The episode taught him the method needed many coordinated observers | historical record of the 1677 transit |
| `11.tex:67` (no ledger entry) | Before Halley, comets "were understood to move in straight lines" | Oversimplified to the point of error. Kepler favoured straight lines, but Newton had already established parabolic orbits in the *Principia* (1687), which is what Halley worked from | Halley, *Synopsis* (1705) |
| `11.tex:77`, `11.tex:79` (ch11-017, -019) | Return predicted for 1757 | Halley predicted about the end of **1758**. Appears twice | Halley, *Synopsis* (1705) |
| `11.tex:79` (ch11-019) | Refinement by "Delaunay and Adams" a century later | Clairaut, Lalande and Lepaute, 1757-58, before the return. See must-fix 9 | MacTutor, Nicole-Reine Lepaute; Ridpath, The Comet returns |
| `11.tex:79` (ch11-018) | Jupiter's pull "comparable in magnitude to the solar force" | Never comparable; at closest approach it is a few parts in a thousand. Enough to shift the period by a year over 76 years, which is the real point | standard planetary masses |
| `11.tex:81` (ch11-022) | Halley "deceased for fourteen years" when the comet returned | Sixteen years and eleven months. He died 14 January 1742; Palitzsch sighted the comet 25 December 1758; perihelion 13 March 1759 | Ridpath, The Comet returns |
| `11.tex:99` (ch11-023) | "HMS Paramour" | Spelled *Paramore*, and she was a pink rather than a conventional naval vessel; Halley held a temporary commission to command her | Cook, *Edmond Halley* (1998) |
| `11.tex:109` (ch11-025) | Breslau records "compiled by the city clerk" | Compiled from the parish registers by **Caspar Neumann**, the Protestant pastor of Breslau, for 1687-1691, and forwarded via Leibniz, Justel and the Royal Society. Naming him matters in a book that argues for crediting unnamed labour | Bellhouse, JRSS A 174(3) (2011) |
| `11.tex:109` (ch11-026) | "the first life table" | The first based on population data. Graunt's 1662 table came first but was not derived from recorded ages at death. Also, the figure caption's "cohort of 1000 births" is not what Halley tabulated: his radix is 1000 survivors at age one, from about 1238 annual births | Bellhouse 2011 |
| `11.tex:133` (no ledger entry) | Method articulated "in the 1690s when the next convenient transit was still sixty years away" | About seventy years from the 1690s to 1761, and Halley's fullest statement is the 1716 paper, forty-five years before | Halley, *Methodus singularis* (1716) |
| `11.tex:141-149` (ch11-030) | Tobolsk worked example, 19.3-minute contact difference | Tobolsk at 68.2 deg E is 4h 33m ahead of Greenwich, not 3h, so 08:41:06 local is 04:08 GMT and the 19.3 minutes is an artefact of the wrong conversion. Real inter-station contact differences are minutes, not nineteen minutes. Rebuild from published 1761 timings or drop | recomputed |
| `11.tex:147` (ch11-032) | Nortonshire; Nandi Island | Neither exists. See must-fix 2 | Sigismondi and Oliveira 2013 |
| `11.tex:149` (ch11-032) | 1761 yielded a solar parallax of 8.76 arcsec | Not the 1761 result. The 1761 analyses scattered between roughly 8.3 and 10.6 arcseconds, which is why 1769 was mounted; 8.78 comes from Hornsby's 1771 reduction of the 1769 transit. The modern value is 8.794148 | Sigismondi and Oliveira 2013 |
| `11.tex:151` (ch11-033) | "more than 150 observers at 77 locations" for 1761 and 1769 | Could not source that figure for the two transits jointly. Numbers of that order are quoted for 1769 alone; 1761 is usually given as roughly 120 observers at about 60 stations. Split them or drop the numbers | none found |

Citation keys used in this chapter that `verification.yaml` marks `not-found`,
all four of which are broken beyond the catalogue miss:

- `Halley1693` (`11.tex:59`) - fabricated; see the table.
- `Hughes2000` (`11.tex:79`) - entered as "The Tudor Astronomical System: Tycho
  Brahe and the Heliocentric System", cited for Halley's cometary work. The
  title has nothing to do with Halley and the note claiming it "includes
  chapters on Halley's cometary work" is invented.
- `Chapin1995` (`11.tex:59`, `11.tex:151`) - entered as "Nutation and the Earth's
  Axis" (Willmann-Bell), cited twice for the history of transit-of-Venus
  expeditions. Title and subject do not match. Seymour Chapin was a real
  historian of eighteenth-century astronomy; this is not one of his books.
- `Sykes1926` (`11.tex:118`) - "The Life and Work of Edmond Halley" (OUP, 1926)
  by Frederick Henry Sykes. Frederick Henry Sykes, the Canadian educator, died
  in 1917. The book does not exist. Use Cook, *Edmond Halley* (Clarendon, 1998),
  which is real and already in the bibliography as `Cook1998`.

---

## Chapter 12: Bradley and the Aberration of Starlight

44 ledger claims: 15 corrected, 4 unsourced, 25 verified. Plus 6 findings with
no ledger entry.

| Where | Claim as printed | Correct value | Source |
|---|---|---|---|
| `12.tex:4`, `12.tex:17` (ch12-002, -005) | Bradley "had planned this observation"; "Bradley and Molyneux decided" | Molyneux had the parallax programme, commissioned the sector and invited Bradley to assist in December 1725. Hooke had attempted the same star in 1669, so "what earlier astronomers had not" also overstates it | MacTutor, James Bradley |
| `12.tex:4` vs `12.tex:88` (ch12-016) | "the next eighteen months" vs "December 1725 to December 1726" | Internally inconsistent. The Kew series is about twelve months; Bradley's wider survey began August 1727 at Wanstead with his own instrument | MacTutor, James Bradley |
| `12.tex:21` (ch12-036) | "the mural arc, which measured both altitude and azimuth" | A mural arc is fixed in the plane of the meridian and measures altitude only. It cannot measure azimuth | Chapman, *Dividing the Circle* (1990) |
| `12.tex:23`, `12.tex:36` (ch12-008) | Sector "built by John Hadley", "radius of about 12 feet", "short focal length" | Built by **George Graham**; telescope about **24 feet**. The 12.5-foot sector is Bradley's own Wanstead instrument of 1727. See must-fix 13 | ROG, Bradley's 12.5-foot Zenith Sector; MacTutor |
| `12.tex:34` (no ledger entry) | gamma Draconis "a third-magnitude star" | V = 2.23, so second magnitude | SIMBAD, HD 164058 |
| `12.tex:36`, `12.tex:170`, `12.tex:172` (ch12-007) | Expected parallax "roughly 0.3 arcsecond" | Could not source a contemporary expectation of 0.3. The true parallax is 0.0211 arcsec, so the star is about 47 pc away, not "within a few parsecs". Say plainly if this is the author's reconstruction | SIMBAD |
| `12.tex:40` (ch12-010) | Star "moved south in December... yet continued to move south even in June" | It kept moving south to a **March** minimum, then north to a **September** maximum: three months out of phase with parallax, not opposite to it. By June it was back near its December position | MacTutor, James Bradley |
| `12.tex:40` (ch12-010) | Position "changed by roughly 20 arcseconds over the course of a year" | About one hundredth of a degree over six months, so roughly 36 to 40 arcsec peak to peak. Amplitude 20, range 40 | MacTutor, James Bradley |
| `12.tex:75` (ch12-015) | Bradley "confirmed the value to roughly this precision" (20.49552) | Bradley's own result implies about **20.2 arcsec**: he derived a solar light-time of 8 min 12 s against the modern 8 min 20 s, roughly 1.5 per cent low. And the footnote cites `Feingold1984`, *The Newtonian Moment*, which is a 2004 book on Newton's cultural reception with nothing on aberration. Cite Bradley's own 1729 paper | MacTutor; derivations.py |
| `12.tex:88-96` (ch12-016) | Four observations: Mar +17.26, Jun +10.10, Sep -7.06, Dec -20.47 | Inverted in phase and inconsistent with the figure caption at `12.tex:128` and with Appendix I. See must-fix 5 | MacTutor, James Bradley |
| `12.tex:112-124` (ch12-017) | Phase fit; "predictions match the observations almost exactly" | Every value wrong; the stated phase does not satisfy its own defining equation; no single sinusoid fits the four points. See must-fix 5. `scripts/verify/derivations.py` independently flags the parallel fit in the appendices (phi -0.634 vs the book's -1.05, offset -1.02 vs -0.2, residuals 3.15 arcsec RMS vs the claimed 1-2) | recomputed; derivations.py |
| `12.tex:140`, `12.tex:153-155`, `12.tex:160`, `12.tex:192` (ch12-024, -043) | Nutation "9.2 arcseconds in longitude and 7.5 arcseconds in obliquity" | 17.2 in longitude, 9.2 in obliquity. See must-fix 10 | Britannica, Nutation; IERS Conventions 2010 |
| `12.tex:147-155` (ch12-022) | The nutation torque formula | Not a standard result and apparently garbled: it multiplies by the lunar eccentricity for no stated reason and omits the dynamical ellipticity that the real expression depends on. The footnote cites `Vallado2013`, "Revisiting Spacetrack Report 3", which is a 2006 AIAA paper on SGP4 orbit propagation, not a 2013 AAS book, and has no chapter on nutation | none found |
| `12.tex:155` (no ledger entry) | Bradley's nutation "remarkable given that most of his observations spanned only a few years" | The reverse. Bradley deliberately observed a full nodal cycle, returning to Wanstead for twenty years, concluded by 1747, and announced in a letter read to the Royal Society in February 1748. That persistence is the whole point of the achievement, and the footnote erases it | MacTutor, James Bradley |
| `12.tex:168` vs `12.tex:233` (ch12-025, -026) | Precision "roughly 2--3 arcseconds" vs the arc read "to a fraction of an arcsecond" | Internally contradictory, and both disagree with the corrected Appendix A, which speaks of one arcsecond of measurement error over eighteen nights. About one arcsecond per observation is the defensible figure | derivations.py; appendix-a.tex as corrected |
| `12.tex:217` (ch12-032) | Roemer gave c = 2.75e5 km/s | Roemer published a light-time, not a speed. Huygens turned it into roughly 2.1 to 2.2e5 km/s using his own solar distance. `derivations.py` already flags this as a FAIL | derivations.py |
| `12.tex:245` (no ledger entry) | Bradley fitted "both aberration and nutation" and removed proper motion over the 18-month campaign | Anachronistic. Nutation took twenty years to establish and was not part of the 1725-27 reduction. gamma Draconis's proper motion is about 0.025 arcsec/yr, negligible over 18 months | MacTutor, James Bradley |
| `12.tex:251` (ch12-040) | 61 Cygni "about 3.4 parsecs away" | Bessel's 0.3136 arcsec gives 3.19 pc (10.4 ly); the modern 0.286 arcsec gives 3.5 pc (11.4 ly). 3.4 matches neither. Flagged by `derivations.py` | derivations.py |
| whole chapter (ch12-035) | (omission) | The chapter never states when Bradley's letter was published. Appendix G established Philosophical Transactions vol. 35 for **1729**, read January 1729, not 1728. Say so: the 1728 date circulates widely and the book will be checked against it | Phil Trans 35, no. 406 (1729), 637-661 |

Citation keys used in this chapter that `verification.yaml` marks `not-found`:
`Feingold1984` (`12.tex:75`) - wrong year (the book is 2004), wrong subject.
`Vallado2013` (`12.tex:155`) is marked `ambiguous` but is equally broken: wrong
year, wrong format, wrong subject.

---

## Contradictions

### Within chapter 12

1. **Phasing of gamma Draconis.** The figure caption at `12.tex:128` says the
   star stands farthest south in March and farthest north in September. The
   observation list at `12.tex:88-96` says farthest north in March and farthest
   south in December, and the narrative at `12.tex:40` says it kept moving south
   through June. The caption is right; the other two are wrong. This is a
   contradiction visible on a single page.
2. **Sector precision.** `12.tex:168` says 2-3 arcseconds per observation;
   `12.tex:233` says the arc was read to a fraction of an arcsecond.
3. **Length of the campaign.** `12.tex:4` says eighteen months; `12.tex:88` says
   December 1725 to December 1726.

### Chapter 12 against the appendices

4. **Bradley's observation table.** Appendix I (`appendix-i.tex`) tabulates a
   northern maximum of +20.5 arcsec on 3 October 1725 and a southern maximum of
   -20.5 on 19 December 1725, with the series starting in September 1725.
   Chapter 12 gives September as -7.06 (south) and December as -20.47, and dates
   the start to December 1725. The three files (chapter body, chapter caption,
   Appendix I) now give three different phasings. Appendix I additionally dates
   the observations to before the campaign began and locates Bradley at
   Greenwich, where he did not work until 1742. Whoever fixes chapter 12 should
   fix Appendix I in the same pass so the reconstruction is single-sourced.
5. **Zenith sector.** Appendix G established that the December 1725
   observations used Molyneux's sector at Kew and that Bradley's own sector came
   later. Chapter 12 still credits the Kew instrument to Hadley and gives it the
   Wanstead instrument's 12-foot dimension.

### Chapter 9 against Appendix B and chapter 21

6. **H4's escapement.** Appendix B (`appendix-b.tex:85-88`, corrected today) has
   H4 and H5 as modified verge with diamond pallets and states that the spring
   detent is Arnold's and Earnshaw's from about 1780. `09.tex:122` calls H4's
   escapement a detent. `21.tex:4` says Earnshaw worked on "the detent mechanism
   that Harrison perfected decades ago", and `21.tex:143, 147` say Earnshaw's
   detent "retained the principles of Harrison's mechanism" and "simplified
   Harrison's grasshopper escapement". Chapter 21 is outside my scope but
   carries the same error and should be corrected together with chapter 9,
   otherwise Appendix B will contradict two chapters instead of one.

### Chapter 10 against chapters 9, 16 and 25

7. **When chronometers displaced lunars.** `10.tex:184` says the lunar distance
   method "faded from use by the early 19th century"; `10.tex:135` says
   chronometers were reliable enough "by the 1780s"; `09.tex:239` says
   chronometers became common in the 1790s and standard in the 19th century.
   Meanwhile the same chapter argues the Almanac endured precisely because
   lunars remained available. Lunar distance tables ran until 1907. The book
   needs one timeline.
8. **Maskelyne and time distribution.** `10.tex:174` credits Maskelyne with
   envisioning the Observatory as the source of standard time as railways and
   telegraphs spread. `25.tex:35` goes further and credits him with "the network
   of distributed time balls, the connection to the Telegraph network".
   Maskelyne died in 1811; `16.tex:4` dates the Greenwich time ball to 1833.
   Both passages attribute his successors' work to him.

### Bibliography

9. **Andrewes duplicated.** `Andrewes1996` and `Andrewes1998` are the same book
   entered twice with different publishers and years. The real one is the 1996
   Longitude Symposium volume. `09.tex:229` cites the 1998 form; `21.tex:4`
   cites the 1996 form.
10. **Chapman1990 and Chapman1996.** `verification.yaml` flags a year and author
    mismatch on `Chapman1996` (catalogue says 1991, Bennett). Both keys are used
    in these chapters (`11.tex:98`, `12.tex:249` lineage). Worth a check by
    whoever owns the bibliography, though the books themselves are real.

---

## What I could not source

Listed so nobody mistakes silence for confirmation. These stay `unverified` in
the ledgers with the search recorded in the `note` field.

- The George III quotation, "By God, Harrison, I will see you righted!"
  (`ch09-002`, `ch09-032`). No contemporary document found.
- Harrison memorials to the Board dated 1735 and 1757 (`ch09-006`, `ch09-014`).
- H4's error budget: thermal lag time constant, wear rates, the 7-second total
  (`ch09-035`, `-036`, `-037`).
- H1's balance frequency, and therefore the 15-20 Hz range at `09.tex:194`.
- The Almanac's labour estimate in person-hours (`ch10-009`) and the navigator's
  30-60 minute and 2-3 hour timings (`ch10-016`, `-018`).
- The late-18th-century chronometer price of £100-200 (`10.tex:143`).
- Observer and station counts for the 1761 and 1769 transits taken jointly
  (`ch11-033`).
- The contemporary parallax expectation of 0.3 arcsec for gamma Draconis
  (`ch12-007`, `-028`, `-030`).
- The nutation torque expression at `12.tex:147` (`ch12-022`).
