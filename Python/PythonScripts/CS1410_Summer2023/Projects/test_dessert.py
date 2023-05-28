"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_dessert.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
from dessert import *


def test_dessert_item():
    """
    Testing superclass DessertItem:
    1st Testing constructor with default values.
    2nd Testing for expected user-input values.
    3rd Testing modifying values from default constructor
    4th Testing modifying values from non-default constructor
    """
    # Step 1
    dessert_item_test = DessertItem()
    assert dessert_item_test.name == ""
    # Step 2
    dessert_item_test = DessertItem("Test Name")
    assert dessert_item_test.name == "Test Name"
    # Step 3
    dessert_item_test = DessertItem()
    dessert_item_test.name = "Snickerdoodles"
    assert dessert_item_test.name == "Snickerdoodles"
    # Step 4
    dessert_item_test = DessertItem("un-modified")
    dessert_item_test.name = "Chocolate Chip"
    assert dessert_item_test.name == "Chocolate Chip"




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


def test_sundae():
    """
    Testing superclass DessertItem:
    1st Testing constructor with default values.
    2nd Testing for expected user-input values.
    3rd Testing modifying values from default constructor
    4th Testing modifying values from non-default constructor
    """
    # Step 1
    sundae_test = Sundae()
    assert sundae_test.name == ""
    assert sundae_test.scoop_count == 0
    assert sundae_test.price_per_scoop == 0.0
    assert sundae_test.topping_name == ""
    assert sundae_test.topping_price == 0.0
    # Step 2
    sundae_test = Sundae("Test Sundae Name", 3, 2.50, "Test Topping", 0.50)
    assert sundae_test.name == "Test Sundae Name"
    assert sundae_test.scoop_count == 3
    assert sundae_test.price_per_scoop == 2.50
    assert sundae_test.topping_name == "Test Topping"
    assert sundae_test.topping_price == 0.50
    # Step 3
    sundae_test = Sundae()
    sundae_test.name = "Banana Split"
    assert sundae_test.name == "Banana Split"
    sundae_test.scoop_count = 3
    assert sundae_test.scoop_count == 3
    sundae_test.price_per_scoop = 2.30
    assert sundae_test.price_per_scoop == 2.30
    sundae_test.topping_name = "Banana"
    assert sundae_test.topping_name == "Banana"
    sundae_test.topping_price = 3.25
    assert sundae_test.topping_price == 3.25
    # Step 4
    sundae_test = Sundae("un-modified", 1, 5.00, "unmodified", 0.25)
    sundae_test.name = "Ras-Fudge Split"
    assert sundae_test.name == "Ras-Fudge Split"
    sundae_test.scoop_count = 5
    assert sundae_test.scoop_count == 5
    sundae_test.price_per_scoop = 5.10
    assert sundae_test.price_per_scoop == 5.10
    sundae_test.topping_name = "Sprinkles"
    assert sundae_test.topping_name == "Sprinkles"
    sundae_test.topping_price = 4.00
    assert sundae_test.topping_price == 4.00
