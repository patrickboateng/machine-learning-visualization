import copy
import math

import numpy as np
from sklearn.preprocessing import StandardScaler

from algorithms.cost_functions import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error,
)

cost_functions = {
    "mse": mean_squared_error,
    "rmse": root_mean_squared_error,
    "mae": mean_absolute_error,
}


def hypothesis(x, theta):
    """Calculates the prediction of the model

    Args:
        x: input parameters
        theta: weights of the model
    """

    pred = np.round((x @ theta).flatten(), decimals=4)[0]
    return pred


def error(pred, y_i, X_ij):
    """Calculates the error of a single feature

    Args:
        pred (float): predicted value using `hypothesis`
        y_i (float): the target variable for the ith training eg.
        X_ij (float): the feature value j in the ith training eg.

    Returns:
        float: error
    """
    return (pred - y_i) * X_ij


def gradient(X, y, theta, total_training_egs, j):
    """Calculates the gradient of the cost function

    Args:
        X (numpy.array): input variable/features
        y (numpy.array): output variable/target
        theta (numpy.array): weights of the model
        total_training_egs (int): number of training examples
        j (int): the current parameter

    Returns:
        float: summation of the total error calculated using theta
    """

    sum_error = 0

    for i in range(total_training_egs):
        pred = hypothesis(X[i], theta)
        sum_error += error(pred, y[i], X[i][j])

    return sum_error


def transform_X(X, total_training_egs=None, normalize: bool = True):
    """Transforms the input variable

    Args:
        X: input variable
        total_training_egs: number of training examples
        normalize (bool): checks whether the input variable should be
                          transformed or not
    """

    if X.ndim == 1:
        X = X.reshape(-1, 1)  # convert X to 2 dimensions

    if normalize:
        scaler = StandardScaler()
        scaler.fit(X)
        print(scaler.mean_)
        print(scaler.var_)
        X = scaler.transform(X)

    coefficient_of_constant = np.ones(shape=(total_training_egs, 1))
    X = np.hstack(tup=(coefficient_of_constant, X))

    return X


def _select_cost_function(cost_function):
    if cost_function is None:
        print("Using default cost function (RMSE)")
        compute_cost = cost_functions["rmse"]
    else:
        if isinstance(cost_function, str):
            try:
                compute_cost = cost_functions[cost_function]
            except KeyError:
                print("Cost function not available using Root Mean Squared Error")
                compute_cost = cost_functions["rmse"]

        else:
            compute_cost = cost_function

    return compute_cost


def batch_gradient_descent(
    X,
    y,
    theta=None,
    *,
    alpha: float = 0.01,
    num_iters: int = 3500,
    cost_function=None,
    normalize: bool = True
):
    """Batch Gradient Descent implementation in python.

    Args:
        X (numpy.array): input variable/features
        y (numpy.array): output variable/target
        theta (numpy.array): initial weights/parameters
        alpha (float): learning rate
        num_iters (int): number of iteration taken to run gradient descent
        cost_function (str | callable): loss function used in evaluating the model

    Returns:
        numpy.array: weights of the model

    Raises:

    """

    history = {}

    total_training_egs = len(y)

    X = transform_X(X, total_training_egs=total_training_egs, normalize=normalize)

    if theta is None:
        _, n = X.shape

        theta = np.zeros(shape=(n, 1))

    compute_cost = _select_cost_function(cost_function)

    loss = compute_cost(X, y, theta, total_training_egs)

    step_size = alpha / total_training_egs

    num_of_features, _ = theta.shape

    for epoch in range(num_iters):

        temp_theta = copy.deepcopy(theta)

        for j in range(num_of_features):
            temp_theta[j] = temp_theta[j] - (
                step_size * gradient(X, y, theta, total_training_egs, j)
            )

        theta = copy.deepcopy(temp_theta)

        history[epoch] = loss

        loss = compute_cost(X, y, theta, total_training_egs)

    return theta, history
