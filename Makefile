# Python configuration
PYTHON := .venv/bin/python3

# Python figure scripts
FIGURE_SCRIPTS := $(wildcard scripts/figures/ch*.py)
FIGURE_OUTPUTS := $(patsubst scripts/figures/ch%.py,src/figures/generated/.ch%-built,$(FIGURE_SCRIPTS))

.PHONY: build watch clean distclean figures claims refs figure-qa status verify lint derivations

# Generate all figures
figures: $(FIGURE_OUTPUTS)

# Per-chapter figure generation (only runs if script changed)
src/figures/generated/.ch%-built: scripts/figures/ch%.py scripts/figures/common.py
	@mkdir -p src/figures/generated
	cd scripts/figures && ../../$(PYTHON) ch$*.py
	@touch $@

build: figures
	mkdir -p build/out build/tmp
	latexmk -f -pdf -cd src/main.tex || true
	@if [ -f build/tmp/main.pdf ]; then \
		cp build/tmp/main.pdf build/out/measure-of-the-world.pdf && echo "✓ PDF built successfully: build/out/measure-of-the-world.pdf"; \
	else \
		echo "✗ PDF generation failed"; exit 1; \
	fi
	@# Fail on any LaTeX error, even though latexmk -f produced a PDF.
	@# (nonstopmode lets pdflatex limp past errors; the PDF is not trustworthy.)
	@if grep -qE "^! |^\./.*:[0-9]+: " build/tmp/main.log 2>/dev/null; then \
		echo "✗ LaTeX errors found:"; grep -E "^! |^\./.*:[0-9]+: " build/tmp/main.log | head -20; exit 1; \
	fi
	@# Report undefined references, excluding intentional forward references to future chapters
	@if grep -q "LaTeX Warning: Reference .* undefined" build/tmp/main.log 2>/dev/null; then \
		unresolved=$$(grep "Reference.*undefined" build/tmp/main.log | grep -v "ch:harrison\|ch:escapement\|ch:chronomet" | wc -l); \
		if [ $$unresolved -gt 0 ]; then echo "⚠ $$unresolved unresolved reference(s) found (excluding forward references to future chapters)"; fi; \
	fi
	@# Fail only on undefined citations
	@if grep -q "LaTeX Warning: Citation .* undefined" build/tmp/main.log 2>/dev/null; then echo "✗ Undefined citations found."; exit 1; fi

# --- Production engine ------------------------------------------------
# See docs/plan/production-engine.md. These maintain the ledgers under
# review/ that track how far each chapter has moved through the gates.

# Re-extract claim ledgers from the manuscript. Safe to re-run: verification
# status is preserved for any claim whose sentence has not changed.
claims:
	$(PYTHON) scripts/claims/extract_claims.py

# Resolve every bibliography entry against Crossref, OpenLibrary and Google
# Books. Slow (a few minutes) because it rate-limits itself against free
# endpoints. Pass keys as arguments to check a subset.
refs:
	$(PYTHON) scripts/refs/verify_bib.py

# Overlapping labels, effective printed font size, and image sanity.
figure-qa: figures
	$(PYTHON) scripts/figures/qa.py

# Mechanical style checks against docs/styleguide.md.
lint:
	$(PYTHON) scripts/lint/prose.py

# Recompute the book's worked examples and compare against the printed results.
derivations:
	$(PYTHON) scripts/verify/derivations.py

# Everything that can be checked without a human, in the order that fails fastest.
verify: claims lint derivations figure-qa

# Rebuild docs/status.md from the ledgers.
status:
	$(PYTHON) scripts/status.py

watch:
	latexmk -pdf -pvc -cd src/main.tex

clean:
	latexmk -c -cd src/main.tex
	rm -f src/main.{aux,bcf,fdb_latexmk,fls,glo,ist,log,toc,bbl,blg,run.xml}
	rm -f src/figures/generated/.ch*-built

distclean:
	latexmk -C -cd src/main.tex
	rm -rf build/tmp build/out
	rm -f src/main.{aux,bcf,fdb_latexmk,fls,glo,ist,log,toc,bbl,blg,run.xml}
