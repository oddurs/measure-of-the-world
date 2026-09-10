# Chapters 1–4: fact check

Checked 2026-09-09 against Royal Museums Greenwich, royalobservatorygreenwich.org, Boydell
and Brewer, the Library of Congress newspaper catalogue, the Western Australian Museum, and
direct computation. Wikipedia was used only to find sources, never as one.

| | ch01 | ch02 | ch03 | ch04 | total |
|---|---|---|---|---|---|
| claims checked | 25 | 28 | 26 | 30 | 109 |
| wrong (`corrected`) | 12 | 15 | 10 | 20 | 57 |
| supported (`verified`) | 5 | 8 | 9 | 4 | 26 |
| could not reach a source | 8 | 5 | 7 | 6 | 26 |

Sixteen of the 109 entries were added by hand because `extract_claims.py` did not pick the
sentence up. They carry ids from `-101` upward and are marked with a banner comment in each
ledger. **Re-running the extractor will delete them.**

No `.tex` file was edited and nothing was committed.

---

## Must fix, worst first

**1. The Aldebaran worked example in chapter 4 is fabricated end to end.**
Every number in it is wrong and the conclusion it draws is impossible. Aldebaran stood at
right ascension 4h 17m 37s, declination +15° 49′ 14″ in 1680, giving a meridian altitude
from Greenwich of about 54° 21′. The chapter's "raw measurements" put it 7° higher, and its
"result" of 19h 20m 24s is not a period position at all. The chapter then claims that
correcting for precession and proper motion "brings the values into agreement, validating
the method". It cannot: precession moves a star about 4.5° in 320 years and Aldebaran's
proper motion amounts to roughly one arcminute over the same span, against a claimed
discrepancy of nine hours. The sidereal-time constant is wrong (2h 18m 24s, where Greenwich
mean sidereal time at 0h that date was 3h 11m 57s New Style or 3h 51m 22s Old Style), the
arithmetic does not reproduce itself (1.0027379 × 16h 58m 37s is 17h 01m 24s, not the
17h 02m 00s printed), and the whole observation is dated nine years before the mural arc's
first observation. Delete and rebuild on a real post-1689 observation. Ledger: ch04-014
through ch04-020.

**2. A drafting note was left in the manuscript.** Chapter 4's worked example contains
"Wait—I made an error. Refraction makes the star appear higher, so we subtract the
refraction to get the true altitude. Let me correct:" in the author's first-person drafting
voice, along with the wrong intermediate line it corrects. This is in a book going to print.
Ledger: ch04-101.

**3. Chapter 1 cites a newspaper that did not exist.** The footnote on the disaster rests on
"the *Weekly Journal* of 3 November 1707". The Weekly Journal, or Saturday's Post was
founded by Nathaniel Mist on 15 December 1716, nine years after the wreck. The same footnote
cites a "court of inquiry transcript"; there was no court of inquiry. Only the surviving
officers of the *Firebrand* were court-martialled, as a formality, and were acquitted.
The court of inquiry finding "nobody obviously at fault" appears twice in the chapter.
Ledger: ch01-002, ch01-104.

**4. Two bibliography entries name books that do not exist**, and both are load-bearing for
the instrument and clock claims.
- `Betts1978`, "Harrison: The Cabinet of Arts and Sciences", National Maritime Museum, 1978.
  Jonathan Betts did not join the National Maritime Museum until 1980 and his Harrison
  monograph is 1993. No such title exists. It is cited five times, including as the
  authority for Tompion's clocks, which a Harrison book would not cover anyway.
- `NMGMT`, "Conservation Report: Thomas Tompion's Clocks at Greenwich Observatory",
  National Maritime Museum, 1999. Untraceable in any catalogue.

  `Willmoth1992` ("The Biographical Work of John Flamsteed", Greshop Press) is also
  untraceable; the real book is Willmoth's *Sir Jonas Moore: Practical Mathematics and
  Restoration Science*, Boydell, 1993. `verification.yaml` already flags all three
  `not-found`. Ledger: ch03-011, ch01-005.

