# Appendix B, Instrument Specifications: fact-check

Source file: `src/appendices/appendix-b.tex`
Ledger: `review/claims/appb.yaml`
Checked: 30 instrument rows across five tables, plus 3 prose claims in the section introductions. 34 ledger entries in total.

**Result: 32 of 34 entries need correction. 1 is clean. 1 could not be checked.**

Every numeric field in these tables should be treated as unsourced until re-derived. The pattern is not random noise. Apertures are wrong by consistent factors of about 2.5, which points to a unit or designation slip; several rows put escapement values in the compensation column and vice versa; and four rows carry placeholder text (`Instrument maker`, `Various`, `Multiple`, `Chronometer`) where a real value was never known. Roughly a third of the accuracy and rate figures could not be traced to any source at all.

---

## MUST FIX BEFORE PRINT

Ordered by severity. Items 1 to 4 are the ones a reviewer will catch.

### 1. Halley transit instrument: wrong date, impossible mounting, placeholder maker

Four independent errors in one row. The date should be **1721**, not 1710: Halley did not become Astronomer Royal until 1720, and the instrument came into use in 1721. The maker column reads `Instrument maker`, which is not a value; the maker is genuinely **unknown** (Lalande attributed it to Hooke in 1759, but Hooke died in 1702 and the attribution is rejected). Aperture is **1.75 inches, 44 mm**, not 100 mm. And a transit instrument cannot have an **equatorial mounting**; this one turned on a horizontal axis 3 ft 6 in long, fixed in the meridian, with the tube mounted 13 inches off-centre.

