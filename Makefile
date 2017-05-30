# Makefile to process datafiles, generate a plot and build LaTeX report.
#
# Variable with list of files with raw data:
DATA1=raw_data/data_1a.txt raw_data/data_1b.txt raw_data/data_1c.txt
FIGURES=plots/figure_1.svg  plots/figure_2a.svg  plots/figure_2b.svg  plots/figure_2c.svg

report.pdf:  report.tex  $(FIGURES)
	latexmk  report.tex  -pdf -pdflatex='pdflatex -shell-escape'

plots/figure_1.svg:  make_figure1.py  $(DATA1)  processed_data/means.csv
	python  make_figure1.py  $(DATA1)  processed_data/means.csv

plots/figure_2a.svg: make_figure2.py  raw_data/data_2a.csv
	python  make_figure2.py  raw_data/data_2a.csv  plots/figure_2a.svg

plots/figure_2b.svg: make_figure2.py  raw_data/data_2b.csv
	python  make_figure2.py  raw_data/data_2b.csv  plots/figure_2b.svg

plots/figure_2c.svg: make_figure2.py  raw_data/data_2c.csv
	python  make_figure2.py  raw_data/data_2c.csv  plots/figure_2c.svg

processed_data/means.csv: process_data1.py  $(DATA1)
	python  process_data1.py  $(DATA1)

.PHONY:  clean  almost_clean

clean:  almost_clean
	rm report.pdf
	rm plots/figure*
	rm processed_data/means.csv

almost_clean:
	latexmk -c
	rm *.pyg