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
    """
    # Step 1
    ice_cream_test = IceCream()
    assert ice_cream_test.name == ""
    assert ice_cream_test.scoop_count == 0
    assert ice_cream_test.price_per_scoop == 0.0
    # Step 2
    ice_cream_test = IceCream("Test Ice Cream Name", 3, 2.50)
    assert ice_cream_test.name == "Test Ice Cream Name"
    assert ice_cream_test.scoop_count == 3
    assert ice_cream_test.price_per_scoop == 2.50
    # Step 3
    ice_cream_test = IceCream()
    ice_cream_test.name = "Mint Chip"
    assert ice_cream_test.name == "Mint Chip"
    ice_cream_test.scoop_count = 5
    assert ice_cream_test.scoop_count == 5
    ice_cream_test.price_per_scoop = 0.75
    assert ice_cream_test.price_per_scoop == 0.75
    # Step 4
    ice_cream_test = IceCream("un-modified", 9, 0.50)
    ice_cream_test.name = "Rainbow Cheese Cake"
    assert ice_cream_test.name == "Rainbow Cheese Cake"
    ice_cream_test.scoop_count = 1
    assert ice_cream_test.scoop_count == 1
    ice_cream_test.price_per_scoop = 1.11
    assert ice_cream_test.price_per_scoop == 1.11
