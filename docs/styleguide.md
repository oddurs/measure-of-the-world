# Style Guide: "The Measure of the World"

This guide combines **writing and formatting principles** for a technical history that integrates narrative, mathematics, and analytical design. We use LaTeX with the `memoir` class to achieve the precision and flexibility that this project demands.

---

## Part I: Writing Philosophy and Principles

### Core Ambitions

**Intellectual rigor married to narrative power.** The mathematics is real; the history is vivid. These are not in tension. A derivation of aberration and a description of Bradley at the eyepiece belong in the same chapter, illuminating each other.

**Integration over segregation.** Text, equations, diagrams, and citations form a unified argument. Mathematics appears where it belongs in logical flow. Figures sit adjacent to their discussion. References are visible alongside claims.

**Respect for the reader.** Assume intelligence and willingness to work. Define terms precisely, then use them without apology. Trust that readers who follow one step can follow the next. Never simplify at the cost of accuracy.

**Data-ink ratio applies to prose.** Every sentence advances understanding. Eliminate throat-clearing, redundant transitions, decorative adjectives. Density over length: three precise sentences are worth more than six vague ones.

### Tuftean Design Principles

**Small multiples and layered information.** When comparing instruments, methods, or observations across time, use parallel structure. Present data at multiple resolutions: key result in text, detailed derivation in figures, raw data in annotations.

**The smallest effective difference.** When distinguishing concepts, use minimum necessary contrast. Let the reader perceive distinctions through careful exposition rather than emphatic signposting.

**Data prominence.** Diagrams, equations, and citations are primary evidence, not decoration. A well-labeled figure often replaces paragraphs of description.

### Narrative Method

**Open with human stakes.** Every chapter begins with a concrete moment—a disaster at sea, an astronomer's frustration, a midnight observation. Establish why the problem mattered before explaining how it was solved.

**Vignettes: dense and focused.** Opening vignettes should be one paragraph. Set emotional and narrative frame; later sections develop analysis. Resist expansion; vivid brevity is stronger than elaborate storytelling.

**Period texture without antiquarianism.** Evoke the 17th and 18th centuries through specific sensory detail: whale oil lamps, brass flexing under temperature change, quill on logbook. But write in modern English with period vocabulary where it illuminates.

**Let historical actors speak.** Quote primary sources when original language reveals character or thinking. A sentence from Halley's correspondence or Flamsteed's preface carries authority that paraphrase cannot.

**Treat figures as intelligent agents under constraints.** Not heroes or villains. Show their reasoning, errors, workarounds. Let personalities emerge through actions and words, not adjectives. Acknowledge historical debates.

**Section rhythm: story into science, science back into story.** Alternate between narrative and analysis. After a technical passage, return briefly to the human story: what did this result mean? What did they do next? This movement is the book's heartbeat.

---

## Part II: Mathematics as Exposition

Mathematics is **not illustration**; it is **argument**. Every derivation should build fluency in spherical trigonometry, coordinate transformations, error analysis, orbital mechanics, optical physics, and horological dynamics.

### Exposition Sequence

1. **Motivation.** State the problem in concrete terms. What did the astronomer need to compute? What precision mattered? What happened if they failed?

2. **Geometric setup.** Define the situation with a labeled diagram. Introduce notation. A clear figure often obviates paragraphs of description.

3. **Derivation.** Work through step by step. Show reasoning, not just results. Where manipulation is routine, indicate method and state result. Where insight is required, slow down.

4. **Worked example.** Apply the formula to a specific historical observation with actual numbers. Reproduce a calculation from Flamsteed's ledger, Maskelyne's almanac, or Bradley's notebooks. Let readers verify against real data.

5. **Error analysis.** Quantify uncertainty. What were dominant error sources? How did instrumental limits, atmospheric effects, or human factors bound precision?

6. **Historical resolution.** How did practitioners of the period handle this calculation? What shortcuts, tables, or approximations did they use?

**Use "we" when working through derivations.** Invite participation: "If we take the observed altitude and correct for refraction..."

