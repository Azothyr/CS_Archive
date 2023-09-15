import pytest
from ..functions.math_funcs import calculate_geometric_progression as calc_geo_progress


@pytest.mark.parametrize(
    "initial_value, num_iterations, ratio, expected",
    [
        (100, 12, 2, [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800]),
        (0, 5, 2, [0, 0, 0, 0, 0]),
        (100, 5, 0, [100, 0, 0, 0, 0])

    ],
    ids=[
        "Test geometric progression with base 100, iterations 12, and ratio 2",
        "Test geometric progression with base 0, iterations 5, and ratio 2",
        "Test geometric progression with base 100, iterations 5, and ratio 0"
    ]
)
def test_geometric_progression(initial_value, num_iterations, ratio, expected):
    result = calc_geo_progress(initial_value, num_iterations, ratio)
    assert result == expected