**5. Chapter 3 opens on a scene that could not have happened.** "On the afternoon of
22 June 1675 … John Flamsteed stood in the empty rooms of Flamsteed House" — the building
did not exist. Its foundation stone was laid on 10 August 1675 and Flamsteed moved in on
10 July 1676. The same paragraph has him holding the two Tompion clocks, delivered summer
1676, and inheriting "transit instruments from earlier observers", of whom there were none.
Move the scene to summer 1676. Ledger: ch03-001, ch03-102.

**6. Chapter 3 says Flamsteed's clocks kept sidereal time. They kept mean solar time.**
The Royal Observatory Greenwich study of his clock work states that all his clocks except
the unsuccessful Degree Clock of 1691 were set to mean solar time, and that the Degree Clock
was rarely if ever used. The chapter builds a further claim on the error, that Flamsteed's
"adoption of sidereal timekeeping … set a precedent that eventually led to the definition of
Greenwich Sidereal Time as a world standard". Chapters 4 and 5 both treat the clock reading
as mean solar, so the book contradicts itself. Ledger: ch03-013.

**7. Chapter 2 has Jonas Moore paying for an instrument built nine years after he died.**
The mural arc's expense is described as one "that Moore and other patrons helped defray".
Moore died on 27 August 1679; construction began in 1688. Flamsteed paid for it himself, over
£120, out of an inheritance — which is both documented and a stronger illustration of the
chapter's argument about his salary. Ledger: ch02-015.

**8. The mural arc is given three different construction spans in three chapters:**
1679–1691 (ch2), 1689–1691 (ch3 and ch4). It was built 1688–1689; first observation
11 September 1689, last 27 December 1719. Ledger: ch02-012, ch03-006, ch04-002.

**9. Chapter 2 puts the mural arc in the wrong building.** The Octagon Room is described as
"designed to house long-focus telescopes and the great mural arc". The Octagon Room's walls
are not aligned to a meridian, which is why it was nearly useless for positional work; the
arc hung on the west wall of the Quadrant House, a detached building in the garden.
Chapter 4 repeats the error, putting the arc on "the meridian wall of Flamsteed House".
Ledger: ch02-102, ch04-001.

**10. Chapter 1's Polaris footnote is wrong by a factor of two and a half.** It says Polaris
lay "within about 1°" of the pole in the seventeenth century. It was 2° 52′ away in 1600,
2° 27′ in 1675 and 2° 16′ at the time of the wreck. The size of that correction is the whole
reason pole-star regiment tables existed. Ledger: ch01-102.

**11. Chapter 1's dead-reckoning equations have the trigonometry swapped and are
dimensionally inconsistent.** With heading measured clockwise from north, northing is
v cos θ and easting is v sin θ; the chapter prints the reverse. Separately, the left-hand
side of the first equation is Δλ, an angle, while the right-hand side is a distance;
departure must be divided by cos φ. Ledger: ch01-103.

**12. Three of the five entries in chapter 1's disaster catalogue are wrong, and one is not
a disaster.**
- *São Thomé*: 1589, not 1591; homeward from India, not bound for it; lost off southern
  Mozambique, not near Sumatra. The complement of 944 could not be sourced.
- *Eendracht*: 1616, not 1615, and the ship **was not lost**. Dirk Hartog left the pewter
  plate at Cape Inscription and reached Batavia safely on 14 December 1616.
- *Tryall*: 1622, not 1656. The survivors were not marooned; 44 of them reached Bantam by
  longboat and skiff on 21 June 1622.
- **1691**: two ships lost, not five, and the cause was a full south-south-east gale, not
  fog and not a longitude error. The fleet bore up for Plymouth Sound precisely because it
  knew where the Eddystone was.

  Ledger: ch01-106 through ch01-109.

