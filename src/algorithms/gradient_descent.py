import copy

import numpy as np

from algorithms.cost_functions import (
    root_mean_squared_error,
    mean_squared_error,
    mean_absolute_error,
)


cost_functions = {
    "mse": mean_squared_error,
    "rmse": root_mean_squared_error,
    "mae": mean_absolute_error,
}


def hypothesis(x, theta):

    pred = np.round((x @ theta).flatten(), decimals=4)[0]

    return pred


def error(pred, y_i, X_ij):
    return (pred - y_i) * X_ij


def gradient(X, y, theta, m, j):

    sum_error = 0

    for i in range(m):

        pred = hypothesis(X[i], theta)

        sum_error += error(pred, y[i], X[i][j])

    return sum_error


def check_X_dimension(X):
    pass


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
    alpha=0.01,
    num_iters=3500,
    cost_function=None,
):

    m = len(y)

    if X.ndim == 1:

        X = X.reshape(-1, 1)  # convert X to 2 dimensions

    coefficient_of_constant = np.ones(shape=(m, 1))

    X = np.hstack(tup=(coefficient_of_constant, X))

    if theta is None:
        _, n = X.shape

        theta = np.zeros(shape=(n, 1))

    cost_history = []  # Keep current best score

    compute_cost = _select_cost_function(cost_function)

    loss = compute_cost(X, y, theta, m)

    step_size = alpha / m

    num_of_features, _ = theta.shape

    for _ in range(num_iters):

        temp_theta = copy.deepcopy(theta)

        for j in range(num_of_features):
            temp_theta[j] = temp_theta[j] - (step_size * gradient(X, y, theta, m, j))

        cost_history.append(loss)

        theta = copy.deepcopy(temp_theta)

        loss = compute_cost(X, y, theta, m)

    return theta
