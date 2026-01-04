# The Measure of the World

A comprehensive 25-chapter technical history of the Royal Observatory, Greenwich, from its founding in 1675 through the 19th century. The book integrates narrative history, mathematical exposition, and instrument analysis, treating precision as a practical achievement built from instruments, mathematics, and institutional habit.

## Build Requirements

- **TeX Live** (2020 or later) with the following packages:
  - `memoir` class
  - `biblatex` and `biber`
  - `glossaries`
  - `tikz` and `pgfplots`
  - `microtype`
  - `siunitx`

- **Perl** (for `latexmk`)
- **Makeglossaries** (included with glossaries)

## Installation (macOS)

```bash
brew install texlive
brew install latexmk
```

## Building the Document

### Quick Build
```bash
make build
```

This compiles the LaTeX document, runs biber for bibliography processing, and makeglossaries for glossary/acronym generation. The build will fail loudly if there are undefined references or citations.

Output: `build/out/measure-of-the-world.pdf`

### Watch Mode (continuous compilation)
```bash
make watch
```

The PDF viewer will automatically refresh as you edit source files.

### Clean Intermediate Files
```bash
make clean
```

Remove temporary build artifacts but keep the final PDF.

### Full Clean
```bash
make distclean
```

Remove all build output and temporary files.

## Project Structure

```
measure-of-the-world/
├─ src/
│  ├─ main.tex                 # Master document
│  ├─ preamble.tex             # Package setup and configuration
│  ├─ metadata.tex             # Title, author, description
│  ├─ frontmatter/
│  │  ├─ titlepage.tex
│  │  └─ dedication.tex
│  ├─ chapters/
│  │  ├─ 01.tex through 25.tex # Chapter stubs
│  ├─ appendices/
│  │  ├─ appendix-a.tex through appendix-f.tex
│  ├─ figures/
│  │  ├─ jpg/                  # JPEG figures
│  │  ├─ png/                  # PNG figures
│  │  └─ pdf/                  # PDF figures
│  ├─ tables/                  # Table data
│  ├─ bibliography/
│  │  └─ references.bib        # BibTeX entries
│  └─ glossary/
│     ├─ terms.tex             # Glossary terms
│     └─ acronyms.tex          # Acronyms
├─ build/
│  ├─ out/                     # Final PDF output
│  └─ tmp/                     # Temporary build artifacts
├─ prompts/                    # AI prompt history and planning
│  ├─ chapter-plans/
│  ├─ rewriting/
│  └─ image-prompts/
├─ docs/
│  ├─ BUILD.md                 # Detailed build documentation
│  ├─ STYLEGUIDE.md            # Writing and formatting guidelines
│  └─ CONTRIBUTING.md          # Contribution guidelines
├─ Makefile
├─ latexmkrc
├─ .gitignore
├─ .editorconfig
├─ README.md                   # This file
└─ LICENSE
```

## Using Figures

Figures in JPG format are fully supported via `pdflatex`. Place images in the appropriate subdirectory:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{maskelyne-chronometer.jpg}
  \caption{Example instrument photograph.}
  \label{fig:maskelyne-chronometer}
\end{figure}
```

For print-quality output, use 300 DPI at final print size.

## Bibliography & Glossary

### Adding Bibliography Entries

Edit `src/bibliography/references.bib`:

```bibtex
@book{flamsteed1725,
  author = {Flamsteed, John},
  year = {1725},
  title = {Historia Coelestis Britannica},
  publisher = {Royal Society}
}
```

### Adding Glossary Terms

Add to `src/glossary/terms.tex`:

```latex
\newglossaryentry{meridian}{
  name=meridian,
  description={an imaginary great circle on Earth's surface...}
}
```

## Troubleshooting

- **"Undefined references found"**: Check that all `\label{}` commands are present and unique.
- **"Undefined citations found"**: Verify all citations match entries in `references.bib`.
- **Missing graphics**: Ensure image files are in the correct subdirectory (`figures/jpg/`, etc.).
- **LaTeX warnings promoted to errors**: The preamble treats warnings as errors for strict builds. Comment out the warning-to-error hook in `preamble.tex` if needed during early drafting.

## License

See [LICENSE](LICENSE) for details.
