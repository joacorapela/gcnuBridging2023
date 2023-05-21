all: foundations.pdf

foundations.pdf: foundations.tex foundations_content.tex

%.pdf: %.tex
	pdflatex $<
	bibtex $*.aux
	pdflatex $<
	pdflatex $<
