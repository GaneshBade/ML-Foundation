#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

#  Detect outliers using z-score
outlier = []
def detect_outlier(data):

    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i - mean) / std
        print(f"z_score is {z_score}")

        if np.abs(z_score) > threshold:
            print(f"Outlier data: {i}")
            outlier.append(i)
    return outlier

outlier_pts = detect_outlier(dataset)

#  Detect outlier using IQR
#  Steps:
    # 1. sort data in ascending order
    # 2. calculate q1 and q3
    # 3. Find interquartile range
    # 4. Find lower boundary 1.5*q1
    # 5. Find upper bound 1.5*q3
# Any data point that lies outside of lower and upper bound will be considered as outlier
outlier_iqr = []
def detect_outlier_IQR(data):
    sort_data = sorted(data)
    q1, q3 = np.percentile(sort_data, [25, 75])

    iqr = q3 - q1

    iqr_lower_bound = q1 - (1.5 * iqr)
    iqr_upper_bound = q3 + (1.5 * iqr)

    # print(f"Data : {data}", end=" ")
    # print(f"iqr_lower_bound: {iqr_lower_bound}")
    # print(f"iqr_upper_bound: {iqr_upper_bound}")

    for i in data:
        if (i < iqr_lower_bound) | (i > iqr_upper_bound):
            outlier_iqr.append(i)
    return outlier_iqr

outlierByIQR = detect_outlier_IQR(dataset)















