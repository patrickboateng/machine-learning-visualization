"""Implementation of various cost functions.

The module contains the following functions:

- `mean_absolute_error(y_pred, y_true, total_training_egs)` - Calculates and returns the mean absolute error of the predicted and actual values.

- `mean_squared_error(y_pred, y_true, total_training_egs)` - Calculates and returns the mean squared error of the predicted and actual values.

- `root_mean_squared_error(y_pred, y_true, total_training_egs)` - Calculates and returns the root mean squared error of the predicted and actual values

"""

import math


def mean_absolute_error(y_pred, y_true, total_training_egs=None) -> float:
    """Calculates the mean absolute error.

    Args:
        y_pred: the predicted values from the model.
        y_true: the actual values from the datasets.
        total_training_egs: the number of training examples in the datasets.

    Returns:
        float: mean absolute error.

    """

    if total_training_egs is None:
        total_training_egs = len(y_pred)

    sum_abs_error = 0

    for actual, guess in zip(y_pred, y_true):
        abs_error = abs(actual - guess)
        sum_abs_error += abs_error

    return sum_abs_error / total_training_egs


def mean_squared_error(y_pred, y_true, total_training_egs=None) -> float:
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


def root_mean_squared_error(y_pred, y_true, total_training_egs=None) -> float:
    """Calculates the root mean squared error.

    Args:
        y_pred: the predicted values from the model.
        y_true: the actual values from the datasets.
        total_training_egs: the number of training examples in the datasets.

    Returns:
        float: root mean squared error.

    """

    avg_squared_error = mean_squared_error(y_pred, y_true, total_training_egs)
    return math.sqrt(avg_squared_error)
