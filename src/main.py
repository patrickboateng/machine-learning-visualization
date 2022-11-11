from time import time

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from optimization_algorithms.optimizers import batch_gradient_descent
from optimization_algorithms.optimizers import normal_eqn


if __name__ == "__main__":
    # df = np.loadtxt("../test_data/ex1data1.txt", delimiter=",")

    # X = df[:, 0]
    # y = df[:, 1]

    # df = pd.read_csv("../test_data/mod_carprices.csv")

    # X = df[["mileage", "age"]].values
    # y = df["sell_price"].values

    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)

    X = np.array([1, 2, 3, 4])
    y = np.array([1.5, 1.6, 2.1, 3.0])

    # X = np.array([1, 2, 3, 4, 5])
    # y = np.array([4.2, 3.5, 3.0, 3.4, 2.0])

    # X = np.array([20, 25, 27, 29, 35, 38, 40])
    # y = np.array([83, 90, 93, 95, 99, 110, 120])

    # if X.ndim == 1:
    #     X = X.reshape(-1, 1)

    # m = len(X)

    # coefficient_of_constant = np.ones((m, 1))

    # # X = np.c_[coefficient_of_constant, X]

    # _, n = X.shape

    # theta = np.zeros((n,))

    # t = batch_gradient_descent(X, y, theta)
    # print(t)

    start = time()
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    end = time()
    print(model.coef_)
    print(model.intercept_)
    print(f"Elapsed Time = {end - start}")

    start = time()
    theta = batch_gradient_descent(X, y)
    end = time()
    print(theta)
    print(f"Elapsed Time = {end - start}")

    start = time()
    theta = normal_eqn(X, y)
    end = time()
    print(theta)
    print(f"Elapsed Time = {end - start}")
