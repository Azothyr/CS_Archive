"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_sundae.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
from desserts import *


def test_sundae():
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
    sundae_test = Sundae()
    assert sundae_test.name == ""
    assert sundae_test.scoop_count == 0
    assert sundae_test.price_per_scoop == 0.0
    assert sundae_test.topping_name == ""
    assert sundae_test.topping_price == 0.0
    assert sundae_test.packaging == "Boat"
    assert sundae_test.tax_percent == 7.25
    # Step 2
    sundae_test = Sundae("Test Sundae Name", 3, 2.50, "Test Topping", 0.50, "Hat", 1.11)
    assert sundae_test.name == "Test Sundae Name"
    assert sundae_test.scoop_count == 3
    assert sundae_test.price_per_scoop == 2.50
    assert sundae_test.topping_name == "Test Topping"
    assert sundae_test.topping_price == 0.50
    assert sundae_test.packaging == "Hat"
    assert sundae_test.tax_percent == 1.11
    # Step 3
    sundae_test = Sundae()
    sundae_test.name = "Banana Split"
    sundae_test.scoop_count = 3
    sundae_test.price_per_scoop = 2.30
    sundae_test.topping_name = "Banana"
    sundae_test.topping_price = 3.25
    sundae_test.packaging = "Cat"
    sundae_test.tax_percent = 5.99
    assert sundae_test.name == "Banana Split"
    assert sundae_test.scoop_count == 3
    assert sundae_test.price_per_scoop == 2.30
    assert sundae_test.topping_name == "Banana"
    assert sundae_test.topping_price == 3.25
    assert sundae_test.packaging == "Cat"
    assert sundae_test.tax_percent == 5.99
    # Step 4
    sundae_test = Sundae("un-modified", 1, 5.00, "unmodified", 0.25, None, 0.01)
    sundae_test.name = "Ras-Fudge Split"
    sundae_test.scoop_count = 5
    sundae_test.price_per_scoop = 5.10
    sundae_test.topping_name = "Sprinkles"
    sundae_test.topping_price = 4.00
    sundae_test.packaging = "Sword"
    sundae_test.tax_percent = 25.00
    assert sundae_test.name == "Ras-Fudge Split"
    assert sundae_test.scoop_count == 5
    assert sundae_test.price_per_scoop == 5.10
    assert sundae_test.topping_name == "Sprinkles"
    assert sundae_test.topping_price == 4.00
    assert sundae_test.packaging == "Sword"
    assert sundae_test.tax_percent == 25.00
    # Step 5
    sundae_test = Sundae("cost_test", 0, 0, 0.00)
    assert sundae_test.calculate_cost() == 0
    sundae_test = Sundae("cost_test", 3, .69, "Hot Fudge", 1.29)
    assert sundae_test.calculate_cost() == 3.36
    # Step 6
    sundae_test = Sundae("tax_test", 0, 0, 0.00)
    assert sundae_test.calculate_tax() == 0
    sundae_test = Sundae("tax_test", 3, .69, "Hot Fudge", 1.29)
    assert sundae_test.calculate_tax() == 0.24
