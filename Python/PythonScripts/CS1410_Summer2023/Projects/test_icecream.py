"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_icecream.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
from desserts import *


def test_icecream():
    """
    Testing superclass DessertItem:
    1st Testing constructor with default values.
    2nd Testing for expected user-input values.
    3rd Testing modifying values from default constructor
    4th Testing modifying values from non-default constructor
    5th Testing calculate_cost cus_funcs
    6th Testing calculate_tax cus_funcs
    """
    # Step 1
    icecream_test = IceCream()
    assert icecream_test.name == ""
    assert icecream_test.scoop_count == 0
    assert icecream_test.price_per_scoop == 0.0
    assert icecream_test.packaging == "Bowl"
    assert icecream_test.tax_percent == 7.25
    # Step 2
    icecream_test = IceCream("Test Ice Cream Name", 3, 2.50, "Hands", 3.33)
    assert icecream_test.name == "Test Ice Cream Name"
    assert icecream_test.scoop_count == 3
    assert icecream_test.price_per_scoop == 2.50
    assert icecream_test.packaging == "Hands"
    assert icecream_test.tax_percent == 3.33
    # Step 3
    icecream_test = IceCream()
    icecream_test.name = "Mint Chip"
    icecream_test.scoop_count = 5
    icecream_test.price_per_scoop = 0.75
    icecream_test.packaging = "Floor"
    icecream_test.tax_percent = 19.99
    assert icecream_test.name == "Mint Chip"
    assert icecream_test.scoop_count == 5
    assert icecream_test.price_per_scoop == 0.75
    assert icecream_test.packaging == "Floor"
    assert icecream_test.tax_percent == 19.99
    # Step 4
    icecream_test = IceCream("un-modified", 9, 0.50, None, 15.00)
    icecream_test.name = "Rainbow Cheese Cake"
    icecream_test.scoop_count = 1
    icecream_test.price_per_scoop = 1.11
    icecream_test.packaging = "Table"
    icecream_test.tax_percent = 0.22
    assert icecream_test.name == "Rainbow Cheese Cake"
    assert icecream_test.scoop_count == 1
    assert icecream_test.price_per_scoop == 1.11
    assert icecream_test.packaging == "Table"
    assert icecream_test.tax_percent == 0.22
    # Step 5
    icecream_test = IceCream("cost_test", 0, 0, 0.00)
    assert icecream_test.calculate_cost() == 0
    icecream_test = IceCream("cost_test", 2, .79)
    assert icecream_test.calculate_cost() == 1.58
    # Step 6
    icecream_test = IceCream("tax_test", 0, 0, 0.00)
    assert icecream_test.calculate_tax() == 0
    icecream_test = IceCream("tax_test", 2, .79)
    assert icecream_test.calculate_tax() == 0.11
