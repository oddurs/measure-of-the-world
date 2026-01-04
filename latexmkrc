# latexmkrc configuration for "The Measure of the World"
# Handles output directories, biber, glossaries, and strict error handling

$out_dir = "build/tmp";
$pdf_dir = "build/out";

# Use pdflatex engine with strict error handling
$pdflatex = "pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S";

# Biblatex uses biber
$bibtex_use = 2;
$biber = "biber %O %B";

# Glossaries (makeglossaries)
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries {
  my ($base_name, $path) = fileparse( $_[0] );
  return system("makeglossaries -d build/tmp \"$base_name\"");
}

$recorder = 1;

$clean_ext = "acn acr alg aux bbl bcf blg fls fdb_latexmk glg glo gls idx ilg ind ist log lof lot nav out run.xml snm synctex.gz toc vrb xdy";

$recorder = 1;

$clean_ext = "acn acr alg aux bbl bcf blg fls fdb_latexmk glg glo gls idx ilg ind ist log lof lot nav out run.xml snm synctex.gz toc vrb xdy";
