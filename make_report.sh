#!/bin/bash

python process_data1.py raw_data/data_1a.txt  raw_data/data_1b.txt  raw_data/data_1c.txt
sleep 5 # let's pretend this step is slooooow

python make_figure1.py  raw_data/data_1a.txt  raw_data/data_1b.txt  raw_data/data_1c.txt  processed_data/means.csv

python make_figure2.py  raw_data/data_2a.csv  plots/figure_2a.svg
python make_figure2.py  raw_data/data_2c.csv  plots/figure_2b.svg
python make_figure2.py  raw_data/data_2c.csv  plots/figure_2c.svg

# pdflatex -shell-escape report
latexmk -pdf  -pdflatex="pdflatex -shell-escape" report
