# latexmkrc configuration for "The Measure of the World"
# Handles output directories, biber, glossaries, and strict error handling
# All build artifacts are output to the project root's build/ directory

$out_dir = "../build/tmp";
$pdf_dir = "../build/out";
$aux_dir = "../build/tmp";

# Use pdflatex engine with nonstopmode to allow builds to complete despite warnings
# -output-directory puts all auxiliary files in the output directory
$pdflatex = "pdflatex -interaction=nonstopmode -file-line-error -output-directory=../build/tmp %O %S";

# Biblatex uses biber
$bibtex_use = 2;
$biber = "biber %O %B";

# Glossaries (makeglossaries) - ignore empty glossaries
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries {
  my ($base_name, $path) = fileparse( $_[0] );
  my $result = system("makeglossaries -d ../build/tmp \"$base_name\" 2>/dev/null");
  # Ignore errors from empty glossaries (return code 1 is acceptable)
  return 0 if $result == 256; # makeglossaries returns 1 (256 in perl) for empty glossaries
  return $result;
}

$recorder = 1;

$clean_ext = "acn acr alg aux bbl bcf blg fls fdb_latexmk glg glo gls idx ilg ind ist log lof lot nav out run.xml snm synctex.gz toc vrb xdy";

