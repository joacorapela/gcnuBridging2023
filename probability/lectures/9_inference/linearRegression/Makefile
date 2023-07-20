all: linearRegression.pdf

linearRegression.pdf: linearRegression.tex

%.pdf: %.tex
	pdflatex $<
	bibtex $*.aux
	pdflatex $<
	pdflatex $<
