"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_customer.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
import pytest
from dessertshop import Customer


def test_default_customer():
    Customer.id_counter = 0
    customer_test = Customer()
    assert customer_test.customer_name == ""
    assert customer_test.id == 0
    assert customer_test.order_history == []


def test_modify_customer():
    Customer.id_counter = 0
    modify_test = Customer("Jack Sparrow")
    assert modify_test.customer_name == "Jack Sparrow"
    assert modify_test.id == 0
    assert modify_test.order_history == []
    modify_test = Customer("Alpha")
    assert modify_test.customer_name == "Alpha"
    assert modify_test.id == 1
    assert modify_test.order_history == []
    modify_test.customer_name = "Beta"
    modify_test.id = 10110111
    modify_test.order_history = ["1", "2", "3", "4"]
    assert modify_test.customer_name == "Beta"
    assert modify_test.id == 10110111
    assert modify_test.order_history == ["1", "2", "3", "4"]


def test_id_update():
    Customer.id_counter = 0
    id_test = Customer()
    assert id_test.id == 0
    id_test = Customer()
    assert id_test.id == 1
    id_test = Customer()
    assert id_test.id == 2
    id_test = Customer()
    assert id_test.id == 3
    with pytest.raises(AssertionError):
        assert id_test.id == 1
