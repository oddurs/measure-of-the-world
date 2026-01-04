.PHONY: build watch clean distclean

build:
	mkdir -p build/out
	latexmk -pdf -cd src/main.tex
	cp src/build/tmp/main.pdf build/out/measure-of-the-world.pdf 2>/dev/null || cp build/tmp/main.pdf build/out/measure-of-the-world.pdf 2>/dev/null || true
	@# Fail the build if common unresolved issues remain:
	@! grep -R "LaTeX Warning: Reference .* undefined" build/tmp/*.log >/dev/null 2>&1 || (echo "Undefined references found." && exit 1)
	@! grep -R "LaTeX Warning: Citation .* undefined" build/tmp/*.log >/dev/null 2>&1 || (echo "Undefined citations found." && exit 1)

watch:
	latexmk -pdf -pvc -cd src/main.tex

clean:
	latexmk -c -cd src/main.tex

distclean:
	latexmk -C -cd src/main.tex
	rm -rf build/tmp build/out
