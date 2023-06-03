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
    5th Testing calculate_cost function
    6th Testing calculate_tax function
    """
    # Step 1
    candy_test = Candy()
    assert candy_test.name == ""
    assert candy_test.candy_weight == 0.0
    assert candy_test.price_per_pound == 0.0
    assert candy_test.packaging == "Bag"
    assert candy_test.tax_percent == 7.25
    # Step 2
    candy_test = Candy("Test Candy Name", 1.5, 0.25, "Fountain", 3.11)
    assert candy_test.name == "Test Candy Name"
    assert candy_test.candy_weight == 1.5
    assert candy_test.price_per_pound == 0.25
    assert candy_test.packaging == "Fountain"
    assert candy_test.tax_percent == 3.11
    # Step 3
    candy_test = Candy()
    candy_test.name = "Taffy"
    candy_test.candy_weight = 2.2
    candy_test.price_per_pound = 5.00
    candy_test.packaging = "Mouth"
    candy_test.tax_percent = 5.33
    assert candy_test.name == "Taffy"
    assert candy_test.candy_weight == 2.2
    assert candy_test.price_per_pound == 5.00
    assert candy_test.packaging == "Mouth"
    assert candy_test.tax_percent == 5.33
    # Step 4
    candy_test = Candy("un-modified", 200.00, 10, "Tray", 1500.00)
    candy_test.name = "Nerds"
    candy_test.candy_weight = 0.30
    candy_test.price_per_pound = 1.25
    candy_test.packaging = "Plate"
    candy_test.tax_percent = 9.99
    assert candy_test.name == "Nerds"
    assert candy_test.candy_weight == 0.30
    assert candy_test.price_per_pound == 1.25
    assert candy_test.packaging == "Plate"
    assert candy_test.tax_percent == 9.99
    # Step 5
    candy_test = Candy("cost_test", 0, 0, 0.00)
    assert candy_test.calculate_cost() == 0
    candy_test = Candy("cost_test", .25, .35)
    assert candy_test.calculate_cost() == 0.09
    # Step 6
    candy_test = Candy("tax_test", 0, 0, 0.00)
    assert candy_test.calculate_tax() == 0
    candy_test = Candy("tax_test", .25, .35)
    assert candy_test.calculate_tax() == 0.01
