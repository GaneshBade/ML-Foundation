#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Data points that falls outside of 1.5 times IQR

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

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

outlier_pts = detect_outlier(dataset)
