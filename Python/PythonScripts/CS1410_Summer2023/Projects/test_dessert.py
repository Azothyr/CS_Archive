"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_dessert.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
from desserts import *


def test_dessert_item():
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
    dessert_test = Candy()
    assert dessert_test.name == ""
    assert dessert_test.packaging == "Bag"
    assert dessert_test.tax_percent == 7.25
    # Step 2
    dessert_test = Candy("Test Name", 0, 0, "Glass", 15.55)
    assert dessert_test.name == "Test Name"
    assert dessert_test.packaging == "Glass"
    assert dessert_test.tax_percent == 15.55
    # Step 3
    dessert_test = Candy()
    dessert_test.name = "Snicker-doodles"
    dessert_test.packaging = "Bowl"
    dessert_test.tax_percent = 0.31
    assert dessert_test.name == "Snicker-doodles"
    assert dessert_test.packaging == "Bowl"
    assert dessert_test.tax_percent == 0.31
    # Step 4
    dessert_test = Candy("un-modified", 0, 0, None, 0.00)
    dessert_test.name = "Chocolate Chip"
    dessert_test.packaging = "Barn"
    dessert_test.tax_percent = 99.99
    assert dessert_test.name == "Chocolate Chip"
    assert dessert_test.packaging == "Barn"
    assert dessert_test.tax_percent == 99.99
    # Step 5
    dessert_test = Candy("cost_test", 0, 0, None, 0.00)
    assert dessert_test.calculate_cost() == 0
    dessert_test = Candy("cost_test", 1.5, .25)
    assert dessert_test.calculate_cost() == 0.38
    # Step 6
    dessert_test = Candy("tax_test", 0, 0, None, 0.00)
    assert dessert_test.calculate_tax() == 0
    dessert_test = Candy("tax_test", 1.5, .25)
    assert dessert_test.calculate_tax() == 0.03
