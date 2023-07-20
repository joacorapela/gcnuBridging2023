all: bayesianLinearRegression.pdf

bayesianLinearRegression.pdf: bayesianLinearRegression.tex

%.pdf: %.tex
	pdflatex $<
	bibtex $*.aux
	pdflatex $<
	pdflatex $<
