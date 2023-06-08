"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_customer.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
import pytest
from dessertshop import Customer


def test_default_customer():
    customer_test = Customer()
    assert customer_test.customer_name == ""
    assert customer_test.customer_id == 0
    assert customer_test.order_history == []


def test_modify_customer():
    customer_test = Customer("Jack Sparrow")
    assert customer_test.customer_name == "Jack Sparrow"
    assert customer_test.customer_id == 0
    assert customer_test.order_history == []
    customer_test = Customer("Alpha")
    assert customer_test.customer_name == "Alpha"
    assert customer_test.customer_id == 0
    assert customer_test.order_history == []
    customer_test.customer_name = "Beta"
    customer_test.customer_id = 10110111
    customer_test.order_history = ["1", "2", "3", "4"]
    assert customer_test.customer_name == "Beta"
    assert customer_test.customer_id == 10110111
    assert customer_test.order_history == ["1", "2", "3", "4"]
