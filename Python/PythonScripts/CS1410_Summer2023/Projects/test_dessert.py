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
    """
    # Step 1
    dessert_item_test = Candy()
    assert dessert_item_test.name == ""
    assert dessert_item_test.tax_percent == 7.25
    # Step 2
    dessert_item_test = Candy("Test Name", 0, 0, 15.55)
    assert dessert_item_test.name == "Test Name"
    assert dessert_item_test.tax_percent == 15.55
    # Step 3
    dessert_item_test = Candy()
    dessert_item_test.name = "Snickerdoodles"
    dessert_item_test.tax_percent = 0.31
    assert dessert_item_test.name == "Snickerdoodles"
    assert dessert_item_test.tax_percent == 0.31
    # Step 4
    dessert_item_test = Candy("un-modified", 0, 0, 0.00)
    dessert_item_test.name = "Chocolate Chip"
    dessert_item_test.tax_percent = 99.99
    assert dessert_item_test.name == "Chocolate Chip"
    assert dessert_item_test.tax_percent == 99.99
