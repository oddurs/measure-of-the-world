.PHONY: build watch clean distclean

build:
	mkdir -p build/out
	latexmk -f -pdf -cd src/main.tex || true
	cp src/build/tmp/main.pdf build/out/measure-of-the-world.pdf 2>/dev/null || true
	@# Fail the build if common unresolved issues remain:
	@if grep -q "LaTeX Warning: Reference .* undefined" src/build/tmp/main.log 2>/dev/null; then echo "Undefined references found."; exit 1; fi
	@if grep -q "LaTeX Warning: Citation .* undefined" src/build/tmp/main.log 2>/dev/null; then echo "Undefined citations found."; exit 1; fi

watch:
	latexmk -pdf -pvc -cd src/main.tex

clean:
	latexmk -c -cd src/main.tex

distclean:
	latexmk -C -cd src/main.tex
	rm -rf build/tmp build/out