### Notation Conventions

- Use modern notation for clarity; note historical notation where it illuminates period thinking
- Define all symbols at first use; maintain consistency across chapters
- Prefer SI units in exposition; provide period units (feet, lines, Paris inches) in historical context
- Distinguish carefully between degrees, radians, hours, and arc-units

### Inline vs. Display Mathematics

**Inline math** (part of a sentence):

```latex
The period is $T = 2\pi\sqrt{L/g}$, depending only on length and gravity.
```

**Display math** (equation on its own line):

```latex
\[
  T = 2\pi\sqrt{\frac{L}{g}}
\]
```

Use `\[...\]` for single, unnumbered equations. Never use `$$...$$` (deprecated).

**Multi-line equations:**

```latex
\begin{align*}
  F &= ma \\
  E &= mc^2
\end{align*}
```

Use `align*` with `&` marking alignment points (usually before `=`).

### Physical Quantities with `siunitx`

Always use `siunitx` for physical quantities:

```latex
Temperature: \SI{300}{\kelvin}
Distance: \SI{10}{\meter}
Acceleration: \SI{9.8}{\meter\per\second\squared}
Angle: $45\degree 30\arcminute 45\arcsecond$
```

The package handles spacing, formatting, and notation automatically. Never write "10 m" or "9.8 m/s²" in plain text.

---

## Part III: Text and Formatting

### Chapter and Section Structure

Each chapter follows this structure:

```latex
\chapter{Chapter Title}
\label{ch:short-slug}

\section{Opening Vignette}
\label{sec:opening}
% Brief, vivid paragraph: one human moment

\section{The Problem}
\label{sec:problem}
% Exposition and motivation

\section{Method and Theory}
\label{sec:method}
% Mathematical and analytical content

\section{Historical Resolution}
\label{sec:resolution}
% How practitioners of the period solved it
```

The document uses `memoir` class with sections numbered down to subsection level only.

### Emphasis and Typography

**Italics** (emphasis):
```latex
\emph{key concept}  % or \textit{...}
```

**Bold** (strong):
```latex
\textbf{important result}
```

**Small caps** (names, acronyms, historical titles):
```latex
\textsc{Royal Society}
\textsc{RGO}  % Royal Greenwich Observatory
```

### Quotes and Punctuation

- **Single quotes:** `` `text' ``
- **Double quotes:** `` ``text'' ``
- **En-dash** (ranges): `1676--1719` (not `1676-1719`)
- **Em-dash** (breaks): `---` (not `-` or `--`)
- **Hyphen** (compound): `well-calibrated`

### Lists

**Unordered list:**

```latex
\begin{itemize}
  \item First item
  \item Second item
\end{itemize}
```

**Ordered list:**

```latex
\begin{enumerate}
  \item First step
  \item Second step
\end{enumerate}
```

### Typography Principles

- **Non-breaking spaces:** `Prof.\ Smith` or `~100~meters` to prevent awkward breaks
- **Spell out numbers 0–9 in prose:** "nine stars" (not "9 stars")
- **Use proper quotation marks** (not straight quotes)

---

## Part IV: LaTeX Source Code Practices

### Clean LaTeX Output: Readability First

The source code is read by humans. Preserve its clarity and maintainability:

**Omit unnecessary marks and separators.** Do not use `---` or `***` or other decorative marks to separate sections. These clutter the source code and add no semantic meaning. Let section headings (`\section{}`, `\subsection{}`) convey organization. The typeset document handles visual hierarchy; the source code should be lean.

**Minimize excessive blank lines.** A single blank line between paragraphs is sufficient. Multiple carriage returns make the source harder to scan and edit. Reserve white space for logical grouping:
- One blank line between paragraphs
- One blank line before section headings
- No blank lines within equations or command sequences
- No trailing whitespace at line ends

**Bad practice:**
```latex
This is a paragraph.


This is another paragraph after excessive whitespace.

---

Another separation with decorative marks.

\section{Next Section}
```

**Good practice:**
```latex
This is a paragraph.

This is another paragraph with proper spacing.

