import math

import numpy as np


def mean_absolute_error(X, y, theta, m=None):

    predictions = (X @ theta).transpose().flatten()  # m

    return np.sum([abs(actual - guess) for guess, actual in zip(predictions, y)]) / m


def mean_squared_error(X, y, theta, m=None):

    predictions = (X @ theta).transpose().flatten()  # m

    error = (
        np.sum([math.pow(actual - guess, 2) for guess, actual in zip(predictions, y)])
        / m
    )

    return np.round(error, decimals=4)


def root_mean_squared_error(X, y, theta, m=None):
    error = math.sqrt(mean_squared_error(X, y, theta, m=m))

    return np.round(error, decimals=4)
