"""
***THIS FILE MUST BE RUN IN THE TERMINAL USING THE PYTEST MODULE, RUN: python -m pytest test_order.py***
IF the file is not run this way, the desired out may not be what is expected.
Expected Output: 100% tests passed
"""
import pytest
from payable import *
from dessertshop import Order
from desserts import *


def test_order_sort():
    order_test = Order()
    order_test.add(Candy("Candy Corn", 1, 2))
    order_test.add(Candy("Gummy Bears", 1, 8))
    order_test.add(Cookie("Chocolate Chip", 1, 4))
    order_test.add(IceCream("Pistachio", 1, 9))
    order_test.add(Sundae("Vanilla", 1, 10, "Hot Fudge", 0))
    order_test.add(Cookie("Oatmeal Raisin", 1, 3))
    order_test.sort()
    expected_result = "Oatmeal Raisin Cookie (Box), 1 cookies, $3.00/dozen, $0.25, $0.02\n" \
                      "Chocolate Chip Cookie (Box), 1 cookies, $4.00/dozen, $0.33, $0.02\n" \
                      "Candy Corn Candy (Bag), 1.0lbs, $2.00/lb, $2.00, $0.14\n" \
                      "Gummy Bears Candy (Bag), 1.0lbs, $8.00/lb, $8.00, $0.58\n" \
                      "Pistachio IceCream (Bowl), 1 scoops, $9.00/scoop, $9.00, $0.65\n" \
                      "Hot Fudge Vanilla Sundae (Boat), 1 scoops, $10.00/scoop:, $10.00, $0.72\n" \
                      "Hot Fudge topping, 1, , , $0.00"
    assert str(order_test) == expected_result


def test_default_payable():
    pay_test = PaymentProcessor()
    assert pay_test.pay_type.value == "CASH"
    assert pay_test.pay_type == PayType.CASH


def test_get_set_pay_type():
    pay_test = PaymentProcessor()
    pay_test.set_pay_type(PayType.PHONE)
    assert pay_test.pay_type == PayType.PHONE
    assert pay_test.pay_type.value == "PHONE"
    assert pay_test.get_pay_type() == "PHONE"
    pay_test.set_pay_type(PayType.CARD)
    assert pay_test.pay_type == PayType.CARD
    assert pay_test.get_pay_type() == "CARD"
    assert pay_test.pay_type.value == "CARD"
    pay_test.set_pay_type(PayType.CASH)
    assert pay_test.pay_type == PayType.CASH
    assert pay_test.pay_type.value == "CASH"
    assert pay_test.get_pay_type() == "CASH"
    with pytest.raises(ValueError):
        try:
            pay_test.set_pay_type(PayType.cash)
        except AttributeError:
            raise ValueError("Invalid payment method.")
