
texfile := mdetlsst
default: pdf

figures:
	python code/make_trend_fig.py --pdf trends.pdf

# just run it
bib:
	bibtex ${texfile}

pdf:
	pdflatex ${texfile}
	pdflatex ${texfile}

clean:
	rm -f \
	${texfile}.dvi \
	${texfile}.out \
	${texfile}.ps \
	${texfile}.pdf \
	${texfile}.aux \
	${texfile}.bbl \
	${texfile}.blg \
	${texfile}.toc \
	${texfile}.log \
	${texfile}.fdb_latexmk \
	${texfile}.fls \
	${texfile}.brf