\section{Next Section}
```

**Rationale:** The LaTeX source is itself a document. It should be scannable, editable, and maintainable. The compiled PDF handles all display concerns; the `.tex` file is for human authors and future editors. Clean source code saves hours in collaborative editing and debugging.

### Footnotes for Extended Commentary

Use footnotes to expand on topics without disrupting narrative flow. Footnotes are ideal for:
- **Technical asides:** Clarifications that are interesting but not essential to the argument
- **Historical details:** Context, anecdotes, or biographical information interesting but tangential
- **Related concepts:** References to related topics not fully developed in this chapter
- **Caveats and qualifications:** Conditions, exceptions, or nuances that would awkwardly interrupt prose if placed inline

**Example usage:**

```latex
The mural arc's precision of ten arc-seconds seems modest by modern standards,\footnote{Modern
telescopes achieve sub-arcsecond precision routinely. The achievement lies not in absolute
precision but in the systematic approach---averaging hundreds of observations and quantifying
error sources---that made Flamsteed's catalog reliable for a century.} but it represented a
tenfold improvement over Tycho Brahe's work.
```

**When to use footnotes:**
- Explanatory comments (definitions of period terminology, clarifications of historical context)
- Comparative context (how something compares to modern practice without distracting from the main narrative)
- Quantitative caveats or qualifications that merit mention but interrupt the main text
- Acknowledgment of scholarly debate or historiographical nuance

**When NOT to use footnotes:**
- Essential arguments (these belong in the main text)
- Citations (use `\citep{}` in parentheses or `\citet{}` as subject; bibliography handles citations)
- Simple definitions that fit naturally in parentheses or appositives
- Anything longer than 2-3 sentences (move to main text or appendix instead)

**Syntax:**

```latex
Flamsteed's catalog was meticulous.\footnote{So meticulous that some entries contain observations
separated by decades, all averaged together to produce a single final position.} The care he took
was essential to the work's subsequent influence.
```

Footnotes are automatically numbered and placed at the bottom of the page. The memoir class manages numbering and placement across pages.

---

## Part V: Figures and Diagrams

### Photographs and Raster Images

Place images in the appropriate subdirectory under `src/figures/`:
- JPEGs: `jpg/`
- PNGs: `png/`
- PDFs: `pdf/`

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\linewidth]{shovell-fleet-track.jpg}
  \caption{Admiral Shovell's fleet track (assumed position vs. actual).}
  \label{fig:shovell-track}
\end{figure}
```

**Sizing:**
- `width=\linewidth` — Full text width
- `width=0.8\linewidth` — 80% of text width
- `width=5cm` — Exact size
- `height=3in` — Exact height (use sparingly; distorts aspect ratio)

**Placement options `[htbp]`:**
- `h` — Here (roughly where placed)
- `t` — Top of page
- `b` — Bottom of page
- `p` — On a page by itself
- `!` — Ignore size restrictions (use rarely)

**Quality standards:**
- JPEGs: 300 DPI at final print size (minimum)
- PNGs: Lossless; use for line art and diagrams
- PDFs: Vector format; use for exported plots and technical diagrams

### Vector Diagrams with TikZ

For diagrams you create, use TikZ:

```latex
\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}
    \draw (0,0) -- (3,0) -- (3,2) -- (0,0);
    \draw (3,0) rectangle +(0.3,0.3);  % Right angle mark
    \node at (1.5,-0.4) {$b$};
    \node at (3.5,1) {$a$};
  \end{tikzpicture}
  \caption{Right triangle with sides $a$, $b$, $c$.}
  \label{fig:right-triangle}
\end{figure}
```

**When to use TikZ:**
- Geometric diagrams
- Graphs and networks
- Annotated schematics
- Anything that scales without pixelation

**When not to use TikZ:**
- Photographs (use JPEGs)
- Complex images with textures (use PNG)
- Plots generated by external software (export as PDF)

### Scientific Plots with pgfplots

For data visualization:

