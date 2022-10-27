import math

import numpy as np


def mean_absolute_error(X, y, theta, m=None):

    predictions = (X @ theta).transpose().flatten()  # m

    return np.sum([abs(actual - guess) for guess, actual in zip(predictions, y)]) / m


def mean_squared_error(X, y, theta, m=None):

    predictions = (X @ theta).transpose().flatten()  # m

    if m is None:
        m = len(predictions)

    sum_error = 0

    for actual, guess in zip(y, predictions):
        error = actual - guess
        try:
            error_squared = math.pow(error, 2)
        except OverflowError:
            print(error)
            exit()
        sum_error += error_squared

    return sum_error / m


def root_mean_squared_error(X, y, theta, m=None):
    error = math.sqrt(mean_squared_error(X, y, theta, m=m))

    return np.round(error, decimals=4)
