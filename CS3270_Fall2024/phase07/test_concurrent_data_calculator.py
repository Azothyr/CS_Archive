import pytest
from concurrent_data_calculator import ConcurrentDataCalculator


@pytest.fixture
def small_data():
    return list(range(1000))


@pytest.fixture
def large_data():
    return list(range(10_000_000))


def test_small_data_analysis(small_data):
    calc = ConcurrentDataCalculator(small_data)
    assert calc.mean is not None
    assert calc.median is not None


def test_large_data_analysis(large_data):
    calc = ConcurrentDataCalculator(large_data)
    assert calc.mean is not None
    assert calc.median is not None


def test_threshold_behavior(small_data):
    calc = ConcurrentDataCalculator(small_data)
    assert len(calc.data) < ConcurrentDataCalculator.concurrency_threshold
    calc._perform_analysis()