```latex
\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}
    \begin{axis}[
      xlabel={Time (years)},
      ylabel={Longitude Error (arcminutes)},
      legend pos=north east
    ]
    \addplot table {
      year error
      1700 120
      1750 90
      1800 45
      1850 10
      1900 2
    };
    \legend{Cumulative Error}
    \end{axis}
  \end{tikzpicture}
  \caption{Historical reduction in longitude measurement error.}
  \label{fig:longitude-error-trend}
\end{figure}
```

Or load data from a CSV file:

```latex
\addplot table [x=year, y=error] {data.csv};
```

---

## Part VI: Tables

### Philosophy: Minimal, Professional Design

Use `booktabs` for professionally typeset tables. **Key principle: horizontal lines only, no vertical lines.**

### Basic Table

```latex
\begin{table}[htbp]
  \centering
  \caption{Longitude-related maritime disasters, 1550–1714.}
  \label{tab:disasters}
  \begin{tabular}{lrr}
    \toprule
    Ship & Year & Lives Lost \\
    \midrule
    São Thomé & 1591 & Unknown \\
    Eendracht & 1615 & Unknown \\
    Tryall & 1656 & $>50$ \\
    \bottomrule
  \end{tabular}
\end{table}
```

**Column specifiers:**
- `l` — Left-aligned
- `c` — Centered
- `r` — Right-aligned
- `p{3cm}` — Fixed-width paragraph (wraps text)

**Booktabs rules:**
- `\toprule` — Top border
- `\midrule` — Middle border (after headers)
- `\cmidrule{2-3}` — Partial rule from column 2 to 3
- `\bottomrule` — Bottom border

**No vertical lines.** Ever. Use padding and whitespace instead.

### Long Tables (multi-page)

For tables spanning pages:

```latex
\begin{longtable}{lrr}
  \caption{A long table spanning multiple pages.} \\
  \toprule
  Column A & Column B & Column C \\
  \midrule
  \endfirsthead
  
  \multicolumn{3}{c}{\textit{(continued)}} \\
  \toprule
  Column A & Column B & Column C \\
  \midrule
  \endhead
  
  \bottomrule
  \endfoot
  
  Row 1 & 100 & Value \\
  Row 2 & 200 & Value \\
\end{longtable}
```

---

## Part VII: Bibliography and Citations

### Setup

The project uses `biblatex` with `biber` backend and `authoryear` citation style:

```latex
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{bibliography/references.bib}
```

### Adding Bibliography Entries

Edit `src/bibliography/references.bib` in BibTeX format:

```bibtex
@book{flamsteed1725,
  author = {Flamsteed, John},
  year = {1725},
  title = {Historia Coelestis Britannica},
  publisher = {Royal Society},
  address = {London}
}

@article{bradley1729,
  author = {Bradley, James},
  year = {1729},
  title = {A New Apparent Motion Discovered in the Fixed Stars},
  journal = {Philosophical Transactions of the Royal Society},
  volume = {35},
  pages = {637--661}
}
```

**Standard entry types:**
- `@book` — Published book
- `@article` — Journal article
- `@inproceedings` — Conference paper
- `@misc` — Websites, unpublished documents

### Citing in Text

**Author as subject:**

```latex
\citet{flamsteed1725} showed that...
```

Output: "Flamsteed (1725) showed that..."

**Parenthetical citation:**

```latex
As demonstrated in \citep{flamsteed1725}...
```

Output: "As demonstrated in (Flamsteed 1725)..."

**With page number:**

```latex
\citep[p.~42]{flamsteed1725}
```

Output: "(Flamsteed 1725, p. 42)"

**Multiple citations:**

```latex
\citep{flamsteed1725, bradley1729}
```

**Golden rule:** Use `\citet` for author as subject; use `\citep` for parenthetical citations.

### Citation Density and Authority

**Cite densely and plentifully.** Every factual claim, quoted passage, and numerical value drawn from observation must carry a citation. Multiple citations per page is normal and expected. The reader should be able to trace any assertion to primary or authoritative secondary sources.

