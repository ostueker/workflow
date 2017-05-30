#!/bin/env python
import numpy as np
import pandas as pd

def func(x, a, b):
    '''function ax+b for generating raw data'''
    return a * x + b

if __name__ == '__main__' :
    data1 = np.random.normal(6.0, 0.5, 1000) # healthy
    data2 = np.random.normal(5.8, 2.0, 1000) # treated
    data3 = np.random.normal(4.0, 0.5, 1000) # untreated

    np.savetxt('raw_data/data_1a.txt', data1, header="Example Data: healthy")
    np.savetxt('raw_data/data_1b.txt', data3, header="Example Data: treated")
    np.savetxt('raw_data/data_1c.txt', data2, header="Example Data: untreated")

    x = np.linspace(0, 10 , 101)
    y1 = func(x, 1, 2)
    yn1 = y1 + 0.9 * np.random.normal(size=(len(x)))

    y2 = func(x, -1, 12)
    yn2 = y2 + 0.9 * np.random.normal(size=(len(x)))

    y3 = func(x, 0.2, 5)
    yn3 = y3 + 0.5 * np.random.normal(size=(len(x)))

    pd.DataFrame({'x': x, 'y': yn1}).to_csv('raw_data/data_2a.csv', 
        float_format="%12.8f", header=False, index=False)
    pd.DataFrame({'x': x, 'y': yn2}).to_csv('raw_data/data_2b.csv', 
        float_format="%12.8f", header=False, index=False)
    pd.DataFrame({'x': x, 'y': yn3}).to_csv('raw_data/data_2c.csv', 
        float_format="%12.8f", header=False, index=False)
