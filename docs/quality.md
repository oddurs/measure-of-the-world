# Quality Control Prompt for Chapter Editing

## Overview
This document serves as a comprehensive editorial guide for proof-editing and formatting chapters in the *Measure of the World* manuscript. It combines book editorial standards with technical LaTeX formatting requirements. Apply this checklist to each chapter to ensure consistency, clarity, and publication-ready quality.

---

## I. Content & Narrative Quality

### Clarity and Voice
- [ ] Is the writing clear and accessible without oversimplifying technical concepts?
- [ ] Does the chapter maintain a consistent narrative voice and perspective?
- [ ] Are jargon terms defined on first use?
- [ ] Are complex sentences broken into shorter, clearer statements?
- [ ] Do paragraph transitions flow logically and guide the reader?

**Improvements to Consider:**
- Replace passive voice with active voice where possible
- Break overly complex sentences (>25 words) into multiple sentences
- Add transitional phrases connecting paragraphs
- Define technical terms in the text, not only in the glossary

### Structure and Organization
- [ ] Does the chapter have a clear introduction setting up its scope and relevance?
- [ ] Are subsections ordered logically, building on previous concepts?
- [ ] Does the chapter conclude with a summary or connection to subsequent chapters?
- [ ] Are there orphaned sections that don't connect to the main narrative?
- [ ] Do section headings accurately reflect their content?

**Improvements to Consider:**
- Add a brief introductory paragraph explaining the chapter's role
- Reorder sections for better conceptual flow
- Merge similar subsections or split oversized ones
- Ensure all subsections are at least 3-4 paragraphs (avoid one-paragraph subsections)

### Historical Accuracy and Attribution
- [ ] Are historical figures and discoveries accurately described with correct dates?
- [ ] Are primary sources properly cited when quoting or paraphrasing?
- [ ] Are controversies or competing historical interpretations acknowledged?
- [ ] Are modern inaccuracies (anachronisms) avoided?
- [ ] Are technical details (instrument specifications, measurements) verifiable?

**Questions to Ask:**
- Is there a reliable source for this historical claim?
- Are the dates consistent with other mentions in the manuscript?
- Does this statement require attribution, or is it well-established fact?
- Are there competing interpretations of this historical event?

---

## II. Mathematical & Technical Content

### Equations and Calculations
- [ ] Are all equations properly displayed and centered (using `equation` or `align` environments)?
- [ ] Do complex equations have line numbers for reference?
- [ ] Are variables defined before use? (e.g., "$v$ is velocity in m/s")
- [ ] Are calculations worked through step-by-step with sufficient detail?
- [ ] Are results compared to historical values where relevant?

**Improvements to Consider:**
- Add variable definitions immediately after equations
- Show intermediate calculation steps (avoid jumping to final results)
- Include units in all numerical results
- Compare modern values to historical measurements to demonstrate precision improvement

### Technical Explanations
- [ ] Are concepts explained before diving into mathematical detail?
- [ ] Is there a diagram or figure supporting complex technical explanations?
- [ ] Are simplifying assumptions explicitly stated?
- [ ] Are limitations or edge cases mentioned?
- [ ] Is the "so what?" clearly explained (why does this matter)?

**Questions to Ask:**
- Would a diagram clarify this explanation?
- Have I assumed reader knowledge that might not be present?
- What assumptions am I making about the physics/mathematics?
- Why should readers care about this technical detail?

---

## III. References & Cross-References

### Citation Completeness
- [ ] Are all figures referenced in text? (using `\ref{fig:label}`)
- [ ] Are all tables referenced in text? (using `\ref{tab:label}`)
- [ ] Are all equations referenced where needed?
- [ ] Are citations to chapters, sections, and appendices using `\ref{}` or `\pageref{}`?
- [ ] Do all references resolve without warnings?

**Check for:**
```
Undefined references: grep "undefined" build/tmp/main.log
```

### Bibliography and Sources
- [ ] Are all sources mentioned in text cited in the bibliography?
- [ ] Are bibliography entries formatted consistently?
- [ ] Are URLs for digital sources included with access dates?
- [ ] Are out-of-print historical texts properly cited with publication dates?

**Improvements to Consider:**
- Add publication details (publisher, year) for all non-journal sources
- Include DOIs for recent academic papers when available
- Distinguish primary sources (historical documents) from secondary sources (modern books)

### Internal Cross-References
- [ ] Do references to other chapters use the form "Chapter X" or "Section X.Y"?
- [ ] Are forward references to appendices clear? (e.g., "see Appendix A")
- [ ] Are glossary terms referenced when first encountered in technical context?

---

## IV. Language & Style

### Grammar and Mechanics
- [ ] Is the writing free of grammatical errors?
- [ ] Are verb tenses consistent throughout the chapter?
- [ ] Is capitalization used correctly (especially for proper nouns, titles)?
- [ ] Are contractions avoided in formal writing? (use "do not" instead of "don't")
- [ ] Are all acronyms defined on first use? (e.g., "Greenwich Mean Time (GMT)")