**Primary sources preferred.** Cite Flamsteed's *Historia*, Maskelyne's logs, Harrison's memorials, the *Nautical Almanac*, *Philosophical Transactions*, Royal Society archives, Board of Longitude records.

**Engage historiography.** Where scholars disagree, cite competing interpretations. History is argued, not merely reported.

---

## Part VIII: Glossaries and Acronyms

### Defining Terms

In `src/glossary/terms.tex`:

```latex
\newglossaryentry{longitude}{
  name=longitude,
  description={Angular distance east or west of the Prime Meridian, measured in degrees}
}

\newglossaryentry{meridian}{
  name=meridian,
  description={An imaginary great circle on Earth's surface passing through both geographic poles}
}
```

### Defining Acronyms

In `src/glossary/acronyms.tex`:

```latex
\newacronym{rgo}{RGO}{Royal Greenwich Observatory}
\newacronym{utc}{UTC}{Coordinated Universal Time}
```

### Using in Text

**First use:**

```latex
The \gls{rgo} was founded in 1675.
```

Output: "The Royal Greenwich Observatory (RGO) was founded in 1675."

**Subsequent uses (same section):**

```latex
The \gls{rgo} quickly became renowned.
```

Output: "The RGO quickly became renowned."

**Force short or long form:**

```latex
\glsshort{rgo}  % Output: RGO
\glslong{rgo}   % Output: Royal Greenwich Observatory
```

---

## Part IX: Cross-References and Links

### Creating Labels

Place labels immediately after chapter/section/figure commands:

```latex
\chapter{The Deadly Ignorance of Position}
\label{ch:deadly-ignorance}

\section{The Scilly Disaster}
\label{sec:scilly-disaster}

\begin{figure}[htbp]
  ...
  \label{fig:shovell-track}
\end{figure}
```

**Naming convention:**
- Chapters: `ch:short-slug`
- Sections: `sec:short-slug`
- Figures: `fig:short-slug`
- Tables: `tab:short-slug`
- Equations: `eq:short-slug`

### Cross-Referencing with `cleveref`

**Never use** `\ref{...}` directly. Always use `\cref{...}`:

```latex
\cref{ch:deadly-ignorance} describes the problem.
```

Output: "Chapter 1 describes the problem."

```latex
See \cref{fig:shovell-track} for the fleet position.
```

Output: "See Figure 1.2 for the fleet position."

```latex
\cref{tab:disasters, fig:shovell-track} show the impact.
```

Output: "Figures 1.1 and 1.2 show the impact."

`cleveref` automatically generates the right label type and number, handles pluralization and formatting.

---

## Part X: Epigraphs

For chapter-opening quotes:

```latex
\chapter{The Deadly Ignorance of Position}

\epigraph{%
  A ship is lost for want of a nail.\\
  A nail is lost for want of a horseshoe.
}{--- \textit{Traditional saying}}

\section{Opening Vignette}
```

Use `\\` for line breaks. Put attribution in `\textit{...}` and precede with `---` (em-dash).

Epigraphs are optional but encouraged for chapter openings. They set tone and context.

---

## Part XI: Instruments and Technical Description

### Describing Instruments

**Describe as if the reader might build or operate one.** Explain not just what it does but why it was designed that way—the constraints it solved, compromises it accepted.

**Connect to observations.** Every instrument discussion should culminate in a specific measurement it enabled. What did Flamsteed see through the mural arc? What could Airy's transit circle resolve?

**Note failures and limitations.** Workarounds observers devised are as instructive as designs. Error sources, calibration procedures, and maintenance routines are part of the story.

**Instrument specifications.** Where relevant, provide quantitative parameters: aperture, focal length, graduation intervals, rated accuracy, temperature coefficients. These details anchor the narrative in physical reality.

### Error Analysis and Uncertainty

Quantify uncertainty throughout. What were dominant error sources? How did instrumental limits, atmospheric effects, or human factors bound achievable precision? Make uncertainty visible and mathematical.

---

## Part XII: LaTeX Package Reference

### The Nine Core Packages

#### memoir

