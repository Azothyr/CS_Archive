"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_candy.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
from desserts import *


def test_candy():
    """
    Testing superclass DessertItem:
    1st Testing constructor with default values.
    2nd Testing for expected user-input values.
    3rd Testing modifying values from default constructor
    4th Testing modifying values from non-default constructor
    """
    # Step 1
    candy_test = Candy()
    assert candy_test.name == ""
    assert candy_test.candy_weight == 0.0
    assert candy_test.price_per_pound == 0.0
    # Step 2
    candy_test = Candy("Test Candy Name", 1.5, 0.25)
    assert candy_test.name == "Test Candy Name"
    assert candy_test.candy_weight == 1.5
    assert candy_test.price_per_pound == 0.25
    # Step 3
    candy_test = Candy()
    candy_test.name = "Taffy"
    assert candy_test.name == "Taffy"
    candy_test.candy_weight = 2.2
    assert candy_test.candy_weight == 2.2
    candy_test.price_per_pound = 5.00
    assert candy_test.price_per_pound == 5.00
    # Step 4
    candy_test = Candy("un-modified", 200.00, 1500.00)
    candy_test.name = "Nerds"
    assert candy_test.name == "Nerds"
    candy_test.candy_weight = 0.30
    assert candy_test.candy_weight == 0.30
    candy_test.price_per_pound = 1.25
    assert candy_test.price_per_pound == 1.25