**Common Issues to Fix:**
- Inconsistent capitalization of instrument names (e.g., "Airy Transit Circle")
- Tense shifts between past (historical) and present (describing concepts)
- Misuse of "its" vs. "it's"
- Comma splices and run-on sentences

### Word Choice and Precision
- [ ] Are technical terms used precisely and consistently?
- [ ] Are vague words ("seems," "appears," "various") replaced with specific language?
- [ ] Do transitions between ideas use precise connecting words?
- [ ] Is vocabulary accessible without sacrificing accuracy?

**Improvements to Consider:**
- Replace "seems" with specific observation or measurement
- Replace "various" with explicit examples (e.g., "five" instead of "various")
- Use consistent terminology for the same concept throughout the chapter
- Avoid qualifiers ("quite," "rather," "somewhat") unless they add meaning

### Tone and Voice
- [ ] Does the chapter maintain an authoritative but accessible tone?
- [ ] Are speculative statements clearly marked as such?
- [ ] Does the author avoid unnecessary editorializing?
- [ ] Is the level of formality consistent with surrounding chapters?

---

## V. LaTeX Formatting & Consistency

### Document Structure
- [ ] Does the chapter begin with `\chapter{Title}` or `\section{Title}`?
- [ ] Are section headings properly formatted with `\section{}`, `\subsection{}`, etc.?
- [ ] Are all headings sentence-case (unless proper nouns)?
- [ ] Is the chapter label set correctly? (e.g., `\label{ch:chapter-name}`)
- [ ] Are subsection labels set? (e.g., `\label{sec:subsection-name}`)

**Examples:**
```latex
\chapter{Measurement and Error}
\label{ch:measurement-error}

\section{Types of Observational Error}
\label{sec:observational-errors}
```

### Typography
- [ ] Are em-dashes used correctly (—) instead of hyphens (--)?
- [ ] Are ellipses properly formatted (`\ldots` or `\cdots` in math)?
- [ ] Are quotation marks properly nested and oriented?
- [ ] Are special characters (°, ′, ″, ±, ×, ÷) properly LaTeX-encoded?
- [ ] Are non-breaking spaces used appropriately (e.g., "Section~\ref{sec:name}")?

**Common Fixes:**
```latex
% Wrong:
- Replace -- with em-dash
- Use ... instead of \ldots

% Correct:
- Replace --- with em-dash
- Use \ldots for ellipsis or \cdots in math

% Temperature: 23°C
23°\text{C} or 23\,°\text{C}

% Arc notation: 20.5″ (arcseconds)
$20.5''$ or $20.5\arcsec$

% Non-breaking space:
Section~\ref{sec:name} instead of Section \ref{sec:name}
```

### Lists and Enumeration
- [ ] Are bulleted lists using `itemize` environment?
- [ ] Are numbered lists using `enumerate` environment?
- [ ] Do list items start with capital letters if they're complete sentences?
- [ ] Are list items parallel in structure?

### Emphasis
- [ ] Is emphasis used sparingly for important concepts?
- [ ] Are italics used for book titles, journal names, and foreign words?
- [ ] Is bold reserved for headings, not used for emphasis in body text?
- [ ] Are small caps (`\textsc{}`) used for historical figures' names on first mention?

---

## VI. Figures and Tables

### Figure Quality
- [ ] Are all figures referenced in text before appearance?
- [ ] Do figures have descriptive captions explaining what to observe?
- [ ] Are figure labels and references consistent?
- [ ] Are figures high resolution (≥300 DPI for print)?
- [ ] Are figures positioned near their first reference?

**Figure Caption Structure:**
```latex
\begin{figure}
  \includegraphics[width=0.8\textwidth]{path/to/figure}
  \caption{Brief title. Detailed explanation of what the figure shows,
    key features to observe, and how it relates to the text.}
  \label{fig:descriptive-name}
\end{figure}
```

### Table Quality
- [ ] Are all tables referenced in text before appearance?
- [ ] Do tables have clear captions explaining their contents?
- [ ] Are column headers descriptive and properly aligned?
- [ ] Are table labels consistent and descriptive?
- [ ] Is table formatting consistent with document style?
- [ ] Are data sources cited if from external sources?

**Questions to Ask:**
- Could this table be replaced with a figure for better clarity?
- Are there too many columns/rows (consider breaking into multiple tables)?
- Are the units clearly labeled for all numerical data?

---

## VII. Specific Historical Content Checks

### For Biographical Sections
- [ ] Are birth-death years included on first mention?
- [ ] Are professional titles used accurately (e.g., "Astronomer Royal" vs. "Astronomer")?
- [ ] Are educational backgrounds verified?
- [ ] Are major contributions accurately described with supporting evidence?

### For Observational/Measurement Data
- [ ] Are measurement units clearly stated?
- [ ] Are measurement uncertainties or tolerances mentioned?
- [ ] Is context provided for why a measurement matters?
- [ ] Are comparisons to modern measurements included?

