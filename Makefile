# Python configuration
PYTHON := .venv/bin/python3

# Python figure scripts
FIGURE_SCRIPTS := $(wildcard scripts/figures/ch*.py)
FIGURE_OUTPUTS := $(patsubst scripts/figures/ch%.py,src/figures/generated/.ch%-built,$(FIGURE_SCRIPTS))

.PHONY: build watch clean distclean figures

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
	@# Report undefined references, excluding intentional forward references to future chapters
	@if grep -q "LaTeX Warning: Reference .* undefined" build/tmp/main.log 2>/dev/null; then \
		unresolved=$$(grep "Reference.*undefined" build/tmp/main.log | grep -v "ch:harrison\|ch:escapement\|ch:chronomet" | wc -l); \
		if [ $$unresolved -gt 0 ]; then echo "⚠ $$unresolved unresolved reference(s) found (excluding forward references to future chapters)"; fi; \
	fi
	@# Fail only on undefined citations
	@if grep -q "LaTeX Warning: Citation .* undefined" build/tmp/main.log 2>/dev/null; then echo "✗ Undefined citations found."; exit 1; fi

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
