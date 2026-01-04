# Contributing

Thank you for interest in "The Measure of the World"! This document outlines how to contribute to the project.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/oddurs/measure-of-the-world.git
   cd measure-of-the-world
   ```

2. **Install dependencies**:
   - macOS: `brew install texlive latexmk`
   - Linux: `sudo apt-get install texlive-full latexmk`
   - Windows: Install [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

3. **Test the build**:
   ```bash
   make build
   ```

4. **Read the documentation**:
   - [Style Guide](STYLEGUIDE.md) for writing guidelines
   - [Build Documentation](BUILD.md) for technical details
   - Chapter outlines (in `prompts/`) for structure and scope

## Workflow

### Creating a Feature Branch

```bash
git checkout -b chapter/01-deadly-ignorance
```

Use descriptive branch names:
- `chapter/XX-title` for chapter work
- `figures/XX-description` for figure additions
- `bibliography/section-name` for bibliography work
- `fix/issue-description` for bug fixes

### Writing/Editing a Chapter

1. Edit the appropriate chapter file in `src/chapters/`:
   ```latex
   \chapter{The Deadly Ignorance of Position}
   
   \section{Opening Vignette}
   % Your content here...
   
   \section{The Problem Defined}
   % More content...
   ```

2. Test your changes:
   ```bash
   make watch
   ```
   This starts continuous compilation. Your PDF viewer will update on save.

3. Follow the [Style Guide](STYLEGUIDE.md) for:
   - Formatting conventions
   - Mathematical notation
   - Figure and table placement
   - Bibliography entries

### Adding Figures

1. Place high-quality images in the appropriate subdirectory:
   - JPG: `src/figures/jpg/`
   - PNG: `src/figures/png/`
   - PDF: `src/figures/pdf/`

2. Use descriptive filenames: `maskelyne-chronometer.jpg`, `flamsteed-house-floor-plan.pdf`

3. Include in your chapter:
   ```latex
   \begin{figure}[htbp]
     \centering
     \includegraphics[width=0.8\linewidth]{maskelyne-chronometer.jpg}
     \caption{John Maskelyne's marine chronometer (ca. 1770).}
     \label{fig:maskelyne-chronometer}
   \end{figure}
   ```

4. Reference in text: `See \cref{fig:maskelyne-chronometer}...`

### Adding Bibliography Entries

1. Edit `src/bibliography/references.bib`

2. Add entries in BibTeX format:
   ```bibtex
   @book{flamsteed1725,
     author = {Flamsteed, John},
     year = {1725},
     title = {Historia Coelestis Britannica},
     publisher = {Royal Society},
     address = {London}
   }
   ```

3. Cite in text:
   ```latex
   \citet{flamsteed1725} catalogued over 3,000 stars...
   As shown in \citep{flamsteed1725}...
   ```

### Committing Your Changes

```bash
git add src/chapters/01.tex src/figures/jpg/example.jpg
git commit -m "Write Chapter 1: The Deadly Ignorance of Position

- Introduce the Scilly disaster (1707)
- Explain longitude problem geometry
- Add maritime disaster cases
- Include figure: Shovell's fleet track"
```

Guidelines:
- Write meaningful commit messages
- Keep commits focused on a single topic
- Include references to figures or sections added
- Avoid committing build artifacts (handled by `.gitignore`)

### Pushing and Creating a Pull Request

```bash
git push origin chapter/01-deadly-ignorance
```

Create a pull request with:
- Clear title: "Chapter 1: The Deadly Ignorance of Position"
- Description: Summary of content added, any questions or notes
- References: Link to any related issues or discussions

## Code Review Guidelines

### For Authors
- Expect constructive feedback on content, clarity, and technical accuracy
- Be open to suggestions on structure and emphasis
- Verify all references and citations are accurate
- Test the build before submitting: `make build`

### For Reviewers
- Check for clarity, historical accuracy, and technical correctness
- Ensure adherence to the Style Guide
- Verify figures are high-quality and properly captioned
- Confirm bibliography entries are complete and accurate
- Test the build with changes: `make build`

## Building Your Changes

### Test Build
```bash
make build
```

Ensures:
- LaTeX compilation succeeds
- All references resolve
- All citations resolve
- No undefined labels or bibliography entries

### Watch Mode
```bash
make watch
```

Good for iterative editing. PDF updates on save.

### Full Clean and Rebuild
```bash
make distclean
make build
```

Use if you suspect stale build artifacts are causing issues.

## Chapters & Status

| Chapter | Title | Status |
|---------|-------|--------|
| 1 | The Deadly Ignorance of Position | Outline |
| 2 | The State of the Art in 1675 | Outline |
| ... | ... | ... |
| 25 | Lessons for Science and Society | Outline |

See `prompts/chapter_outlines.md` for detailed outlines of all 25 chapters.

To claim a chapter:
1. Create an issue: "Working on Chapter X: [Title]"
2. Create a branch: `chapter/XX-slug`
3. Submit PR when ready

## Prompts and Planning

The `prompts/` directory tracks:
- `chapter-plans/`: Detailed outlines for each chapter
- `rewriting/`: Revisions and refinements
- `image-prompts/`: Descriptions for figures to commission or generate

These files support collaboration and iteration.

## Questions?

- Review existing issues and discussions
- Check the [Style Guide](STYLEGUIDE.md) and [Build Docs](BUILD.md)
- Open an issue for questions or clarifications

Thank you for contributing!
