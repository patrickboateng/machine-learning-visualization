import copy
import math

import numpy as np


def mean_squared_error(
    y_pred: np.array, y_true: np.array, total_training_egs: int = None
) -> float:
    """Calculates the mean squared error.

    Args:
        y_pred: the predicted values from the model.
        y_true: the actual values from the datasets.
        total_training_egs: the number of training examples in the datasets.

    Returns:
        float: mean squared error.

    """

    if total_training_egs is None:
        total_training_egs = len(y_pred)

    sum_squared_error = 0

    for actual, guess in zip(y_true, y_pred):
        error_squared = math.pow((actual - guess), 2)
        sum_squared_error += error_squared

    return sum_squared_error / total_training_egs


def gradient(X: np.array, y: np.array, theta: np.array, m: int, j: int, func):

    sum_error = 0

    for i in range(m):
        sum_error += (func(X[i], theta) - y[i]) * X[i][j]

    return sum_error


def batch_gradient_descent(
    X: np.array, y: np.array, theta: np.array, alpha: float = 0.01, num_iters=3500
):
    m = len(y)
    step_size = alpha / m
    num_of_features = len(theta)

    for _ in range(num_iters):
        temp_theta = copy.deepcopy(theta)

        for j in range(num_of_features):
            temp_theta[j] = temp_theta[j] - (
                step_size
                * gradient(
                    X,
                    y,
                    theta,
                    m,
                    j,
                    lambda x, theta: np.dot(x, theta),
                )
            )

        theta = copy.deepcopy(temp_theta)
        predictions = (X @ theta).transpose().flatten()  # m
        cost = mean_squared_error(predictions, y, m)
        print(cost)

    return theta
