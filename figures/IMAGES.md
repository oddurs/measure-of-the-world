# Images: licensing rules and sourcing guide

*The Measure of the World* is licensed **CC BY 4.0**, which lets anyone redistribute
and adapt the book **commercially**. That single fact governs every image decision
in this project.

---

## 1. The licence rule

An image may go in the book only if its own licence permits commercial reuse and
adaptation. In practice that means one of:

| Licence | Usable? | Obligation |
|---|---|---|
| Public domain / PD-Art / Public Domain Mark 1.0 | Yes | None legally; credit anyway |
| CC0 | Yes | None legally; credit anyway |
| CC BY (2.0 / 4.0) | Yes | Print the credit line |
| CC BY-SA (2.0 / 3.0 / 4.0) | Yes | Print the credit line, and see the ShareAlike note below |
| CC BY-**NC** anything | **No** | Needs a separate paid licence |
| CC BY-**ND** anything | **No** | Needs a separate paid licence |
| "Non-commercial research only", "all rights reserved" | **No** | Needs a separate paid licence |

**Attribution is not optional on CC BY and CC BY-SA.** If the credit line is not
printed, the licence terminates and the use becomes infringement. Every such image
in `manifest.yaml` carries a `credit_line` written exactly as it must appear.

**The ShareAlike note.** CC BY-SA obliges you to license *adaptations* of the image
alike. Reproducing a photograph unmodified inside a book is a collection, not an
adaptation, so the book stays CC BY 4.0 and only the image carries its own licence.
Cropping, recolouring or compositing a CC BY-SA image into a new figure *does*
create an adaptation, and that derivative would have to be CC BY-SA. So reproduce
CC BY-SA photographs as-is, and prefer CC0 or CC BY files whenever a figure needs
editing.

### Two rules about what carries copyright

1. **Flat 2D reproductions of public-domain works.** A faithful photograph of a
   pre-1900 painting, engraving or printed page adds no new copyright in the US
   (*Bridgeman Art Library v. Corel*, 1999), and Wikimedia Commons operates on that
   basis via the `PD-Art` tag. The UK position differs: some institutions assert
   "sweat of the brow" rights over their reproductions. Where a Commons file carries
   the third-party-claim notice, the manifest says so.
2. **Photographs of 3D objects.** A modern photograph of a clock, a telescope or a
   building gets its **own** copyright, however old the object is. An 18th-century
   chronometer photographed in 2015 needs a freely licensed *photograph*. This is
   why several instrument entries depend on a Wikimedia photographer's CC BY-SA
   grant rather than on the age of the object.

---

## 2. Which archives are safe, and which are not

### Safe

| Source | Why |
|---|---|
| **Wikimedia Commons** | Every file states its licence. Check each one; the site mixes PD, CC0, CC BY and CC BY-SA. |
| **Wellcome Collection** | Most historical prints are CC BY 4.0 or PD, at 2000-3400 px. The single best source for pre-1900 portrait engravings. |
| **Library of Congress** | "No known copyright restrictions" on large collections, including Bain News Service. Masters are far larger than the Commons derivatives. |
| **Internet Archive / Google Books** | Pre-1900 book scans. Check the item's `rights` field; many are Public Domain Mark 1.0, some carry nothing at all. |
| **Biodiversity Heritage Library** | Runs of *Philosophical Transactions* with an explicit "no longer under copyright protection" statement. |
| **Rijksmuseum** | CC0, often at very high resolution. |
| **Metropolitan Museum of Art** | Open Access items are CC0. |
| **NASA / NIST / US federal agencies** | Public domain under 17 U.S.C. 105. No attribution obligation. |
| **Geograph Britain and Ireland** | CC BY-SA 2.0 throughout. Reliable, and often surprisingly large. |

### Not usable

| Source | Terms | Consequence |
|---|---|---|
| **Royal Museums Greenwich** (rmg.co.uk) | CC BY-NC-ND | Excluded. Painful, because RMG holds most of the objects this book is about. |
| **Science Museum Group** | CC BY-NC-SA | Excluded. |
| **Cambridge Digital Library** | CC BY-NC 3.0 at item level; site terms forbid commercial use without a licence | Excluded. This blocks the **Board of Longitude papers (RGO 14)** entirely. |
| **Bibliothèque nationale de France / Gallica** | Paid licence required for commercial reuse | Excluded. |
| **British Museum** | CC BY-NC-SA | Excluded. |
| **Getty, Alamy, Bridgeman** | Rights-managed | Excluded unless you buy a licence. |
| **National Portrait Gallery, London** | Asserts sweat-of-brow over its reproductions | Use with care; see below. |

### The RMG and NPG distinction, which matters a lot here

