#!/bin/env python
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg') # Don't use QT backend
import matplotlib.pyplot as plt

mpl.rcParams['errorbar.capsize'] = 3
mpl.rcParams['grid.linestyle'] = ':'

if __name__ == '__main__':

    if len(sys.argv[1:]) != 4:
        print('Please supply exactly four data files.\n e.g.:')
        print('python {:} data_1a.txt data_1b.txt data_1c.txt means.csv'.format(sys.argv[0]))
        sys.exit(1)

    # load data
    data_1a = np.loadtxt( sys.argv[1])
    data_1b = np.loadtxt( sys.argv[2])
    data_1c = np.loadtxt( sys.argv[3])
    means   = pd.read_csv(sys.argv[4])

    # make plots for Bio Essay
    fig1 = plt.figure(1, (10, 4))
    fig1.suptitle("Bio Assay")

    # Subplot 1: Barplot with error bars:
    ax1 = plt.subplot(121)
    means['means'].plot(kind='bar', yerr=means['err'], title='Averages w/ error bars')
    ax1.yaxis.set_ticks(np.arange(1,10,1), minor=True)
    ax1.yaxis.set_ticks_position(position='both')
    ax1.yaxis.grid(which='both' )
    for label in ax1.get_xmajorticklabels():
        label.set_rotation(30)
        label.set_horizontalalignment("right")

    # Subplot 1: three histograms:
    ax2 = plt.subplot(122)
    ax2.set_title('Distribution')
    ax2.hist(data_1a, bins=30, alpha=0.5, label='healthy' )
    ax2.hist(data_1b, bins=30, alpha=0.5, label='treated' )
    ax2.hist(data_1c, bins=30, alpha=0.5, label='untreated' )
    ax2.legend()

    figname = "plots/figure_1.svg"
    fig1.savefig(figname)
    print('Saved: "{:}"'.format(figname))