**13. Chapter 2's account of Flamsteed's assistant is wrong in every particular.** "His
assistant, Abraham Sharp … was paid £20 per year—leaving Flamsteed less than £80." Sharp was
not there in 1675 (he was at Greenwich 1684–85, August 1688 to autumn 1690, and from 1705 as
a calculator); the Observatory assistant was carried by the Board of Ordnance at 18d a day,
about £27 4s 6d, not by Flamsteed; so the subtraction does not follow. The parenthetical
"who would later become the second-best observational astronomer in Britain" is a ranking no
source makes. Ledger: ch02-103.

**14. Chapter 4 claims temperature compensation that did not exist in 1676.** Tompion's
clocks are credited with "brass and steel construction (minimizing thermal effects … by
employing differential expansion)". Compensated pendulums begin with Graham's mercury
pendulum of 1721 and Harrison's gridiron of about 1726. This directly contradicts chapter 2's
footnote, corrected earlier today to read "no temperature compensation of any sort".
Ledger: ch04-012.

**15. Chapter 4 says Tompion's clocks "would not be surpassed until the 19th century".**
Graham (1721) and Harrison's wooden regulators of the later 1720s both surpassed them inside
the eighteenth century. Ledger: ch04-103.

**16. Chapter 2 gets the star count off by one in a sentence that says "exactly".** The
*Historia Coelestis Britannica* catalogue holds 2,935 stars, not 2,934. Ledger: ch02-104.

---

## Per-chapter corrections

### Chapter 1 — The Deadly Ignorance of Position