Several of the best files in the manifest depict objects **held by** Royal Museums
Greenwich or the National Portrait Gallery. That is not the same as being licensed
by them. Where a pre-1900 painting has been uploaded to Commons under `PD-Art`, the
*file* is public domain regardless of the holding institution's website terms, and
those terms do not attach to it.

The exception is the NPG. Files from the 2009 bulk upload of NPG images sit in
Commons' `Category:Items with copyright claims` and carry an explicit notice that a
third party asserts copyright over the reproduction. That claim is unsound in the US
and contested in the UK. Where a claim-free alternative of equal or better quality
exists, take it. `ch01-admiral-shovell` is exactly this case, and the manifest names
the replacement.

---

## 3. The manifest schema

`manifest.yaml` holds one top-level block per image, keyed by a stable id of the
form `chNN-slug` or `appX-slug`.

```yaml
ch02-john-flamsteed:
  file: src/figures/photos/ch02-john-flamsteed.jpg
  status: present        # present | wanted | rejected
  risk: SAFE             # SAFE | NEEDS-SOURCING | REPLACE  (omit for wanted/rejected)
  subject: "John Flamsteed, first Astronomer Royal"
  creator: "Thomas Gibson"          # artist or photographer, "" if unknown
  date: "1712"
  source_url: "https://commons.wikimedia.org/wiki/File:..."   # "" if unverified
  license: "public domain (PD-Art, artist died 1751)"
  credit_line: "John Flamsteed by Thomas Gibson, 1712. The Royal Society, London (RS.9346). Public domain."
  pixels: "816x1024"
  notes: "..."
```

**Field meanings**

- `status` — `present`: the file is in the repo. `wanted`: the book should have it
  but it has not been fetched. `rejected`: researched and deliberately excluded.
- `risk` — a judgement about *copyright*, not about picture quality. `SAFE`: public
  domain or a clean permissive licence, provenance pinned. `NEEDS-SOURCING`: usable,
  but something must be done before print, such as printing a mandatory credit or
  resolving a contested reproduction claim. `REPLACE`: likely not usable commercially.
  Production problems like low resolution or a wrong caption go in `notes`, not here.
- `source_url` — the page whose licence was actually read, not a search result.
  Empty means no compatible source could be verified. Never guess a URL.
- `credit_line` — the exact string to typeset. For public-domain works it is still
  filled in, because a reader deserves the provenance even when the law does not
  demand it.
- `pixels` — native dimensions at the source. Divide by 300 for printable inches.
- `recommended_replacement` — optional. Names another manifest id that is a better
  file for the same subject.

Two `wanted` entries carry an empty `source_url` on purpose:
`ch12-bradley-zenith-sector` and `appc-spencer-jones`. Nothing commercially reusable
exists for either. Their notes record what was searched and what the paid options are.

---

## 4. How to add an image

1. **Find it** on one of the safe archives above. Search Wikimedia Commons first.
2. **Open the file page and read the licence.** Not the search result, not the
   thumbnail, not a blog that reused it. The actual file page.
3. **Reject it** if the licence contains `NC` or `ND`, or if the page carries a
   third-party copyright claim you cannot live with.
4. **Check the pixels.** Divide the smaller dimension by 300 to get printable inches.
   A full-page plate needs roughly 1800 x 2700 px. Several otherwise fine images in
   this project fail on this and nothing else.
5. **Add the manifest block** before downloading, with `status: wanted`, the verified
   `source_url`, the exact licence string from the page, and the credit line.
6. **Download** into `src/figures/photos/` using the manifest id as the filename, and
   flip `status` to `present` with a `risk` rating.
7. **Reference it** from the chapter with `\includegraphics{photos/<id>}`, and make
   sure the caption matches what the source page actually says about the object.
8. **Print the credit.** Anything under CC BY or CC BY-SA must carry its credit line
   in the figure caption or in a picture-credits page. Public-domain items should
   carry it too.

To verify a file you already have, hash it against Commons:

```sh
h=$(shasum -a 1 path/to/file.jpg | cut -d' ' -f1)
curl -s "https://commons.wikimedia.org/w/api.php?action=query&list=allimages&aisha1=$h&format=json"
```

An exact hash match pins the provenance beyond argument. That is how all six existing
photographs in this repo were identified.

---

## 5. Audit of the six existing photographs

All six were matched to a Wikimedia Commons file by exact SHA-1 hash, so the
provenance below is certain rather than inferred.