The **document class** that structures everything. Designed for book publishing with full control over layout, chapter styling, and frontmatter management.

**Key features:**
- `\chapter{}` for chapter-level sections
- `\frontmatter`, `\mainmatter`, `\backmatter` for logical divisions
- `\setsecnumdepth{subsection}` for numbering control
- Built-in support for footnotes, page styles, and margin notes

**Typography control:**
```latex
\setsecheadstyle{\Large\bfseries}
\setsubsecheadstyle{\large\bfseries}
\pagestyle{headings}  % Page headers with chapter/section info
```

#### geometry + microtype

**geometry** sets page dimensions and margins. **microtype** enables professional typography through character protrusion, font expansion, and kerning.

```latex
\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{microtype}  % Automatic protrusion and expansion
```

Microtype lets LaTeX squeeze text imperceptibly to avoid widows, orphans, and bad line breaks.

#### amsmath, amssymb, mathtools

Mathematical typesetting. **amsmath** provides environments like `align*`, `gather*`, and refined `\frac{}`. **amssymb** adds math symbols. **mathtools** extends with matrix environments and extensible arrows.

```latex
\begin{align*}
  E &= mc^2 \\
  p &= mv
\end{align*}
```

#### siunitx

Physical quantities with correct spacing and notation:

```latex
\SI{10}{\meter}
\SI{9.8}{\meter\per\second\squared}
\SI{300}{\kelvin}
45\degree 30\arcminute 15\arcsecond
```

#### graphicx

Image inclusion:

```latex
\includegraphics[width=0.8\linewidth]{filename.jpg}
```

#### tikz + pgfplots

**TikZ** for vector graphics. **pgfplots** builds scientific plots on top of TikZ.

```latex
\begin{tikzpicture}
  \draw (0,0) -- (3,0) -- (3,2) -- (0,0);
\end{tikzpicture}
```

#### biblatex + biber

Bibliography management with full control over formatting.

```latex
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{references.bib}
```

Use `biber` (not `bibtex`) as the backend for reliability and Unicode support.

#### hyperref + cleveref

**hyperref** makes all cross-references clickable. **cleveref** auto-generates correct reference text:

```latex
\cref{fig:example}  % Outputs "Figure 1.2"
```

#### booktabs + longtable

Professional table typography (no vertical lines) and multi-page tables.

```latex
\toprule, \midrule, \bottomrule
```

#### glossaries

Glossary and acronym management with automatic indexing and sorting.

```latex
\newacronym{rgo}{RGO}{Royal Greenwich Observatory}
\gls{rgo}  % First use expands; later uses show abbreviation
```

#### epigraph

Chapter-opening quotations with proper attribution.

```latex
\epigraph{Quote text}{---Attributed Person}
```

---

## Part XIII: Common Pitfalls and Solutions

### Problem: "Undefined reference to ..."

**Cause:** You used `\ref{}` but the label doesn't exist or is spelled differently.

**Solution:**
1. Check spelling of `\label{...}` and `\ref{...}` match exactly
2. Ensure label is immediately after sectioning/figure command
3. Rebuild: `make distclean && make build`

### Problem: "Citation foo undefined"

**Cause:** You used `\cite{foo}` but `foo` doesn't exist in `references.bib`.

**Solution:**
1. Check spelling in `\citep{foo}` matches BibTeX key exactly
2. Ensure `.bib` file has valid BibTeX syntax
3. Run `make build` again

### Problem: Glossary appears empty

**Cause:** No glossary entries defined or entries not used in text.

**Solution:**
1. Add `\newglossaryentry{...}` or `\newacronym{...}` entries
2. Use `\gls{...}` in document to reference entries
3. Rebuild: `make clean && make build`

### Problem: Table overflows page width

**Cause:** Table is too wide for margins.

**Solution:**
1. Use `p{...}` columns with fixed widths and text wrapping
2. Reduce font size locally: `{\small \begin{tabular}...\end{tabular}}`
3. Rotate the table with `rotating` package
4. Break into multiple smaller tables

### Problem: Figure appears in wrong place

