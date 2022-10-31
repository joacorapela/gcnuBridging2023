all: rapela.pdf

%.pdf: %.tex
	pdflatex $<
	bibtex $*.aux
	pdflatex $<
	pdflatex $<

clean:
	rm *.aux *.out *.log
