import numpy as np

from optimization_algorithms.optimizers import batch_gradient_descent


if __name__ == "__main__":
    # df = np.loadtxt("../test_data/ex1data1.txt", delimiter=",")

    # X = df[:, 0]
    # y = df[:, 1]

    # X = np.array([1, 2, 3, 4])
    # y = np.array([1.5, 1.6, 2.1, 3.0])

    X = np.array([1, 2, 3, 4, 5])
    y = np.array([4.2, 3.5, 3.0, 3.4, 2.0])

    # X = np.array([20, 25, 27, 29, 35, 38, 40])
    # y = np.array([83, 90, 93, 95, 99, 110, 120])

    X = X.reshape(-1, 1)

    m = len(X)

    coefficient_of_constant = np.ones((m, 1))

    X = np.hstack((coefficient_of_constant, X))

    _, n = X.shape

    theta = np.zeros((n, 1))
    print(theta)

    t = batch_gradient_descent(X, y, theta)
    print(t)
