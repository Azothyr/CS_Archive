"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_cookie.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
from desserts import *


def test_cookie():
    """
    Testing superclass DessertItem:
    1st Testing constructor with default values.
    2nd Testing for expected user-input values.
    3rd Testing modifying values from default constructor
    4th Testing modifying values from non-default constructor
    """
    # Step 1
    cookie_test = Cookie()
    assert cookie_test.name == ""
    assert cookie_test.cookie_quantity == 0
    assert cookie_test.price_per_dozen == 0.0
    # Step 2
    cookie_test = Cookie("Test Cookie Name", 12, 5.50)
    assert cookie_test.name == "Test Cookie Name"
    assert cookie_test.cookie_quantity == 12
    assert cookie_test.price_per_dozen == 5.50
    # Step 3
    cookie_test = Cookie()
    cookie_test.name = "Double Fudge"
    assert cookie_test.name == "Double Fudge"
    cookie_test.cookie_quantity = 15
    assert cookie_test.cookie_quantity == 15
    cookie_test.price_per_dozen = 15.00
    assert cookie_test.price_per_dozen == 15.00
    # Step 4
    cookie_test = Cookie("un-modified", 99, 200.00)
    cookie_test.name = "Double Fudge"
    assert cookie_test.name == "Double Fudge"
    cookie_test.cookie_quantity = 24
    assert cookie_test.cookie_quantity == 24
    cookie_test.price_per_dozen = 12.50
    assert cookie_test.price_per_dozen == 12.50
