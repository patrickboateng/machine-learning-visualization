import copy

import numpy as np

from .errors import InconsistentLengthError


def mean_squared_error(y_pred: np.array, y_true: np.array) -> float:
    """Calculates the mean squared error.

    Args:
        y_pred: the predicted values from the model.
        y_true: the actual values from the dataset.

    Returns:
        float: mean squared error.

    """

    errors = np.subtract(y_pred, y_true)
    errors_squared = np.square(errors)

    return np.mean(errors_squared)


def mse_gradient(
    X: np.array, y: np.array, theta: np.array, m: int, num_of_features: int, func
) -> np.array:
    """Calculates the gradient for each feature

    Args:
        X: total number of feature examples
        y: total number of label examples
        theta: weights of the model
        m: number of training examples
        num_of_features: number of features
        func: hypothesis function

    Returns:
        np.array: an array of feature gradients
    """

    errors: list[float] = []

    for j in range(num_of_features):
        sum_error: float = 0.0
        for i in range(m):
            error: float = func(X[i], theta) - y[i]
            error *= X[i][j]
            sum_error += error

        errors.append(sum_error)

    return np.array(errors)


def batch_gradient_descent(
    X: np.array, y: np.array, theta: np.array, alpha: float = 0.01, num_iters=3500
) -> np.array:
    """Batch gradient descent implementation

    Args:
        X: total number of feature examples
        y: total number of label examples
        theta: initial weights of the model
        alpha: learning rate
        num_iters: number of times to repeat the algorithm

    Returns:
        np.array: calculated weights of the model

    Raises:
        InconsistentLengthError: when the lengths of X and y are not equal

    """

    if len(X) != len(y):
        raise InconsistentLengthError(
            f"Length of feature and label variables are not equal: features={len(X)} label={len(y)}"
        )

    m: int = len(y)
    step_size: float = alpha / m
    num_of_features: int = len(theta)

    for _ in range(num_iters):
        temp_theta = copy.deepcopy(theta)

        temp_theta = temp_theta - step_size * mse_gradient(
            X, y, theta, m, num_of_features, lambda x, theta: np.dot(x, theta)
        )

        theta = copy.deepcopy(temp_theta)
        # predictions: np.array = (X @ theta).transpose().flatten()  # m
        # cost: float = mean_squared_error(predictions, y)
        # print(cost)

    return theta
