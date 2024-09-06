import numpy as np
import scipy.stats as sp


class DataCalculator:
    def __init__(self, data: list[int | float]):
        self.data = []
        self.validate_data(data)

        self.mean = self.get_mean()
        self.median = self.get_median()
        self.mode = self.get_mode()
        self.variance = self.get_variance()
        self.standard_deviation = self.get_standard_deviation()
        self.min = self.get_min()
        self.max = self.get_max()

    def validate_data(self, in_data):
        if not isinstance(in_data, list):
            in_data = [0]

        self.data = [i for i in in_data if isinstance(i, (int, float))]

        if not self.data:
            self.data = [0]

    def get_data(self):
        return self.data

    def get_mean(self):
        return np.mean(self.data)

    def get_median(self):
        return np.median(self.data)

    def get_mode(self):
        return sp.mode(self.data)

    def get_variance(self):
        return np.var(self.data)

    def get_standard_deviation(self):
        return np.std(self.data)

    def get_min(self):
        return np.min(self.data)

    def get_max(self):
        return np.max(self.data)