| id | claim as printed | correction | source |
|---|---|---|---|
| ch01-002 | "*Weekly Journal* of 3 November 1707" and a court of inquiry transcript | The Weekly Journal began 15 Dec 1716. No court of inquiry was held; only the *Firebrand*'s officers were court-martialled, and acquitted. | [LoC catalogue, The Weekly Journal, or, Saturday's Post](https://www.loc.gov/item/2014218664/) |
| ch01-005 | "Willmoth's *Flamsteed's Stars*" | Ed. Frances Willmoth, *Flamsteed's Stars: New Perspectives on the Life and Work of the First Astronomer Royal, 1646–1719*, Boydell, **1997**. The `.bib` subtitle "The Catalogue of the Brightest Stars" is invented, the year is wrong, and the key misspells the surname. | [Boydell and Brewer](https://boydellandbrewer.com/9780851157061/flamsteeds-stars/) |
| ch01-007 | Longitude Act "established the Board of Longitude in perpetuity" | Dissolved by Act of Parliament in 1828. The Act named 24 commissioners; they did not meet formally until 1737. Cite as 12 Anne, Stat. 2, c. 15. | [ROG, Longitude Acts](https://www.royalobservatorygreenwich.org/articles.php?article=1309) |
| ch01-010 | "Charles II's warrant of 4 March 1675 is the founding document" | 4 March 1675 appointed Flamsteed astronomical observator. The **22 June 1675** warrant founded the Observatory. Chapter 2 states this correctly, so ch1 contradicts ch2. | [ROG, Royal Warrants](https://www.royalobservatorygreenwich.org/articles.php?article=909) |
| ch01-101 | latitude "to within one degree, the apparent diameter of the full Moon" | The Moon is about **half** a degree across. | mean lunar diameter ≈ 31′ |
| ch01-102 | Polaris "within about 1° of the true pole" in the 17th century | 2° 52′ in 1600, 2° 27′ in 1675, 2° 16′ in 1707. | computed by precessing the J2000 position with IAU 1976 angles; the same computation reproduces the known 1900.0 declination of +88° 46′ |
| ch01-103 | Δλ = ∫v cos θ dτ eastward, Δφ = ∫v sin θ dτ northward | Swapped. Northing is v cos θ, easting v sin θ. Also dimensionally inconsistent: departure must be divided by cos φ to give a longitude difference. | plane sailing |
| ch01-104 | "The court of inquiry … found nobody obviously at fault" (twice) | No inquiry was held. | as ch01-002 |
| ch01-106 | 1591 São Thomé, bound for India, wrecked near Sumatra, 944 aboard | 1589, **homeward** from India, lost off southern Mozambique. Complement unsourced. | Diogo do Couto's narrative in the *História Trágico-Marítima* |
| ch01-107 | 1615 Eendracht, "the ship was lost" | 1616, and the ship survived — reached Batavia 14 Dec 1616. | Western Australian Museum; National Museum of Australia |
| ch01-108 | 1656 Tryall, forty marooned, "only a handful ever rescued" | 25 May 1622; 44 survivors reached Bantam on 21 June 1622. | [WA Museum, Trial 1622](https://visit.museum.wa.gov.au/trial-1622) |
| ch01-109 | 1691, five ships lost in fog at Plymouth | Two lost (*Coronation*, *Harwich*) on 3 Sept 1691 in a gale, about 900 dead. Not fog, not a longitude failure. | wreck records for HMS Coronation and HMS Harwich |

Left unverified: the whole dead-reckoning error table (ch01-012 to ch01-016, unsourced, and
its 40-day row of 150–250 nm contradicts the chapter's own 40 nm disaster threshold), the
"more than forty nautical miles off course" figure (ch01-105), and the "three centuries"
span (ch01-003).

### Chapter 2 — The Founding of the Royal Observatory

| id | claim as printed | correction | source |
|---|---|---|---|
| ch02-002 | "The position was officially created by Royal Warrant, 22 June 1675" | Reversed. The post was created 4 March 1675; the Observatory on 22 June 1675. | [ROG, Royal Warrants](https://www.royalobservatorygreenwich.org/articles.php?article=909) |
| ch02-004, ch02-021 | the investment was "unprecedented"; the institution "unprecedented in the history of astronomy" | The Paris Observatory (1667) preceded it on the same model. Supportable claim: Britain's **first state-funded** scientific research institution. | [RMG, founding of the Royal Observatory](https://www.rmg.co.uk/stories/space-astronomy/curatorial/founding-royal-observatory) |
| ch02-006 | warrant "resolved to establish an observatory" … "rectifying the tables of the motions of the heavens" | The warrant says "we have resolved to **build a small observatory within our park at Greenwich**". The "rectifying the tables" phrase is **not in it**; it is from the 4 March warrant. The warrant is not terse. | [warrant text](https://www.royalobservatorygreenwich.org/articles.php?article=977) |
| ch02-007 (fn) | Wren "complained the sum was 'far too little'"; costs ran to £520 "with Moore supplying additional funds" | Quotation untraceable, and at odds with Wren's one recorded remark, that he built it "for the observator's habitation and a little for pompe". Outturn was £520 9s 1d; Moore funded **instruments**, not fabric. | [ROG, Flamsteed House](https://www.royalobservatorygreenwich.org/articles.php?article=916) |
| ch02-011 | Flamsteed "could not commission instruments from professional makers as Tycho had done" | He did. Moore paid for the 7-ft sextant, Hooke's 10-ft mural quadrant and the two Tompion clocks, all 1676. | [ROG, Private Patronage](https://www.royalobservatorygreenwich.org/articles.php?article=961) |
| ch02-012 | mural arc "between 1679 and 1691" | 1688–1689; in service 1689–1719. | [ROG, Flamsteed's Mural Arc](https://www.royalobservatorygreenwich.org/articles.php?article=1045) |
| ch02-015 | arc expense "that Moore and other patrons helped defray" | Moore died 27 Aug 1679. Flamsteed paid over £120 himself from an inheritance. | as above, plus ROG Private Patronage |
| ch02-018 | 10–20″ is "an order of magnitude improvement over Tycho" | Tycho approached 1′ (60″), so the factor is about 4–6. | [Oxford, Hven 1576–97](https://www.cabinet.ox.ac.uk/hven-1576-97-tycho-brahes-observatory) |
| ch02-101 | "four stories tall, with a distinctive octagonal turret rising from the northwest corner" | Three storeys; **four** turrets, one at each corner. | [ROG, Flamsteed House](https://www.royalobservatorygreenwich.org/articles.php?article=916) |
| ch02-102 | Octagon Room "designed to house … the great mural arc" | The arc was in the Quadrant House. The Octagon Room's walls are not on a meridian. | as above |
| ch02-103 | Sharp as 1675 assistant, paid £20/yr, "second-best observational astronomer in Britain" | Sharp arrived 1684. Assistant paid 18d/day (≈£27 4s 6d) by the Ordnance, not by Flamsteed. Ranking unsourceable. | [ROG, Abraham Sharp](https://www.royalobservatorygreenwich.org/articles.php?article=1148); [ROG, Board of Ordnance funding](https://www.royalobservatorygreenwich.org/articles.php?article=957) |
| ch02-104 | "exactly 2,934 stars" | 2,935. | ROG article 1045 |
| ch02-105 | "inherited a sextant of seven-foot radius" | Newly made 1676 at Moore's expense; the most-used instrument until 1689. | ROG Private Patronage |
| ch02-106 | "Abraham Sharp remained his indispensable assistant" (in 1709) | Sharp left in autumn 1690. | ROG article 1148 |

Also corrected in the ledger: ch02-010, where the extracted text is stale (the `.tex`
footnote was fixed earlier today). Two residual problems remain in the body: the clocks stood
in the Octagon Room on the first floor, not "on the ground floor", and the "ten or fifteen
seconds per day" figure is one of four incompatible numbers the book gives.

Left unverified: the 1709 petition to the Admiralty and the £200 request (ch02-019,
ch02-020). Royal Observatory Greenwich's account of Ordnance funding records no petition and
no increase, and oversight passed to a Royal Society Board of Visitors in 1710, not the
Admiralty. The claim that living costs "roughly doubled since 1675" needs a price-index
citation. Also unverified: the circumpolar-first observing order (ch02-016).

### Chapter 3 — Instruments and Methods of the Observatory

| id | claim as printed | correction | source |
|---|---|---|---|
| ch03-001 | Flamsteed in Flamsteed House on 22 June 1675 with the Tompion clocks | Building not begun until 10 Aug 1675, completed summer 1676; clocks delivered summer 1676. | [RMG founding](https://www.rmg.co.uk/stories/space-astronomy/curatorial/founding-royal-observatory); [RMG Year-Going Clock](https://www.rmg.co.uk/collections/objects/rmgc-object-202113) |
| ch03-003 | Tycho "observing from … Uraniborg … from 1576 until his death in 1601" | He left Hven in 1597 and died in **Prague** on 24 Oct 1601. Much of the precision work was at Stjerneborg. | [Oxford, Hven 1576–97](https://www.cabinet.ox.ac.uk/hven-1576-97-tycho-brahes-observatory) |
| ch03-006 | mural arc "between 1689 and 1691" | 1688–1689. Radius 79½ in (6 ft 7½ in) is fine. | ROG article 1045 |
| ch03-010 | "Huygens's principle of isochronous oscillation" | Huygens proved the circular pendulum is **not** isochronous; his answer was the cycloidal cheek (*Horologium Oscillatorium*, 1673). Chapter 6 states this correctly. | Huygens 1673 |
| ch03-011 | `Betts1978` and `NMGMT` | Neither exists. Betts joined the NMM in 1980; his *Harrison* is 1993. Replace with the RMG object record and ROG article 1381. | [Jonathan Betts biography](https://en.wikipedia.org/wiki/Jonathan_Betts) (lead), NMM catalogue |
| ch03-013 | "Each clock … set to sidereal time" | Mean solar time. Only the unsuccessful Degree Clock (1691) was sidereal, and it was rarely used. | [ROG, Decoding Flamsteed](https://www.royalobservatorygreenwich.org/articles.php?article=1381) |
| ch03-016 | "factor of five to ten"; Tycho at "one to three arc-minutes" | Tycho approached 1′. Factor about 4. | Oxford Hven page |
| ch03-021 | "The next chapter traces … the bitter controversy with Newton and Halley" | That is chapter 5. Chapter 4 is the mural arc and transits. | internal |
| ch03-101 | eye resolves ~1′, "about the angular width of a grain of wheat held at arm's length" | 1′ at arm's length is 0.17 mm; a wheat grain subtends about 17′. Resolution figure right, illustration wrong by ~20×. | geometry |
| ch03-102 | "inherited some transit instruments from earlier observers" | There were no earlier observers. Everything came from Moore in 1676. | ROG Private Patronage |

Left unverified: Tycho's quarter-arcminute graduation (ch03-103), the Tompion accuracy figure
(ch03-104, four incompatible values across the book), and both Howse and Baily page
references (ch03-007, ch03-017 — note ch2 cites Howse ch. 3 and ch3 cites Howse ch. 4 for the
same instrument, and the two Baily ranges overlap for unrelated content).

Verified and worth keeping: precession at ~50″/yr, Bradley on aberration in the 1720s,
T = 2π√(L/g), horizon refraction ≈ 35′, Flamsteed observing 1676 to his death on
31 December 1719, catalogue of ~3,000 stars.

### Chapter 4 — The Mural Arc and the Method of Transits

| id | claim as printed | correction | source |
|---|---|---|---|
| ch04-001 | arc in Flamsteed House; altitude read "to perhaps one-tenth of a degree" | Arc hung in the Quadrant House. One tenth of a degree is 6′, twenty times coarser than the graduation the same chapter claims. | ROG articles 1045, 916 |
| ch04-002 | "between 1689 and 1691" | 1688–1689. | ROG article 1045 |
| ch04-003 | "a curved wall of iron … radius approximately 6.75 feet" | **Brass**, on iron support bands with wooden reinforcement. Radius 79½ in = 6.63 ft. The chapter contradicts itself two sentences later ("cutting the lines into brass"). The 140° span could not be confirmed. | ROG article 1045 |
| ch04-011 | clocks "commissioned by Jonas Moore in 1676 and delivered … in 1677" | Commissioned late 1675, delivered summer 1676, probably 7 July. | [RMG Year-Going Clock](https://www.rmg.co.uk/collections/objects/rmgc-object-202113) |
| ch04-012 | anchor escapement; brass-and-steel temperature compensation | Prototype **dead-beat** escapement; **no** temperature compensation. The book now names four different escapements for the same two clocks (dead-beat ch2, anchor ch4, remontoire ch6:52, constant-force ch6 table). | RMG object 202113 |
| ch04-013 | 10–15 °C swing gives "a second or more per day" | About **6 s/day** for an uncompensated steel rod (½ · 11.5 ppm/K · 12 K · 86400 s). | thermal expansion of steel |
| ch04-014 | Aldebaran observed 8 Nov 1680 with the mural arc | The arc's first observation was 11 Sept 1689. | ROG article 1045 |
| ch04-015 | α₀ = 2h 18m 24s | GMST at 0h was 3h 11m 57s (Gregorian date) or 3h 51m 22s (Old Style date). | computed |
| ch04-016 | h_obs = 61° 24′ 32″ | Aldebaran's 1680 meridian altitude at Greenwich was ≈54° 21′. It also transited near 1h mean solar time, not 16h 58m. | computed from the J2000 position with IAU 1976 precession |
| ch04-017 | R ≈ 50″ | The chapter's own formula gives 32″ at that altitude. | 58.3″ cot h |
| ch04-019 | "differs by roughly 9 hours … and 6 degrees" | 14h 44m 29s (9h 15m 31s the short way) and 6° 22′; and the underlying figures are invented. The printed arithmetic also fails: 17h 01m 24s, sum 19h 19m 48s. | computed |
| ch04-020 | precession and proper motion "brings the values into agreement" | False. Precession ≈4.5° over 320 yr; Aldebaran's proper motion ≈1′. Correct 1680 position: 4h 17m 37s, +15° 49′ 14″. | computed |
| ch04-022 | "factor of 3 or more"; Tycho at 1–3′ | Tycho approached 1′; factor about 4–6. | Oxford Hven page |
| ch04-101 | "Wait—I made an error … Let me correct:" | Drafting artifact. Remove. | internal |
| ch04-102 | "the longitude correction accounts for the observer being at Greenwich rather than the Prime Meridian" | Greenwich **is** the prime meridian; the term is zero there. The neighbouring reference to the equation of time is also confused — it relates apparent to mean solar time, not mean solar to sidereal. | definition |
| ch04-103 | "would not be surpassed until the 19th century" | Graham 1721; Harrison's wooden regulators of the later 1720s (~1 s/month). | horological record |
| ch04-104 | clocks rated against noon transit "using a gnomon … and a marked scale on the floor" | Flamsteed rated them from **altitude** observations of the Sun or stars, 3–5 readings over ~5 min with a small quadrant in the Octagon Room, 30–50 sets a year, plus equal-altitude pairs. Chapter 5 repeats the gnomon claim. | [ROG, Decoding Flamsteed](https://www.royalobservatorygreenwich.org/articles.php?article=1381) |
| ch04-105 | figure caption: refraction near the horizon "exceeds five arcminutes" | ≈35′. The chapter's own formula gives 5.5′ at 10° and 55.7′ at 1°, so the caption contradicts the equation beside it. Chapters 3 and 8 both give 35′. | standard refraction |
| ch04-106 | eye "could resolve perhaps one or two arcseconds" | ~1′ on the sky. Chapter 3 gets this right. The passage needs to distinguish sky resolution from judging a fraction of a division on brass. | visual acuity |
| ch04-107 | clock reading "in Greenwich Mean Time" | Anachronistic in 1680. Local mean solar time at Greenwich. | ROG article 1381 |

Left unverified: the error-budget magnitudes (ch04-006 to ch04-009, ch04-021). The numbers are
internally consistent but nothing sources them; Chapman's *Dividing the Circle* or a Journal
for the History of Astronomy residual analysis would settle them.

---

## Contradictions with other chapters

Found by grepping `src/chapters/` for the shared facts. These are reported, not fixed —
several will need a decision that spans chapters outside this assignment.

**The Flamsteed-over-Tycho improvement factor is stated five different ways.** Chapter 2 says
"an order of magnitude"; its own figure caption says "approximately four times"; chapter 3
says "a factor of five to ten"; chapter 4 says "a factor of 3 or more"; chapter 5 line 170
says "a threefold improvement". The defensible figure, with Tycho approaching 1′ and
Flamsteed at 10–20″, is about four to six. Pick one and propagate it.

**Tycho's own error is stated two ways.** "One to three arc-minutes" in chapters 3, 4 and 5;
the sourced figure is accuracy approaching one arcminute.

**The Tompion clocks are given four escapements and four accuracies.** Escapement: dead-beat
(ch2 footnote, correct), anchor (ch4), remontoire (ch6 line 52), constant-force (ch6 table
line 180). Accuracy: 10–15 s/day (ch2, ch3), "a few seconds" (ch4), ±5 s and ±3 s (ch6 table).
Royal Museums Greenwich claims two seconds a day. Chapter 6's table line 181 also invents a
second "Tompion regulator, 1710, improved thermal compensation" at Greenwich, which needs
checking on its own — it is outside my chapters but it conflicts with chapter 2's corrected
"no temperature compensation of any sort".

**Horizon refraction is given two values.** ≈35′ in chapter 3 (caption) and chapter 8 line
103; "exceeds five arcminutes" in chapter 4's caption and "several arcminutes" in its body.
Chapter 4 is wrong.

**Sidereal versus mean solar clock time.** Chapter 3 says the Greenwich clocks were set to
sidereal time; chapters 4 and 5 both treat the reading as mean solar and convert. Chapter 3
is wrong.

**The clock-rating method.** Chapter 4 and chapter 5 line 32 both describe a gnomon and a
floor scale in Flamsteed House; the Royal Observatory Greenwich account describes altitude
and equal-altitude observations with a small quadrant. Both chapters need the same fix.

**Who calls the transit time.** Chapter 4 opens with the assistant calling the time and
Flamsteed reading the arc; chapter 4's own "Human factors" section reverses it; chapter 3 has
the assistant calling; chapter 2 has Flamsteed calling. Chapter 13 line 4 has Airy calling to
his assistant, which is separately documented and probably the model the earlier chapters
were reaching for.

**Howse chapter references disagree.** Chapter 2 cites Howse chapter 3 for the mural arc;
chapter 3 cites Howse chapter 4 for the same instrument. One is wrong, and I could not reach
a copy to say which.

**The founding warrant.** Chapter 1's footnote calls the warrant of 4 March 1675 "the
founding document"; chapter 2 correctly gives 22 June 1675. Chapter 1 is wrong.

---

## Citation keys flagged `not-found` in `review/refs/verification.yaml`

Used in chapters 1–4 and confirmed by me as unsound:

- **`Betts1978`** — does not exist (see must-fix 4). Cited 5×. Every sentence it supports
  about Tompion's clocks needs a real source; use the Royal Museums Greenwich object record
  for the year-going clock and Royal Observatory Greenwich article 1381.
- **`Willmoth1992`** — "The Biographical Work of John Flamsteed", Greshop Press, does not
  exist. Cited 3×, in chapters 2 and 3. The nearest real work is Frances Willmoth, *Sir Jonas
  Moore: Practical Mathematics and Restoration Science*, Boydell, 1993, which is in fact the
  right source for chapter 2's Moore material.
- **`Flamsteed1725`** — the work is real (*Historia Coelestis Britannica*, 3 vols, 1725), so
  the `not-found` status is a cataloguing artifact, not an error. Scans are on the Internet
  Archive. But chapter 3 cites "Prolegomena, pp. 12–18" for clock correction procedures and I
  could not check that page range.

Two more entries in the same file are wrong without being flagged:

- **`WilmothFlamsteeds2002`** — correct is Willmoth (ed.), *Flamsteed's Stars: New
  Perspectives on the Life and Work of the First Astronomer Royal, 1646–1719*, Boydell, 1997.
  Wrong year, invented subtitle, misspelled key, and it is an edited volume so chapters should
  be cited individually.
- **`Chapman1996`** — *Dividing the Circle* was published by Ellis Horwood in **1990** and in
  a second Wiley-Praxis edition in **1995**. There is no 1996 edition. The full title carries
  the date range "1500–1850". Worse, the same book appears **twice** in the bibliography:
  `Chapman1996` at line 68 and `Chapman2003` at line 956, the latter dating the second
  edition to 2003. Both years are wrong and the two keys are cited independently across the
  book. Merge them onto Chapman, *Dividing the Circle*, 2nd edn, Wiley-Praxis, 1995,
  ISBN 0-471-96169-8.
- **`Howse1980`** — the 1980 Oxford University Press edition is titled *Greenwich Time and
  the **Discovery of the** Longitude*; the shortened title in the `.bib` belongs to the 1997
  revision. Chapter 1 also cites "Howse, *Measure of All Things*", which is not a Howse title
  at all and has no `.bib` entry.
