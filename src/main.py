import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from algorithms.cost_functions import (
    mean_squared_error,
    mean_absolute_error,
)

from algorithms.gradient_descent import BatchGradientDescent


if __name__ == "__main__":
    # df = np.loadtxt("../test_data/ex1data1.txt", delimiter=",")

    # X = df[:, 0]
    # y = df[:, 1]

    # X = np.array([1, 2, 3, 4])
    # y = np.array([1.5, 1.6, 2.1, 3.0])

    X = np.array([20, 25, 27, 29, 35, 38, 40])
    y = np.array([83, 90, 93, 95, 99, 110, 120])

    # X = X.reshape(-1, 1)

    # m = len(X)

    # coefficient_of_constant = np.ones((m, 1))

    # X = np.hstack((coefficient_of_constant, X))

    # _, n = X.shape

    # theta = np.zeros((n, 1))

    bgd = BatchGradientDescent(X, y, feature_scaler="min_max")
    theta, history = bgd.run()
    print(theta)
    i = bgd.transform(np.array([[40]])).flatten()[0]

    print(bgd.hypothesis(np.array([[1, i]]), theta))
    # plt.plot(bgdinfo.num_of_epochs, bgdinfo.cost_history)

    # print(mean_squared_error(X, y, theta))

    # for x in X:
    #     print(hypothesis(np.array([[1, x[0]]]), np.array([[0.0322], [0.0876]])))

    # print(hypothesis(np.array([[1, 8.0]]), np.array([[4.57], [-0.45]])))
