import pytest
from data_calculator import DataCalculator
import numpy as np
import scipy.stats as sp


def test_data_initialization():
    data = [1, 2, 3, 4, 5]
    calculator = DataCalculator(data)

    assert calculator.get_data() == data
    assert calculator.mean == np.mean(data)
    assert calculator.median == np.median(data)
    assert calculator.mode == sp.mode(data)[0]


def test_data_validation():
    data = [1, 'a', 2.5, 'b']
    calculator = DataCalculator(data)
    assert calculator.get_data() == [1, 2.5]

    # Test with no valid data
    calculator = DataCalculator(['a', 'b'])
    assert calculator.get_data() == [0]


def test_mean_calculation():
    data = [1, 2, 3]
    calculator = DataCalculator(data)
    assert calculator.calculate_mean() == 2.0


def test_median_calculation():
    data = [1, 3, 5]
    calculator = DataCalculator(data)
    assert calculator.calculate_median() == 3.0


def test_mode_calculation():
    data = [1, 1, 2, 2, 2]
    calculator = DataCalculator(data)
    assert calculator.calculate_mode() == 2


def test_variance_calculation():
    data = [1, 2, 3]
    calculator = DataCalculator(data)
    assert calculator.calculate_variance() == np.var(data)


def test_standard_deviation_calculation():
    data = [1, 2, 3]
    calculator = DataCalculator(data)
    assert calculator.calculate_standard_deviation() == np.std(data)


def test_min_max_calculation():
    data = [1, 2, 3]
    calculator = DataCalculator(data)
    assert calculator.calculate_min() == 1
    assert calculator.calculate_max() == 3
