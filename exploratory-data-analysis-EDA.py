#! /usr/bin/env python3
# exploratory-data-analysis-EDA.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
# import scipy.optimize as opt

# Uses numpy statistics routines, scipy.stats statistical functions, and 
# possibly scipy.optimize optimization.
# Note you can also implement pandas if needed.

first_data = np.array([8.8, 3.1, 4.2, 6.2, 7.6, 3.6, 5.2, 8.6, 6.3, 1.8, 6.8, 3.9]) # mg/L
# number_of_elements = first_data.size # 1D
number_or_elements = first_data.shape # multipleD
# row, col = first_data.shape # 2D
minimum = np.amin(first_data)
maximum = np.amax(first_data)
peak_to_peak = np.ptp(first_data)

mean = np.mean(first_data)
std = np.std(first_data)
std_of_mean = stat.sem(first_data)
# covariance = np.cov(first_data, second_data) # for 2D datasets

# Describe data statistics
print(' ')
print('overview', stat.describe(first_data))
print('number_or_elements', number_or_elements)
print('minimum', minimum)
print('maximum', maximum)
print('peak_to_peak', peak_to_peak)
print('mean', mean)
print('std', std)
print('std_of_mean', std_of_mean)
# print('covariance', covariance)