import numpy as np

from algorithms.cost_functions import (
    mean_squared_error,
    root_mean_squared_error,
    mean_absolute_error,
)

from algorithms.gradient_descent import batch_gradient_descent, hypothesis


if __name__ == "__main__":
    df = np.loadtxt("../test_data/ex1data1.txt", delimiter=",")

    X = df[:, 0]
    y = df[:, 1]

    # X = np.array([20, 25, 27, 29, 35, 38, 40])
    # y = np.array([83, 90, 93, 95, 99, 110, 120])

    # X = X.reshape(-1, 1)

    # m = len(X)

    # coefficient_of_constant = np.ones((m, 1))

    # X_mod = np.hstack((coefficient_of_constant, X))

    # _, n = X_mod.shape

    # theta = np.zeros((n, 1))

    print(batch_gradient_descent(X, y, cost_function="mse"))

    # for x in X:
    #     print(hypothesis(np.array([[1, x[0]]]), np.array([[0.0322], [0.0876]])))

    # print(hypothesis(np.array([[1, 8.0]]), np.array([[4.57], [-0.45]])))
