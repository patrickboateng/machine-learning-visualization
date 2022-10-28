import copy
import math

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from algorithms.cost_functions import (
    mean_absolute_error,
    mean_squared_error,
)


class BatchGradientDescent:

    cost_functions = {
        "mse": mean_squared_error,
        "mae": mean_absolute_error,
    }

    feature_scalers = {"std_scaler": StandardScaler, "min_max": MinMaxScaler}

    def __init__(
        self,
        X,
        y,
        theta=None,
        alpha=0.01,
        num_iters=3500,
        cost_func="rmse",
        normalize: bool = True,
        feature_scaler: str = "std_scaler",
    ):
        self.initial_theta = theta
        self.X = X
        self.y = y
        self.alpha = 0.01
        self.num_iters = num_iters
        self.feature_scaler = feature_scaler
        self.total_training_egs = len(self.y)

        # TODO Check X and y dimensions

        if normalize:
            self.fit()
            self.X = self.transform(self.X)

        coefficient_of_constant = np.ones(shape=(self.total_training_egs, 1))
        self.X = np.hstack(tup=(coefficient_of_constant, self.X))

        try:
            self.compute_cost = self.cost_functions[cost_func]
        except KeyError:
            self.compute_cost = self.cost_functions["mse"]

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, val):
        if val.ndim == 1:
            val = val.reshape(-1, 1)

        self._X = val

        if self.initial_theta is None:
            _, self.num_of_features = self._X.shape
            self.num_of_features += 1
            self.initial_theta = np.zeros(shape=(self.num_of_features, 1))

    def fit(self):
        self.scaler = self.feature_scalers[self.feature_scaler]()
        self.scaler.fit(self.X)

    def transform(self, X):
        return self.scaler.transform(X)

    @staticmethod
    def hypothesis(x, theta) -> float:
        """Calculates the prediction of the model

        Args:
            x: input parameters
            theta: weights of the model
        """

        pred = np.round((x @ theta).flatten(), decimals=4)[0]
        return pred

    @staticmethod
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

    def gradient(self, theta, j) -> float:
        """Calculates the gradient of the cost function

        Args:
            theta: weights of the model
            j (int): the current parameter

        Returns:
            float: summation of the total error calculated using theta
        """

        sum_error = 0

        for i in range(self.total_training_egs):
            pred = self.hypothesis(self.X[i], theta)
            sum_error += self.error(pred, self.y[i], self.X[i][j])

        return sum_error

    def run(self):
        history = {}
        theta = copy.deepcopy(self.initial_theta)
        predictions = (self.X @ theta).transpose().flatten()  # m
        loss = self.compute_cost(predictions, self.y, self.total_training_egs)
        step_size = self.alpha / self.total_training_egs

        for epoch in range(self.num_iters):

            temp_theta = copy.deepcopy(theta)

            for j in range(self.num_of_features):
                temp_theta[j] = temp_theta[j] - (step_size * self.gradient(theta, j))

            theta = copy.deepcopy(temp_theta)

            history[epoch] = loss

            predictions = (self.X @ theta).transpose().flatten()  # m

            loss = self.compute_cost(predictions, self.y, self.total_training_egs)

        return theta, history