Source: [ROG, Halley's 5-foot Transit Instrument](https://www.royalobservatorygreenwich.org/articles.php?article=1076)

### 2. Photographic zenith tube: date wrong by 55 years, wrong site, anachronistic graduation

The Royal Observatory's photographic zenith tube came into use in **1955**, took over time determination on 16 October 1957, and ran until 30 June 1984. It was built by **Grubb Parsons**, not `Various`, one of three (Neuchatel 1954, Greenwich 1955, Mount Stromlo 1956). It stood at **Herstmonceux**, not Greenwich. The graduation `digital` is not merely anachronistic; a PZT has **no graduated circle at all**, because it records star images photographically.

Source: [ROG, Photographic Zenith Tube](https://www.royalobservatorygreenwich.org/articles.php?article=1071), [Scientific Instrument Society on the Neuchatel PZT](https://scientificinstrumentsociety.org/eliminating-errors-automating-observation-the-photographic-zenith-tube-of-the-neuchatel-observatory-in-switzerland/)

### 3. "Hadley quadrant" is not a separate instrument from the Hadley octant

The navigation table lists these as two devices with different date ranges, different frames and different steadiness. They are **two names for the same instrument**. It measures angles up to 90 degrees on a physical arc of only 45 degrees, because paired mirrors double the reflection angle, and it was therefore known both as an octant and as Hadley's quadrant. The second row should be **deleted** and the first relabelled to give both names.

Source: [History of Science Museum, Oxford: Octant](https://www.hsm.ox.ac.uk/octant), [Britannica: octant](https://www.britannica.com/technology/octant)

### 4. Three telescope apertures wrong by a factor of about 2.5

| Telescope | Printed | Correct | Nature of the error |
|---|---|---|---|
| Isaac Newton Telescope | 980 mm | **2.54 m** | 98-inch designation read as 98 cm |
| Herschel 20-ft | 190 mm | **475 mm** (18.7 in) | not the small 20-ft either, which was 305 mm |
| Herschel 40-ft | 490 mm | **1.22 m** (48 in) | 49.5-inch blank mis-converted |

The INT error makes the book's largest telescope smaller than the Greenwich 28-inch refractor sitting two rows above it in the same table.

### 5. Airy transit circle: three of five specifications wrong

This is the anchor instrument for the book's argument and the one a specialist reader will check first.

| Field | Printed | Correct |
|---|---|---|
| Aperture | 170 mm | **206 mm** (8.1 in clear aperture) |
| Circle | 1.37 m | **1.83 m** (6 ft, cast iron) |
| Graduation | 1 arcmin | **5 arcmin**, read by 6 of 10 micrometer microscopes |
| Focal length | not given | 3.53 m (11 ft 7 in) |

The notes column also omits the single most important fact about it: **it defines the prime meridian**. Maker should acknowledge that Troughton and Simms did the optics and instrumentation while Ransomes and May of Ipswich did the heavy engineering.

Source: [Greenwich Observations 1908, description of the Airy Transit Circle](https://www.royalobservatorygreenwich.org/articles.php?article=1233)

### 6. Tompion regulators, 1676, credited with a gridiron pendulum

A 50-year anachronism. The **gridiron pendulum is Harrison's, from about 1726**. Tompion's two year-going clocks of 1676 had no temperature compensation whatever. Their escapement was an early form of **dead-beat**, not anchor. Stated accuracy of 1 s/day is optimistic; sources give about 2 s/day, improving to within 8 seconds per month after adjustment.

Source: [RMG, Year-Going Clock](https://www.rmg.co.uk/collections/objects/rmgc-object-202113), [ROG, Decoding Flamsteed](https://www.royalobservatorygreenwich.org/articles.php?article=1381)

### 7. Shepherd master clock dated 1880 instead of 1852

Charles Shepherd installed the master clock and its sympathetic network in **1852**, the gate dial on 13 August 1852, and it remained the heart of Britain's time system until 1893. Escapement `Spring detent` is wrong: it is an electrically controlled clock under Shepherd's 1849 galvanic patent, not a detent chronometer escapement.

Source: [RMG, Shepherd Gate Clock](https://www.rmg.co.uk/royal-observatory/attractions/shepherd-gate-clock)

### 8. Shortt free-pendulum accuracy understated by at least twelvefold

The Shortt-Synchronome kept time to about **one second per year**, not one second per month; a 1984 test at the US Naval Observatory found one second in ten years. The date should be **1921**. This error runs against the direction of the book's argument, since it makes the best mechanical clock ever built look worse than it was.

Source: [Shortt-Synchronome clock](https://en.wikipedia.org/wiki/Shortt%E2%80%93Synchronome_clock), [The Clockworks, free pendulum No. 47](https://theclockworks.org/collection-online/free-pendulum-and-subsidiary-no-47)

### 9. Bradley's 1750 transit instrument attributed to Graham

The maker was **John Bird**, ordered 1749, in use September 1750. Graham had made the earlier instruments. Aperture is **2.7 inches, 69 mm**, stopped to 1.5 in by the wire-illumination screen, not 120 mm.

Source: [ROG, Bradley's 8-foot Transit Instrument](https://www.royalobservatorygreenwich.org/articles.php?article=1296)

### 10. Bird 8-ft quadrant: two instruments conflated, and a mural quadrant called portable

Bird's 8-ft brass mural quadrant of **1750 was Bradley's, at Greenwich**. His 8-ft quadrants for the Radcliffe Observatory, **Oxford, date from 1772-73**. The row pairs the Greenwich date with the Oxford location. `Portable design` is wrong either way: a mural quadrant is bolted to a wall in the plane of the meridian. Aperture 240 mm is wrong; the 1773 Radcliffe quadrant has a 3-inch (76 mm) object glass.

### 11. Caesium row conflates two clocks 44 years apart

`1955+` is Essen's caesium standard at the National Physical Laboratory, accurate to about 1 ms/day, roughly **1 second in 300 years**. `NIST-F1` is a caesium fountain that began operating in **1999**, accurate to **1 second in 20 million years**, not 30 million. Pick one.

Source: [NIST, brief history of atomic clocks](https://www.nist.gov/pml/time-and-frequency-division/time-services/brief-history-atomic-clocks-nist)

### 12. Harrison H1 listed as having no temperature compensation

`Compensation: None` is wrong and it inverts the historical point. **H1 carries Harrison's gridiron** of brass and steel, which compensates temperature by shifting the attachment point of the balance springs. Its escapement is the **grasshopper**; `Linked balance` describes the oscillator, not the escapement.

### 13. Escapement and compensation columns swapped or wrong across the Harrison rows

| Row | Escapement printed | Escapement actual | Compensation printed | Compensation actual |
|---|---|---|---|---|
| H1 | Linked balance | grasshopper | None | gridiron |
| H2 | Similar | grasshopper | Temperature trim | unverified |
| H3 | Bi-metallic balance | grasshopper | Integral | **bimetallic strip** |
| H4 | Detent | **modified verge, diamond pallets** | Diamond pallets | bimetallic curb |
| H5 | Detent | verge, diamond pallets | Bi-metallic | correct |
| K1 | Copy of H4 (fair) | verge, diamond pallets | Diamond pallets | bimetallic curb |

The **detent escapement is Arnold and Earnshaw's, from about 1780-82**, two decades after H4. Attributing it to Harrison erases the distinction the chronometer section depends on. Diamond pallets are escapement components and do not belong in a compensation column.

Source: [Annals of Science on H4's diamond pallets](https://www.tandfonline.com/doi/abs/10.1080/00033790701619675), [SJX Watches on H4](https://watchesbysjx.com/2019/09/john-harrison-marine-chronometer-h4-diamond-pallets.html), [Redfern Animation, Arnold and Earnshaw](https://redfernanimation.com/arnold-and-earnshaw/)

### 14. Prose claim: silver and aluminium coatings dated post-1900

Silvered glass mirrors were introduced by **Steinheil and Foucault in 1856-57**, and vacuum-deposited aluminium by **John Strong in the 1930s**. Neither is post-1900 in the sense claimed, and silver tarnishes and needs re-silvering, so it does not eliminate the maintenance burden. The copper-tin description of speculum is correct.

### 15. Prose claim: "the largest reflectors of the 20th century"

The largest reflector in the table is the INT at 2.54 m. The largest reflectors of the century were the Hale 5 m (1949), BTA-6 6 m (1976) and Keck 10 m (1993). Rewrite as the largest reflector ever sited in the British Isles, which is what the INT actually was.

### 16. Prose claim: the 10^10 factor does not follow from the caption's own numbers

One second per day to one second per **million** years is a factor of 3.7e8. The 1e10 figure requires the caesium row at 30 million years. The caption and the table disagree. The span 1676 to 1999 is 323 years, not 350.

---

## Full field-by-field table

Legend: OK = checked against a source and correct. **WRONG** = contradicted by a source. **UNSOURCED** = no source reached documents this value, so it cannot be defended in print. Internal = contradicted by the book's own logic or by another cell in the same table.

### Meridian instruments (Table B.1)

| Instrument | Date | Maker | Aperture | Circle | Grad. | Accuracy | Notes |
|---|---|---|---|---|---|---|---|
| Flamsteed mural arc | OK 1689 | OK Abraham Sharp | **UNSOURCED** 130 mm, implausible for 1689 | **WRONG** column says circle; 2.1 m is the radius (79.5 in) of a 130-140 degree arc | UNSOURCED | UNSOURCED ±10 arcsec | OK Greenwich |
| Halley transit instr. | **WRONG** 1710, should be **1721** | **WRONG** placeholder, maker **unknown** | **WRONG** 100 mm, should be **44 mm** | **WRONG** no circle; tube is 1.69 m | **WRONG** setting circle only, does not survive | UNSOURCED ±15 arcsec | **WRONG** not equatorial; horizontal axis in the meridian |
| Bradley zenith sector | OK 1727 (19 August) | OK George Graham | OK 80 mm (about 3 in) | n/a | n/a | OK ±1 arcsec, conservative; source says 0.1 arcsec | **WRONG** Wanstead, not Greenwich |
| Bradley transit instr. | OK 1750 | **WRONG** Graham, should be **John Bird** | **WRONG** 120 mm, should be **69 mm** | **WRONG** no circle; 8 ft tube is 2.44 m | **WRONG** n/a | UNSOURCED ±5 arcsec | OK Greenwich, defined the meridian 1750-1816 |
| Bird 8-ft quadrant | **WRONG** 1750 is the Greenwich instrument; Oxford ones are **1772-73** | OK John Bird | **WRONG** 240 mm, should be **76 mm** | OK 2.4 m radius | **WRONG** 5 arcmin plus a 96-part scale, read to 1 arcsec | UNSOURCED ±8 arcsec | **WRONG** Oxford conflict; a mural quadrant is **not portable** |
| Airy transit circle | OK 1851 (built 1850, first obs 4 Jan 1851) | OK, incomplete: Ransomes and May did the engineering | **WRONG** 170 mm, should be **206 mm** | **WRONG** 1.37 m, should be **1.83 m** | **WRONG** 1 arcmin, should be **5 arcmin** | UNSOURCED ±0.5 arcsec, plausible | Incomplete: omits that it **defines the prime meridian** |
| Photographic ZT | **WRONG** 1900, should be **1955** | **WRONG** placeholder, should be **Grubb Parsons** | UNSOURCED 150 mm | n/a | **WRONG** digital, anachronistic; PZT has no circle | UNSOURCED ±0.3 arcsec | **WRONG** Herstmonceux, not Greenwich |

### Telescopes (Table B.2)

| Telescope | Aperture | Focal length | Type | Maker/Era | Location |
|---|---|---|---|---|---|
| Newton's reflector | OK 30 mm (documented 33 mm) | OK 160 mm (documented about 150 mm) | OK Newtonian | OK Newton 1668 | OK Cambridge |
| Herschel 20-ft | **WRONG** 190 mm, should be **475 mm** | OK 6.1 m | OK speculum | OK 1783 | **WRONG** Datchet; Slough only from April 1786 |
| Herschel 40-ft | **WRONG** 490 mm, should be **1.22 m** | OK 12.2 m | OK speculum | OK 1789 | OK Slough |
| Grubb 28-inch | OK 710 mm | **WRONG** 10.4 m, should be **8.48 m** (27 ft 10 in) | OK achromatic | OK Grubb 1893 | OK Greenwich Great Equatorial |
| Isaac Newton Telescope | **WRONG** 980 mm, should be **2.54 m** | **WRONG** 13.7 m matches no documented focus; primary is **7.475 m**, f/2.94 | OK reflector | OK Grubb Parsons, dedicated 1967, first light 1965 | OK Herstmonceux then La Palma (1984) |

### Navigational instruments (Table B.3)

| Type | Era | Makers | Arc range | Reading precision | Notes |
|---|---|---|---|---|---|
| Hadley octant | **WRONG** presented 1731; the 1780 end date is far too early, octants ran through the 19th century | **WRONG** placeholder | OK 0-90 degrees | UNSOURCED 2-3 arcmin; verniers of the period read to 1 arcmin | OK double reflection, portable |
| Hadley quadrant | **WRONG** — **the whole row is a duplicate of the octant under its other name. Delete it.** | | | | |
| Ramsden sextant | **WRONG** Ramsden died in 1800; an era to 1900 credits him with a century of others' work | Partly OK | OK 0-120 degrees | **UNSOURCED** 20-30 arcsec; typical Ramsden verniers read to 1 arcmin, the finest to 10 arcsec | OK vernier |
| Troughton sextant | **WRONG** the firm existed **1826-1922**, so neither 1800 nor 1950 is possible | **WRONG** before 1826 the maker is Edward Troughton alone | OK 0-120 degrees | UNSOURCED 10-20 arcsec | **WRONG** micrometer screws replaced verniers only around 1900 |
| 20th-c. sextant | OK | **WRONG** placeholder | OK 0-120 degrees | OK 10 arcsec, consistent with a micrometer drum | **WRONG** the bubble sextant is an **aviation** instrument (Gago Coutinho, 1922), not the marine standard |

### Chronometers (Table B.4)

| Chronometer | Date | Escapement | Compensation | Rate/day | Notes |
|---|---|---|---|---|---|
| Harrison H1 | OK 1735 (made 1730-35) | **WRONG** grasshopper | **WRONG** None; it has a **gridiron** | UNSOURCED ±5 s | **WRONG** built for sea, trialled to Lisbon 1736 |
| Harrison H2 | **WRONG** 1741, should be **1739** (made 1737-39) | **WRONG** placeholder; grasshopper | **WRONG** placeholder | UNSOURCED ±3 s | Partly OK; H2 was never sea-tried |
| Harrison H3 | OK 1759 (begun 1740) | **WRONG** grasshopper; the bimetallic strip is the compensation | **WRONG** placeholder; **bimetallic strip** | UNSOURCED ±1 s | OK major breakthrough |
| Harrison H4 | OK 1759 | **WRONG** detent; it is a **modified verge with diamond pallets** | **WRONG** diamond pallets belong to the escapement | UNSOURCED ±0.2 s | **WRONG** garbled; H4 **is** a watch, about 5 in across |
| Harrison H5 | **WRONG** 1772 is the trial; completed **1770** | **WRONG** verge with diamond pallets | OK bimetallic | **WRONG** the 1772 trial gave about **one-third second per day**, not 0.1 s | **WRONG** never a production model; a one-off |
| Kendall K1 | OK 1769 (presented 1770) | OK as description | **WRONG** diamond pallets are escapement, not compensation | UNSOURCED ±0.3 s | OK; sailed with Cook 1772-75 |
| Arnold marine chron. | OK 1780+ | **WRONG** placeholder; **spring detent**, patented 1782 | OK bimetallic | **UNSOURCED** ±0.5 s; sources give 1-2 s/day in service | OK |
| Earnshaw chron. | **WRONG** his spring detent dates from **1780**, not 1790 | OK spring detent | OK bimetallic | **UNSOURCED** ±0.5 s; same 1-2 s/day caveat | OK |

### Clocks (Table B.5)

| Clock | Date | Escapement | Compensation | Accuracy | Notes |
|---|---|---|---|---|---|
| Tompion regulators | OK 1676 | **WRONG** anchor; early **dead-beat** | **WRONG** gridiron is a **50-year anachronism**; these had none | **WRONG** about 2 s/day, later 8 s/month | OK Greenwich; 13-ft two-second pendulums |
| Graham regulator | Internal conflict: the **mercury pendulum is 1721**, not 1715 | **WRONG** anchor; **dead-beat**, which is the point of the entry | See date | UNSOURCED ±2 s/week | OK |
| Shepherd master | **WRONG** 1880, should be **1852** | **WRONG** spring detent; an electric system under Shepherd's 1849 patent | UNSOURCED | UNSOURCED ±0.1 s/day | OK electric impulse drive |
| Shortt free-pendulum | **WRONG** 1920, should be **1921** | OK free pendulum | Imprecise: compensation is the **Invar** pendulum; the vacuum removes barometric effects | **WRONG** about **1 s/year**, not 1 s/month | OK electromagnetic coupling |
| Cesium-133 clock | **WRONG** 1955 and NIST-F1 are **44 years apart** | n/a for an atomic clock | n/a | **WRONG** 1955 gives 1 s/300 years; NIST-F1 (1999) gives **1 s/20M years** | Internal conflict with the date |
| Hydrogen maser | OK 1960 (Goldenberg, Kleppner, Ramsey) | n/a | OK cavity tuning is real | **UNSOURCED** and the wrong kind of number: masers are specified by short-term stability, better than 1 part in 1e15 over hours | OK secondary standard; **portable** is questionable for a lab maser |

---

## Structural problems, not row-level

**The "Circle" column in Table B.1 mixes radii and diameters.** Flamsteed's 2.1 m is an arc radius, Bird's cell says "2.4 m radius" explicitly, and Airy's should be a 1.83 m circle diameter. Three rows list a figure in a column that does not apply to them at all: the two transit instruments and the zenith sector have no graduated circle. Split the column, or add a radius/diameter marker to every cell.

**Placeholder values were printed as data.** `Instrument maker`, `Various` (twice), `Multiple` and `Chronometer` appear in maker and escapement columns. Each marks a value that was never established. Where the maker is genuinely unknown, as with Halley's transit instrument, say **unknown** and say why.

**Accuracy figures are the weakest part of the appendix.** Fourteen of the thirty rows carry an accuracy or rate figure I could not trace to any source. They are individually plausible, which is what makes them dangerous, and several form a suspiciously smooth progression (±15, ±10, ±8, ±5, ±1, ±0.5, ±0.3 arcsec) that looks constructed rather than collected. If these cannot be sourced from Chapman's *Dividing the Circle* or Howse's *Greenwich Observatory* vol 3, the column should be dropped or recast in ranges with an explicit note that they are modern estimates.

**Two ledger rows are mis-parsed by the extraction script.** `appb-009` (Airy) and `appb-019` (Troughton) both contain an escaped ampersand from "Troughton & Simms", which shifts every subsequent column by one in the extracted text. The .tex source is fine; the extractor needs to handle `\&`. My checks were made against the .tex, not the mangled ledger text.

---

## Sources used

Royal Observatory Greenwich instrument pages, which carry the ROG's own instrument histories:

- [Flamsteed's Mural Arc (1689)](https://www.royalobservatorygreenwich.org/articles.php?article=1045)
- [Halley's 5-foot Transit Instrument (1721)](https://www.royalobservatorygreenwich.org/articles.php?article=1076)
- [Bradley's 12.5-foot Zenith Sector (1727)](https://www.royalobservatorygreenwich.org/articles.php?article=1065)
- [Bradley's 8-foot Transit Instrument (1750)](https://www.royalobservatorygreenwich.org/articles.php?article=1296)
- [Bradley's 8-foot Brass Mural Quadrant (1750)](https://www.royalobservatorygreenwich.org/articles.php?article=1054)
- [Airy's Transit Circle (1850)](https://www.royalobservatorygreenwich.org/articles.php?article=1234) and the [1908 Greenwich Observations description](https://www.royalobservatorygreenwich.org/articles.php?article=1233)
- [Photographic Zenith Tube (1955)](https://www.royalobservatorygreenwich.org/articles.php?article=1071)
- [28-inch Refractor (1893)](https://www.royalobservatorygreenwich.org/articles.php?article=1174)
- [Isaac Newton Telescope (1967/1984)](https://www.royalobservatorygreenwich.org/articles.php?article=1335)

Royal Museums Greenwich collection and story pages: [H1](https://www.rmg.co.uk/collections/objects/rmgc-object-79139), [H2](https://www.rmg.co.uk/collections/objects/rmgc-object-79140), [H3](https://www.rmg.co.uk/collections/objects/rmgc-object-79141), [H4](https://www.rmg.co.uk/collections/objects/rmgc-object-79142), [K1](https://www.rmg.co.uk/collections/objects/rmgc-object-79143), [Year-Going Clock](https://www.rmg.co.uk/collections/objects/rmgc-object-202113), [Shepherd Gate Clock](https://www.rmg.co.uk/royal-observatory/attractions/shepherd-gate-clock), [Model of Flamsteed's 7ft Mural Arc](https://www.rmg.co.uk/collections/objects/rmgc-object-10184).

Other: [History of Science Museum Oxford on the octant](https://www.hsm.ox.ac.uk/octant) and [the mural quadrant](https://www.mhs.ox.ac.uk/students/96to97/mquad.html); [NIST history of atomic clocks](https://www.nist.gov/pml/time-and-frequency-division/time-services/brief-history-atomic-clocks-nist); [Physics World on Essen's 1955 caesium clock](https://physicsworld.com/a/celebrating-louis-essen-and-the-birth-of-atomic-time/); [Goldenberg, Kleppner and Ramsey, Phys. Rev. Lett. 1960](https://link.aps.org/doi/10.1103/PhysRevLett.5.361); [Annals of Science on H4's diamond pallets](https://www.tandfonline.com/doi/abs/10.1080/00033790701619675); [Science Museum Group on the 40-foot mirror](https://collection.sciencemuseumgroup.org.uk/objects/co56770/original-mirror-for-william-herschels-forty-foot-telescope-1785) and [H5](https://collection.sciencemuseumgroup.org.uk/objects/co8448183/marine-timekeeper-known-as-h5-by-john-harrison-and-son-1770); [Datchet History on the Herschels](https://datchethistory.org.uk/datchet-people/herschels/); [Foucault's silvered-glass reflector, Vistas in Astronomy](https://www.sciencedirect.com/science/article/abs/pii/0083665687900158).

Wikipedia was used only to locate the primary sources above, except where cited directly for uncontroversial dates (Troughton & Simms partnership, 40-foot telescope, Isaac Newton Telescope, Shortt-Synchronome, bubble octant, Thomas Earnshaw, George Graham).

## Not checked

**Two figures I deliberately did not fill in.** Chapman's *Dividing the Circle* and Howse's *Greenwich Observatory* vol 3 were not reachable from here, and they are the sources that would settle the fourteen unsourced accuracy figures and the Flamsteed mural arc's objective aperture. I have left those marked unsourced rather than supplying a plausible number.