**Cause:** LaTeX's float placement algorithm moved it.

**Solution:**
1. Use `[htbp!]` to give LaTeX more flexibility
2. Ensure at least 30% of page is text
3. Add `\FloatBarrier` from `placeins` package to force floats out
4. Use `[H]` from `float` package for absolute positioning (sparingly)

### Problem: Equation numbers overflow margin

**Cause:** Very long equations with numbers on right.

**Solution:**
1. Use `align*` for unnumbered equations
2. Break long equations: `\begin{align} ... \\ ... \end{align}`
3. Use `\tag{...}` for custom numbering

---

## Part XIV: Mathematical Writing Conventions

**Always define notation.** "Let $T$ be the period (in seconds) of the pendulum."

**Use displaystyle for emphasis.** Important equations should be on their own line.

**Capitalize after equations.** `..., which gives $x = 5$. The solution is unique.` (capital after period)

**Distinguish operator types:**

```latex
\sin, \cos, \tan, \log, \exp, \ln, \max, \min, \det, \gcd
```

Not `sin`, `cos`, etc. in math mode.

**Fractions in text:** Use `$\tfrac{a}{b}$` (text-style) for inline fractions to improve readability.

---

## Part XV: Build System and Workflow

### What Happens When You Run `make build`

```
make build
  ├─ Create build/out directory
  ├─ Run pdflatex (1st pass)  → .aux, .glo, .bcf files
  ├─ Run biber on .bcf        → .bbl (processed bibliography)
  ├─ Run makeglossaries       → .gls (processed glossary)
  ├─ Run pdflatex (2nd pass)  → include bibliography and glossary
  ├─ Run pdflatex (3rd pass)  → resolve final references
  ├─ Copy final PDF to build/out/
  └─ Validation checks
     ✓ No undefined references?
     ✓ No undefined citations?
```

All intermediate files go to `build/tmp/`. The final PDF is `build/out/measure-of-the-world.pdf`.

### Other Make Targets

- `make watch` — Continuous compilation with PDF refresh
- `make clean` — Remove intermediates, keep PDF
- `make distclean` — Full cleanup of all artifacts

---

## Part XVI: Accessibility and Best Practices

**Use descriptive labels:** `\label{fig:harrison-chronometer}` (not `fig:1`)

**Use meaningful link text:** `\cref{fig:harrison}` (not "see here")

**Provide captions:** Every figure and table must have a caption

**Mix citation styles:** `Smith (2020) showed that... \citep{smith2020}.` (both author-subject and parenthetical)

**Consistent abbreviations:** All `.bib` entries should have author, year, and title

---

## Part XVII: File Organization and Workflow

- Each chapter in its own file: `src/chapters/01.tex`, `src/chapters/02.tex`, etc.
- Figures organized by format: `src/figures/jpg/`, `src/figures/png/`, `src/figures/pdf/`
- Bibliography centralized: `src/bibliography/references.bib`
- Glossary split: `src/glossary/terms.tex`, `src/glossary/acronyms.tex`

### Version Control

Commit frequently:
- After completing a chapter section
- After adding bibliography entries
- After adding figures

Use meaningful commit messages:
```
Add Chapter 3: Founding the Observatory

- Introduce John Flamsteed and Jonas Moore
- Describe Wren's Flamsteed House design
- Add funding constraints section
```

---

## Part XVIII: When to Break These Rules

If a situation produces worse output while following these guidelines, **document the exception**:

```latex
% EXCEPTION: Using tabularx because booktabs can't handle wrapped columns
\usepackage{tabularx}
\begin{tabularx}{0.9\linewidth}{Xl}
  ...
\end{tabularx}
```

Leave a comment. Future authors will thank you.

---

## Questions and Further Resources

- **`memoir` documentation:** `texdoc memoir`
- **`biblatex` manual:** `texdoc biblatex`
- **`siunitx` guide:** `texdoc siunitx`
- **Technical build details:** See [BUILD.md](BUILD.md)
- **Project planning and history:** See [docs/plan/](docs/plan/)
