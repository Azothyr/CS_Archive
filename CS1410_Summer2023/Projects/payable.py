from enum import Enum
from typing import Protocol


class PayType(Enum):
    CASH = "CASH"
    CARD = "CARD"
    PHONE = "PHONE"


class Payable(Protocol):
    def get_pay_type(self) -> PayType:
        pass

    def set_pay_type(self, payment_method: PayType) -> None:
        pass


class PaymentProcessor:
    def __init__(self):
        self.pay_type: PayType = PayType.CASH

    def __str__(self):
        return f"Paid with {self.pay_type.value}"

    def get_pay_type(self) -> str:
        return self.pay_type.value

    def set_pay_type(self, payment_method: PayType) -> None:
        try:
            if isinstance(payment_method, str):
                payment_method = payment_method.upper()
                if payment_method == "CARD":
                    payment_method = PayType.CARD
                elif payment_method == "CASH":
                    payment_method = PayType.CASH
                elif payment_method == "PHONE":
                    payment_method = PayType.PHONE

            if not isinstance(payment_method, PayType):
                raise ValueError("Invalid payment method.")

            self.pay_type = payment_method
        except (AttributeError, TypeError):
            raise ValueError("Invalid payment method.")