| File | Actual source | Licence | Risk | One-line verdict |
|---|---|---|---|---|
| `ch01-admiral-shovell.jpg` | [Sir Clowdisley Shovell by Michael Dahl.jpg](https://commons.wikimedia.org/wiki/File:Sir_Clowdisley_Shovell_by_Michael_Dahl.jpg), NPG 797 | Public domain (PD-Art) | **NEEDS-SOURCING** | Underlying painting is PD, but the file is from the 2009 NPG bulk upload and carries an active sweat-of-brow claim; the caption also credits Dahl himself when NPG catalogues it as *studio of* Dahl. |
| `ch02-john-flamsteed.jpg` | [John Flamsteed (Gemälde).jpg](https://commons.wikimedia.org/wiki/File:John_Flamsteed_(Gem%C3%A4lde).jpg), Royal Society RS.9346 | Public domain (PD-Art) | **SAFE** | Clean copyright, provenance confirmed by the embedded "The Royal Society" IPTC credit; but the caption says "after Thomas Gibson" when this *is* the Gibson original, and 816x1024 is too small to print. |
| `ch02-flamsteed-house.jpg` | [Flamsteed House ... colonnade ... 01.jpg](https://commons.wikimedia.org/wiki/File:Flamsteed_House_Royal_Observatory_from_National_Maritime_Museum_colonnade_Greenwich_London_England_01.jpg) by Acabashi | CC BY-SA 4.0 | **NEEDS-SOURCING** | Commercially fine, but attribution is mandatory and no credit currently appears anywhere in the repo. |
| `ch02-tompion-clock.jpg` | [Royal Observatory, Greenwich 2010 PD 09.JPG](https://commons.wikimedia.org/wiki/File:Royal_Observatory,_Greenwich_2010_PD_09.JPG) by Bin im Garten | CC BY-SA 3.0 | **NEEDS-SOURCING** | It is a personal photograph, but freely licensed, so usable with credit; the real problem is that the object is almost certainly not a 1676 Tompion year-going clock. |
| `ch03-tycho-quadrant.jpg` | [Mauerquadrant.jpg](https://commons.wikimedia.org/wiki/File:Mauerquadrant.jpg) | Public domain | **SAFE** | A flat reproduction of a 1598 engraving, no new copyright, best resolution available anywhere; caption is right except that this impression is hand-coloured. |
| `ch03-uraniborg.jpg` | [Uraniborgskiss 45.jpg](https://commons.wikimedia.org/wiki/File:Uraniborgskiss_45.jpg) | Public domain | **SAFE** | Copyright clean, but the caption misattributes it: this is Blaeu's *Atlas Maior* plate of c. 1662-65, not the 1598 book, and it shows the gardens rather than the observatory. |

### Caption corrections required

Four captions state something the sources contradict.

1. **`src/chapters/01.tex:11`** — "portrait by Michael Dahl, c. 1702". The file is
   NPG 797, catalogued as **studio of** Michael Dahl. Either reword, or switch to
   [RMG BHC3026](https://commons.wikimedia.org/wiki/File:Admiral_Sir_Cloudesley_Shovell,_1650-1707_RMG_BHC3026.tiff),
   which is the autograph 1702 Dahl at 4454x7200 with no copyright claim attached.
2. **`src/chapters/02.tex:9`** — "Portrait after Thomas Gibson, c. 1712". This is the
   Gibson **original**, Royal Society RS.9346, so it should read "by Thomas Gibson,
   1712". "After" denotes a later copy by another hand. (The Royal Society's *other*
   Flamsteed, RS.9345 of c. 1680, is the one with a tangled attribution history:
   Gibson? then School of Lely, now Thomas Murray. That confusion is probably the
   source of the error.)
3. **`src/chapters/02.tex:48`** — "One of Thomas Tompion's year-going clocks ... The
   13-foot pendulum". The photograph shows a floor-standing longcase clock in a
   panelled corner. Tompion's two 1676 year-going clocks were **wall-mounted**, dials
   set high above the wainscot with the pendulums hanging behind the panelling. The
   Commons description identifies only the room, not the clock, and the same category
   holds a 1737 replacement case and a 1972 replica dial. Verify the object before
   printing this claim.
4. **`src/chapters/03.tex:21`** — "from *Astronomiae Instauratae Mechanica* (1598)".
   It is Willem Blaeu's hand-coloured engraving in Joan Blaeu's *Atlas Maior*,
   c. 1662-65, after Tycho's 1598 woodcut. The caption also describes observation
   platforms and instruments, but the plate is a bird's-eye plan of the rampart and
   formal gardens with the house small at the centre.

One adjacent problem, outside the captions: the footnote at **`src/chapters/02.tex:43`**
says Tompion's 1676 mechanism "incorporated Harrison's grasshopper escapement
principles, though Harrison's work came later". That is self-contradictory and
anachronistic. Harrison was born in 1693.

---

## 6. Known gaps

Two subjects have no commercially reusable image anywhere, and the manifest records
them with an empty `source_url` rather than a guess.

- **Bradley's zenith sector.** Only Royal Museums Greenwich holds good photographs,
  under CC BY-NC-ND. `ch12-bradley-mural-quadrant` is the substitute.
- **Sir Harold Spencer Jones.** Nothing on Commons, Wellcome or the Library of
  Congress. He died in 1960, so UK photographic copyright is probably still live.

Three further subjects were researched and could not be sourced cleanly, and are
recorded in the notes of the nearest manifest entry rather than as their own blocks:
the **Francis Place / Thacker engraving of the Octagon Room** of c. 1676 (not on
Commons; Royal Society copy marked "© The Royal Society"; RMG copy CC BY-NC-ND;
British Museum CC BY-NC-SA), a **pre-1900 figure-eight analemma diagram**, and a
**19th-century engraving of the Greenwich time ball or noon gun**.

One subject was rejected on factual rather than licensing grounds. **John Pond**, the
sixth Astronomer Royal, has no authentic portrait at all; the engraving that
circulates as him depicts a Newmarket livery-stable keeper of the same name.

Finally, three files are licence-clean but too small to print at the size they are
wanted: the 1919 eclipse plate (700x899, and that is the global ceiling), the Christie
portrait (357x515, re-scannable from the Internet Archive copy of Maunder 1900), and
the Dyson portrait (398x546 on Commons, but the Library of Congress master is far
larger).

---

## 7. Further verified candidates, not in the manifest

These were researched and their licences read, but cut to keep the plate programme to
sixty. Add a manifest block if any is wanted.

| Subject | Licence | Pixels | Source |
|---|---|---|---|
| The Western Rocks, Isles of Scilly | CC BY-SA 2.0 | 4320x3240 | [Commons](https://commons.wikimedia.org/wiki/File:Isles_of_Scilly,_The_Western_Rocks_from_Gorregan_-_geograph.org.uk_-_7865009.jpg) |
| Shovell's monument, Westminster Abbey | CC BY-SA 4.0 | 5184x3456 | [Commons](https://commons.wikimedia.org/wiki/File:Monument_to_Admiral_Cloudesley_Shovell,_Westminster_Abbey_01.jpg) |
| Stjerneborg, Tycho's underground observatory, 1598 | Public domain | 2643x3609 | [Commons](https://commons.wikimedia.org/wiki/File:Brahe_Stellaeburgi_Orthographia_1598.jpg) |
| The Observatoire de Paris, 1726 engraving | CC0 | 5572x4158 | [Rijksmuseum via Commons](https://commons.wikimedia.org/wiki/File:Gezicht_op_de_Observatoire_te_Parijs,_1726_L%27Observatoire_(titel_op_object)_Les_Forces_de_l%27Europe,_Asie,_Afrique_et_Amerique_Comme_aussi_les_Cartes_des_C%C3%B4tes_de_France_et_d%27Espagne_(serietitel_op_o,_RP-P-OB-83.035-44.jpg) |
| Newton's *Principia* title page, 1687 | Public domain | 2536x2988 | [Commons](https://commons.wikimedia.org/wiki/File:Newton_-_Principia_(1687),_title,_p._5,_color.jpg) |
| Longcase clock by George Graham, c. 1720 | CC0 | 1460x1844 | [Met via Commons](https://commons.wikimedia.org/wiki/File:Longcase_clock_MET_203958.jpg) |
| *Tables Requisite* title page, 1766 | Public Domain Mark 1.0 | — | [Internet Archive](https://archive.org/details/bub_gb_opIlKRuaLrwC/page/n0/mode/1up) |
| *Connaissance des Temps* for 1780 | Public Domain Mark 1.0 | — | [Internet Archive](https://archive.org/details/bub_gb_4-lEAAAAcAAJ) |
| Halley's Comet in the Bayeux Tapestry | CC0 | 2482x2583 | [Commons](https://commons.wikimedia.org/wiki/File:Bayeux_Tapestry_scene32_Halley_comet.jpg) |
| Halley's 1716 transit-of-Venus paper | Public domain (BHL) | — | [Internet Archive](https://archive.org/details/philosophicaltra2917roya) |
| The Airy Transit Circle today | CC BY 2.0 | 976x1632 | [Commons](https://commons.wikimedia.org/wiki/File:Airys_Transit_Circle.jpg) |
| 1884 Conference proceedings page | Public domain | 1760x3050 | [Commons](https://commons.wikimedia.org/wiki/File:International_Meridian_Conference_001.png) |
| Davis quadrant (backstaff), c. 1700-1725 | CC0 | 4320x3240 | [Commons](https://commons.wikimedia.org/wiki/File:Davis_quadrant_(backstaff),_England,_c._1700-1725,_brass_and_boxwood_-_Royal_Ontario_Museum_-_DSC00264.JPG) |
| Isaac Newton Telescope at Herstmonceux, 1968 | CC BY-SA 2.0 | 5144x3495 | [Commons](https://commons.wikimedia.org/wiki/File:The_Isaac_Newton_Telescope_at_Herstmonceux_-_geograph.org.uk_-_7737687.jpg) |