### For Timeline Information
- [ ] Are dates consistent with historical records?
- [ ] Are date formats consistent (e.g., "January 5, 1700" not "5 Jan 1700")?
- [ ] Are BC/AD designations used correctly if applicable?
- [ ] Are century references clear (e.g., "1700s" for 18th century)?

---

## VIII. Appendices and Supplementary Material

### For Chapters with Appendices
- [ ] Are extended proofs or detailed calculations in appendices?
- [ ] Is supplementary data properly tabulated and labeled?
- [ ] Are appendix references clear and complete?
- [ ] Do appendices enhance rather than burden the main narrative?

### For Glossary Terms
- [ ] Are technical terms properly defined in the glossary?
- [ ] Are definitions consistent across all uses?
- [ ] Are related terms cross-referenced?

---

## IX. Editorial Checklists by Chapter Type

### Science/Historical Narrative Chapters
Use: **Historical Accuracy** + **Technical Explanations** + **Biographical Content**

- [ ] Timeline accurate
- [ ] Figures properly credited/sourced
- [ ] Mathematical derivations complete and verifiable
- [ ] Historical context clear

### Technical/Mathematical Chapters
Use: **Equations & Calculations** + **Technical Explanations** + **Clarity**

- [ ] Derivations step-by-step
- [ ] Variables defined
- [ ] Assumptions stated
- [ ] Results connected to physical reality

### Reference/Data Chapters
Use: **Table Quality** + **Citation Completeness** + **Consistency**

- [ ] Data sourced and cited
- [ ] Table formatting consistent
- [ ] Units clearly labeled
- [ ] Data ranges and accuracy specified

---

## X. Final Review Checklist

Before declaring a chapter complete, verify:

- [ ] No undefined references or citations
- [ ] All figures and tables present and captioned
- [ ] No LaTeX warnings or errors in log file
- [ ] Chapter builds correctly in isolation and in full document
- [ ] PDF output is properly formatted (check physical pages)
- [ ] Chapter word count is reasonable (verify pacing)
- [ ] No orphaned widows or orphans (single lines at page breaks)
- [ ] Footnotes/endnotes properly formatted and cross-referenced
- [ ] No inconsistencies with chapter style or title capitalization
- [ ] Tone and voice consistent with surrounding chapters

---

## XI. Common Technical Issues & Fixes

### LaTeX Warning: "Undefined reference to ..."
**Fix:** 
1. Ensure label exists: `\label{fig:name}` for figures
2. Rebuild document twice: `latexmk -f -pdf src/main.tex`
3. Check reference uses matching label: `\ref{fig:name}`

### LaTeX Warning: "Reference on page X of Y; possible infinite loop"
**Fix:** Rebuild document (LaTeX sometimes requires multiple passes)

### Typography: Special Characters Not Displaying
**Problem:** ° (degrees), ′ (arcminutes), ″ (arcseconds) display incorrectly
**Fix:** Use proper LaTeX encoding:
- `$\pm$` for ±
- `$\times$` for ×
- `$\approx$` for ≈
- `$\circ$` or `°` for degrees

### Overfull hbox warnings
**Fix:** Reword sentence to fit line width, or use `\hspace{-0.2em}` sparingly

### Tables extending beyond margins
**Fix:** Use `\resizebox{\textwidth}{!}{...}` or reduce font size with `\small`

---

## XII. Tone Guidance by Topic

**When discussing historical figures:** Use respectful, objective language; avoid anachronistic judgments.

**When explaining measurements:** Emphasize uncertainty and precision; explain why accuracy matters.

**When describing instruments:** Be specific about optical/mechanical design; explain how design improves measurement.

**When discussing scientific theories:** Present historically accurate understanding; distinguish from modern knowledge.

**When correcting historical misconceptions:** Gently introduce the misconception, then explain the corrected understanding.

---

## Implementation Guide

**How to use this checklist:**
1. Read the full chapter once without making edits
2. Complete sections **I-II** (content quality) in a second pass
3. Complete sections **III-IV** (references & language) in a third pass
4. Complete sections **V-VI** (formatting & figures) in a fourth pass
5. Run the chapter-specific checklist from **IX**
6. Perform final review from **X**
7. Build document and check output PDFs

**Recommended Review Order:**
- Author first pass (addressing major content issues)
- Structural editor (reordering sections, improving flow)
- Copy editor (grammar, consistency, style)
- Technical editor (LaTeX formatting, citations)
- Proofreader (final read for typos, formatting)

---

## Notes for Editors

This prompt is *opinionated*. Apply changes that improve clarity and consistency even if they differ from the author's original phrasing, but always preserve scientific accuracy and authorial voice. When uncertain, flag the issue rather than making an editorial decision.

Consistency is a priority: if terminology, formatting, or style varies between chapters, standardize to match the best examples in the manuscript.
