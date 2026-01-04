# Build Documentation

This document provides detailed information on building "The Measure of the World" LaTeX document.

## Prerequisites

### macOS
```bash
brew install texlive
brew install latexmk
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install texlive-full latexmk
```

### Windows
Download and install [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/).

## Build System Overview

The project uses:

- **latexmk**: Automated build tool that handles multiple compilation passes
- **pdflatex**: PDF generation engine (supports JPG images natively)
- **biber**: Bibliography processor (part of biblatex ecosystem)
- **makeglossaries**: Glossary and acronym processor

## Build Process

### 1. Build (`make build`)

Executes:
1. Invoke `latexmk -pdf` with pdflatex engine
2. Automatic handling of:
   - Multiple pdflatex passes (for references, TOC)
   - Biber run (bibliography)
   - Makeglossaries run (glossaries/acronyms)
3. Strict error checking: fails if undefined refs/cites remain

**Configuration**: See `latexmkrc` and `Makefile`

### 2. Watch Mode (`make watch`)

Continuous compilation with `-pvc` flag:
- Monitors source files for changes
- Automatically recompiles on save
- Opens/updates PDF viewer

### 3. Cleaning

- `make clean`: Remove temporary files, keep final PDF
- `make distclean`: Complete cleanup including PDF

## Configuration Files

### latexmkrc
- Engine: pdflatex with `-halt-on-error`
- Output: `build/tmp/` (intermediates), `build/out/` (final PDF)
- Job name: `measure-of-the-world` → outputs to `measure-of-the-world.pdf`
- Glossary support via `makeglossaries` custom dependency
- Clean extensions: comprehensive LaTeX artifact list

### Makefile
- `build`: Compile and validate
- `watch`: Continuous mode
- `clean`: Partial cleanup
- `distclean`: Full cleanup

Validation checks:
```bash
grep "LaTeX Warning: Reference .* undefined" build/tmp/*.log
grep "LaTeX Warning: Citation .* undefined" build/tmp/*.log
```

## Handling Errors

### Build Fails with "halt-on-error"

Real errors (syntax, missing files) stop the build immediately. Check:
- Spelling in `\input{filename}` statements
- Balanced braces `{}`
- Valid LaTeX commands

### Undefined References/Citations

Build will fail in final validation step. Ensure:
- All `\label{fig:...}`, `\label{sec:...}` are present
- All `\cite{}` or `\citet{}`/`\citep{}` have matching `.bib` entries
- Bibliography file has no syntax errors

Example citation:
```latex
\citet{flamsteed1725} showed...  % Creates: (Author Year)
As shown in \citep{flamsteed1725}...  % Creates: (Author Year)
```

### Missing Graphics

LaTeX will error if image files are not found. Verify:
- Images are in `src/figures/jpg/`, `src/figures/png/`, or `src/figures/pdf/`
- Filenames match exactly (case-sensitive on Unix)
- Path in `\includegraphics{}` is relative to `src/main.tex`

## Advanced Configuration

### Switch to lualatex

Edit `latexmkrc`, line 6:
```perl
$pdflatex = "lualatex -interaction=nonstopmode -halt-on-error -file-line-error -jobname=measure-of-the-world %O %S";
```

Benefits: Better Unicode, modern fonts. Drawback: Slower compilation.

### Disable Warning-to-Error Promotion

Comment out lines 35–39 in `src/preamble.tex`:
```latex
% \usepackage{etoolbox}
% \makeatletter
% \pretocmd{\@latex@warning}{\GenericError{}{LaTeX Warning promoted to error}{}{}}{}{}
% \makeatother
```

## Output Locations

- **Final PDF**: `build/out/measure-of-the-world.pdf`
- **Build Log**: `build/tmp/main.log`
- **Biber Log**: `build/tmp/main.blg`
- **Makeglossaries Log**: `build/tmp/main.glg`

## Performance Tips

- First build is slowest (full compilation + biber + glossaries)
- Subsequent builds are fast if only content changed
- Watch mode avoids full rebuilds between edits
- Clean builds from scratch: `make distclean && make build`

## Debugging Tips

To see detailed LaTeX output:
```bash
tail -f build/tmp/main.log
```

To check biber status:
```bash
cat build/tmp/main.blg
```

To manually run makeglossaries:
```bash
makeglossaries -d build/tmp main
```
