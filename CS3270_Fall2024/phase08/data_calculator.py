import logging as log
from tqdm import tqdm
from timer import function_timer
from typing import Any
from numpy import ndarray, floating, mean, median, var, std
from scipy.stats import mode


class DataCalculator:
    """
    DataCalculator class to analyze data

    Attributes:
        analysis_time (float): Time taken to perform the analysis

    Properties:
        data (list[int | float]): List of data to analyze
        mean (float): Mean of the data
        median (float): Median of the data
        mode (ndarray): Mode of the data
        variance (float): Variance of the data
        standard_deviation (float): Standard deviation of the data
        min (float): Minimum value of the data
        max (float): Maximum value of the data

    Methods:
        __init__(data: list[int | float]): Initialize the DataCalculator class
        __iter__(): Return an iterator for the data
        __len__(): Return the length of the data
        __add__(other): Add two DataCalculator instances
        get_data(): Return the data
        _validate_data(in_data: list[int | float]): Validate the data
        _perform_analysis(): Perform the analysis on the data
        _calculate_mean(): Calculate the mean of the data
        _calculate_median(): Calculate the median of the data
        _calculate_mode(): Calculate the mode of the data
        _calculate_variance(): Calculate the variance of the data
        _calculate_standard_deviation(): Calculate the standard deviation of the data
        _calculate_min(): Calculate the minimum value of the data
        _calculate_max(): Calculate the maximum value of the data
    """

    def __init__(self, data: list[int | float]):
        """
        Initialize the DataCalculator class

        Parameters:
            data (list[int | float]): List of data to analyze
        """
        self._data: list[int | float] = []
        self._mean: floating[Any]
        self._median: floating[Any]
        self._mode: ndarray
        self._variance: floating[Any]
        self._standard_deviation: floating[Any]
        self._min: float
        self._max: float

        self.analysis_time = None

        self._validate_data(data)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        return DataCalculator(self.data + other.data)

    def get_data(self) -> list[int | float]:
        return self.data

    @property
    def data(self) -> list[int | float]:
        return self._data

    @data.setter
    def data(self, value: list[int | float]):
        self._validate_data(value)

    def _validate_data(self, in_data: list[int | float]):
        """
        Validate the data to ensure it is a list of integers or floats

        Parameters:
            in_data (list[int | float]): List of data to validate
        """
        if not isinstance(in_data, list):
            raise ValueError("Input data must be a list")

        temp = [i for i in in_data if isinstance(i, (int, float))]
        if len(temp) != len(in_data):
            log.warning("Invalid data found. Only integers and floats are allowed. Skipping invalid data.")

        # If no valid data is found, set the data to a list containing 0
        self._data = temp if temp else []
        self._perform_analysis()

    @function_timer(timer_attr='analysis_time')
    def _perform_analysis(self):
        """
        Perform the analysis on the data
        """
        if not self.data:
            self._mean = None
            self._median = None
            self._mode = None
            self._variance = None
            self._standard_deviation = None
            self._min = None
            self._max = None
        else:
            tasks = {
                "_mean": self._calculate_mean,
                "_median": self._calculate_median,
                "_mode": self._calculate_mode,
                "_variance": self._calculate_variance,
                "_standard_deviation": self._calculate_standard_deviation,
                "_min": self._calculate_min,
                "_max": self._calculate_max
            }

            with tqdm(total=len(tasks), desc="Calculating statistics", colour="green",
                      bar_format="{desc}: {percentage:3.0f}% |{bar}| {n:.0f}/{total:.0f}") as progress:
                for task, func in tasks.items():
                    setattr(self, task, func())
                    progress.update(1)

    @property
    def mean(self) -> floating[Any]:
        return self._mean

    @property
    def median(self) -> floating[Any]:
        return self._median

    @property
    def mode(self) -> ndarray:
        return self._mode

    @property
    def variance(self) -> floating[Any]:
        return self._variance

    @property
    def standard_deviation(self) -> floating[Any]:
        return self._standard_deviation

    @property
    def min(self) -> float:
        return self._min

    @property
    def max(self) -> float:
        return self._max

    def _calculate_mean(self) -> floating[Any]:
        return mean(self.data) if self.data else ndarray([])

    def _calculate_median(self) -> floating[Any]:
        return median(self.data) if self.data else ndarray([])

    def _calculate_mode(self) -> ndarray:
        if self.data:
            return ndarray([])
        modes = mode(self.data)
        modes = modes[0] if len(modes) == 1 else ndarray(modes)
        return modes

    def _calculate_variance(self) -> floating[Any]:
        return var(self.data) if self.data else ndarray([])

    def _calculate_standard_deviation(self) -> floating[Any]:
        return std(self.data) if self.data else ndarray([])

    def _calculate_min(self) -> float:
        return min(self.data) if self.data else ndarray([])

    def _calculate_max(self) -> float:
        return max(self.data) if self.data else ndarray([])
