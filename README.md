# Automated pipelines and Workflows

This contains an example for using `make` to generate 
a workflow for processing data, generating figures
and assembling a report.

* The initial state contains the following files:
	- `Workflow - initial.ipynp` - IPython Notebook with the initial analysis
	- `raw_data/data1[a-c].txt` - Data from a Bio-Essay.
	- `raw_data/data2[a-c].csv` - Some noisy data from calibration runs.
	- `generate_data.py` - Script to create above raw data.

* Second stage has analysis split into separate pyhon files:
	- `process_data1.py` - Calculates means and standard-deviation
	- `make_figure1.py` - Creates barplot and histogram.
	- `make_figure2.py` - Performs linear regression and creates scatterplot.
