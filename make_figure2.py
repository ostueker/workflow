#!/bin/env python
import re
import sys
import os.path
import numpy as np
import matplotlib as mpl
mpl.use('Agg') # Don't use QT backend
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    '''function ax+b for fitting'''
    return a * x + b

if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:
        print('Please supply one data file and one image name. e.g.:')
        print('python {:} data_2a.csv  figure_2a.png'.format(sys.argv[0]))
        sys.exit(1)

    file_name = sys.argv[1]
    figname   = sys.argv[2]

    data_2 = np.loadtxt(file_name, delimiter=',')
    data_2 = data_2.transpose()
    basename = os.path.basename(file_name)

    x     = data_2[0]
    y_raw = data_2[1]
    
    # fitting raw data to function
    popt, pconv  = curve_fit(func, x, y_raw)
    a, b = popt[0], popt[1]
    print("{:}\ta: {:12.8f}, b: {:12.8f}".format(basename, a, b))
    y_fit = func(x, a, b )

    plt.figure(figsize=(8, 6))
    plt.title(file_name)
    plt.scatter(x, y_raw)
    plt.plot(x, y_fit, 'k--')
    plt.ylim(ymin=0 )    
    # plt.ylim(0, 14)

    plt.savefig(figname)
    print('Saved: "{:}"'.format(figname))
