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
    5th Testing calculate_cost function
    6th Testing calculate_tax function
    """
    # Step 1
    cookie_test = Cookie()
    assert cookie_test.name == ""
    assert cookie_test.cookie_quantity == 0
    assert cookie_test.price_per_dozen == 0.0
    assert cookie_test.packaging == "Box"
    assert cookie_test.tax_percent == 7.25
    # Step 2
    cookie_test = Cookie("Test Cookie Name", 12, 5.50, "Cup", 2.11)
    assert cookie_test.name == "Test Cookie Name"
    assert cookie_test.cookie_quantity == 12
    assert cookie_test.price_per_dozen == 5.50
    assert cookie_test.packaging == "Cup"
    assert cookie_test.tax_percent == 2.11
    # Step 3
    cookie_test = Cookie()
    cookie_test.name = "Double Fudge"
    cookie_test.cookie_quantity = 15
    cookie_test.price_per_dozen = 15.00
    cookie_test.packaging = "House"
    cookie_test.tax_percent = 8.99
    assert cookie_test.cookie_quantity == 15
    assert cookie_test.name == "Double Fudge"
    assert cookie_test.price_per_dozen == 15.00
    assert cookie_test.packaging == "House"
    assert cookie_test.tax_percent == 8.99
    # Step 4
    cookie_test = Cookie("un-modified", 99, 200.00, None, 0.00)
    cookie_test.name = "Double Fudge"
    cookie_test.cookie_quantity = 24
    cookie_test.price_per_dozen = 12.50
    cookie_test.packaging = "Dog"
    cookie_test.tax_percent = 4.44
    assert cookie_test.name == "Double Fudge"
    assert cookie_test.cookie_quantity == 24
    assert cookie_test.price_per_dozen == 12.50
    assert cookie_test.packaging == "Dog"
    assert cookie_test.tax_percent == 4.44
    # Step 5
    cookie_test = Cookie("cost_test", 0, 0, 0.00)
    assert cookie_test.calculate_cost() == 0
    cookie_test = Cookie("cost_test", 6, 3.99)
    assert cookie_test.calculate_cost() == 2.0
    # Step 6
    cookie_test = Cookie("tax_test", 0, 0, 0.00)
    assert cookie_test.calculate_tax() == 0
    cookie_test = Cookie("tax_test", 6, 3.99)
    assert cookie_test.calculate_tax() == 0.14


def test_combining():
    cookie_test = Cookie("Oatmeal Raisin", 6, 3.45)
    assert cookie_test.can_combine(Cookie("Oatmeal Raisin", 2, 3.45)) is True
    assert cookie_test.can_combine(Cookie("Chocolate Chip", 6, 3.99)) is False
    cookie_test = Cookie("Oatmeal Raisin", 2, 3.45)
    assert cookie_test.can_combine(Cookie("Oatmeal Raisin", 6, 5.55)) is False
