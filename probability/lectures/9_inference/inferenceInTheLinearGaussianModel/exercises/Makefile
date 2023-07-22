all: exercises.pdf

%.pdf: %.tex
	pdflatex $<
	bibtex $*.aux
	pdflatex $<
	pdflatex $<
