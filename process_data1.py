#!/bin/env python
import numpy as np
import pandas as pd
import sys

if __name__ == '__main__':

    if len(sys.argv[1:]) != 3:
        print('Please supply three data files. e.g.:')
        print('python {:} data_1a.txt data_1b.txt data_1c.txt '.format(sys.argv[0]))
        sys.exit(1)

    # load bio essay data into np arrays
    data_1a = np.loadtxt(sys.argv[1])
    data_1b = np.loadtxt(sys.argv[2])
    data_1c = np.loadtxt(sys.argv[3])
    print('Loaded datafiles: {:}'.format(', '.join(sys.argv[1:4])))

    # calculate averages and standard deviation
    df1 = pd.DataFrame({
        'healthy':    data_1a,
        'treated':    data_1b,
        'untreated':  data_1c,
    })

    means = pd.DataFrame({ 
        'means': df1.mean(),
        'err':   df1.std(),
    })[['means', 'err']]

    means.to_csv('processed_data/means.csv')
    print('Generated processed_data/means.csv')
