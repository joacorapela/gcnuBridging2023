all: inference.pdf

inference.pdf: inference.tex inference_content.tex

%.pdf: %.tex
	pdflatex $<
	bibtex $*.aux
	pdflatex $<
	pdflatex $<
