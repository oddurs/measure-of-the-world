# The Measure of the World
> Oddur Sigurdsson _et al._

## 📖 About This Book

**The Measure of the World** is a comprehensive technical history of the Royal Observatory, Greenwich, spanning nearly 350 years (1675–present). This book tells the story of how astronomy transformed from an ancient discipline into a modern scientific enterprise—through the lens of precision measurement, mechanical ingenuity, and international cooperation.

From John Flamsteed's founding observations to contemporary satellite astrometry, this work traces how astronomers solved the fundamental problems of:
- **Measuring the heavens**: Determining stellar positions with ever-improving accuracy
- **Measuring time**: Transforming local solar time into coordinated global standards
- **Measuring distance**: From parallax to light-years to the cosmic distance ladder
- **Measuring Earth itself**: Charting longitude, latitude, and the planet's dynamic orientation

The narrative integrates rigorous mathematics, detailed instrument analysis, biographical context, and institutional history—revealing precision not as abstract certainty, but as a practical achievement built through decades of careful observation, technological innovation, and dedicated institutional commitment.

## 📥 Download

**[Download the PDF](https://github.com/oddurs/measure-of-the-world/releases/latest/download/measure-of-the-world.pdf)** 
*(Full edition with all appendices and bibliography)*

---

## 📚 Contents Overview

### Chapters 1–25: Main Narrative

The book progresses through five thematic movements:

**Part I: Foundations (Chapters 1–6)**
- The 1707 Scilly disaster and the cost of not knowing longitude
- Founding the Royal Observatory (1675); Flamsteed's instruments and methods
- The mural arc, the transit method, and the *Historia Coelestis Britannica*
- Why pendulum clocks could not solve longitude at sea

**Part II: Discovery (Chapters 7–13)**
- The Longitude Act and its incentives
- The lunar distance method; Harrison's chronometers H1–H5
- Maskelyne's *Nautical Almanac* and computing by distributed labor
- Halley, Bradley and the aberration of starlight, and the Airy transit circle

**Part III: Precision (Chapters 14–19)**
- The Great Equatorial and spectroscopy
- Mean time and the equation of time; the distribution of time by ball, telegraph, and radio
- The 1884 Meridian Conference; GMT, UT, and UTC
- The quadrant and sextant: angle measurement at sea

**Part IV: Transformation (Chapters 20–23)**
- Telescope optics and mountings
- Clocks and chronometers; the meridian instruments
- Light pollution and the move to Herstmonceux

**Part V: Legacy (Chapters 24–25)**
- Heritage, tourism, and symbolism at Greenwich
- Lessons for science and society from 350 years of precision measurement

### Appendices A–I: Technical Reference

- **Appendix A**: Mathematical Derivations (spherical trigonometry, aberration formulas, Earth orientation)
- **Appendix B**: Instrument Specifications (30+ historical instruments with technical details)
- **Appendix C**: The Astronomers Royal (15 biographical entries, 1675–present)
- **Appendix D**: Visiting Greenwich (practical guide to sites, museums, and resources)
- **Appendix E**: Glossary (100+ astronomical and timekeeping terms)
- **Appendix F**: Bibliography & Further Reading (thematic organization; 160+ sources)
- **Appendix G**: Primary Source Documents (6 curated historical excerpts)
- **Appendix H**: Chronologies (master timeline, instruments, Astronomers Royal tenures)
- **Appendix I**: Reference Tables (unit conversions, astronomical constants, extended data)



## 🛠️ Building the Document

### Requirements

- **TeX Live** (2020 or later) with:
  - `memoir` class (book formatting)
  - `biblatex` and `biber` (bibliography management)
  - `glossaries` (terminology database)
  - `tikz` and `pgfplots` (diagrams and plots)
  - `microtype` (typography refinement)
  - `siunitx` (scientific notation)

- **Perl** (for `latexmk`)
- **Make** (for build automation)
- **Python 3.10+** with `matplotlib`, `numpy`, and `SciencePlots` (figure generation; see `requirements.txt`)

### Installation (macOS)

```bash
# Install TeX Live (if needed)
brew install --cask mactex-no-gui

# Navigate to project directory
cd measure-of-the-world

# Create the Python environment used to generate figures
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Build the PDF (generates figures first)
make build

# View the output
open build/out/measure-of-the-world.pdf
```

### Installation (Linux)

```bash
# Install TeX Live packages
sudo apt install texlive-full

# Build the document
cd measure-of-the-world
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
make build
```

### Build Targets

```bash
make build          # Full build with all processing
make clean          # Remove intermediate files
make distclean       # Remove all generated files including PDF
```

---
## 📁 Project Structure

```
measure-of-the-world/
├── README.md                    # This file
├── Makefile                     # Build automation
├── latexmkrc                    # TeX compilation configuration
├── src/
│   ├── main.tex                # Main document (chapters 1–25 + appendices A–I)
│   ├── metadata.tex            # Author, title, publication info
│   ├── preamble.tex            # Package imports and configuration
│   ├── chapters/               # 25 main chapters
│   │   └── 01.tex through 25.tex
│   ├── appendices/             # 9 appendices (A–I)
│   │   ├── appendix-a.tex      # Mathematical derivations
│   │   ├── appendix-b.tex      # Instrument specifications
│   │   ├── appendix-c.tex      # Astronomers Royal
│   │   ├── appendix-d.tex      # Visiting Greenwich guide
│   │   ├── appendix-e.tex      # Glossary
│   │   ├── appendix-f.tex      # Bibliography
│   │   ├── appendix-g.tex      # Primary sources
│   │   ├── appendix-h.tex      # Chronologies
│   │   └── appendix-i.tex      # Reference tables
│   ├── frontmatter/            # Title page, dedication, copyright
│   ├── glossary/               # Glossary entries (terms, acronyms)
│   ├── bibliography/           # references.bib (160+ sources)
│   ├── figures/                # Illustrations (jpg, pdf, png)
│   └── tables/                 # Data tables
├── build/
│   ├── out/                    # Final PDF
│   │   └── measure-of-the-world.pdf
│   └── tmp/                    # Intermediate LaTeX files
├── LICENSE.md                  # License information
└── Makefile                    # Build automation
```

---

## 📊 Document Statistics

- **Total Pages**: 417 (with appendices)
- **Main Chapters**: 25
- **Appendices**: 9 (A–I)
- **Figures**: ~40 diagrams and historical images
- **Tables**: 50+ data tables (instruments, astronomical data, unit conversions)
- **Bibliography**: 160+ citations (primary and secondary sources)
- **Glossary Terms**: 100+ defined
- **Appendix Content**:
  - 16 Astronomer Royal biographies
  - 3 parallel chronologies (1675–present)
  - 30+ instrument specifications with technical details
  - 6 primary source document excerpts

---
## 📜 License

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

As long as you give appropriate credit.

See [LICENSE](LICENSE) for full details.
