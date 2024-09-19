from typing import Any
import numpy as np
import scipy.stats as sp
from numpy import floating


class DataCalculator:
    """
    DataCalculator class to analyze data

    Attributes:
        data (list[int | float]): List of data to analyze
        mean (float): Mean of the data
        median (float): Median of the data
        mode (ModeResult): Mode of the data
        variance (float): Variance of the data
        standard_deviation (float): Standard deviation of the data
        min (float): Minimum of the data
        max (float): Maximum of the data

    Methods:
        validate_data(in_data): Validate the data to ensure it is a list of integers or floats
        get_data(): Return the data
        calculate_mean(): Return the mean of the data
        calculate_median(): Return the median of the data
        calculate_mode(): Return the mode of the data
        calculate_variance(): Return the variance of the data
        calculate_standard_deviation(): Return the standard deviation of the data
        calculate_min(): Return the minimum of the data
        calculate_max(): Return the maximum of the data
    """
    def __init__(self, data: list[int | float]):
        """
        Initialize the DataCalculator class

        Parameters:
            data (list[int | float]): List of data to analyze
        """
        self.data = []
        self.validate_data(data)

        self.mean = self.calculate_mean()
        self.median = self.calculate_median()
        self.mode = self.calculate_mode()
        self.variance = self.calculate_variance()
        self.standard_deviation = self.calculate_standard_deviation()
        self.min = self.calculate_min()
        self.max = self.calculate_max()

    def __iter__(self):
        return iter(self.data)

    def validate_data(self, in_data: list[int | float]):
        """
        Validate the data to ensure it is a list of integers or floats

        Parameters:
            in_data (list[int | float]): List of data to validate
        """
        if not isinstance(in_data, list):
            raise ValueError("Input data must be a list")

        self.data = [i for i in in_data if isinstance(i, (int, float))]

        # If no valid data is found, set the data to a list containing 0
        if not self.data:
            self.data = [0]

    def get_data(self) -> list[int | float]:
        """
        Return the data

        Returns:
            list[int | float]: List of data
        """
        return self.data

    def calculate_mean(self) -> floating[Any]:
        """
        Return the mean of the data

        Returns:
            float: Mean of the data
        """
        return np.mean(self.data)

    def calculate_median(self) -> floating[Any]:
        """
        Return the median of the data

        Returns:
            float: Median of the data
        """
        return np.median(self.data)

    def calculate_mode(self) -> sp.mode:
        """
        Return the mode of the data

        Returns:
            ModeResult: Mode of the data
        """
        return sp.mode(self.data)

    def calculate_variance(self) -> floating[Any]:
        """
        Return the variance of the data

        Returns:
            float: Variance of the data
        """
        return np.var(self.data)

    def calculate_standard_deviation(self) -> floating[Any]:
        """
        Return the standard deviation of the data

        Returns:
            float: Standard deviation of the data
        """
        return np.std(self.data)

    def calculate_min(self) -> float:
        """
        Return the minimum of the data

        Returns:
            float: Minimum of the data
        """
        return np.min(self.data)

    def calculate_max(self) -> float:
        """
        Return the maximum of the data

        Returns:
            float: Maximum of the data
        """
        return np.max(self.data)
