from abc import ABC, abstractmethod


class DessertItem(ABC):
    def __init__(self, name="", tax_percent=7.25):
        self.name = str(name)
        self.tax_percent = float(tax_percent)

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        cost = self.calculate_cost()
        tax = round(cost * round(self.tax_percent / 100, 5), 2)
        return tax


class Candy(DessertItem):
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self.candy_weight = float(candy_weight)
        self.price_per_pound = float(price_per_pound)

    def calculate_cost(self):
        cost = round(self.candy_weight * self.price_per_pound, 2)
        return cost


class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self.cookie_quantity = int(cookie_quantity)
        self.price_per_dozen = float(price_per_dozen)

    def calculate_cost(self):
        cost = round(round(self.price_per_dozen / 12, 5) * self.cookie_quantity, 2)
        return cost


class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)

    def calculate_cost(self):
        cost = round(self.price_per_scoop * self.scoop_count, 2)
        return cost


class Sundae(IceCream):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0,
                 topping_name="", topping_price=0.0, tax_percent=7.25):
        super().__init__(name, scoop_count, price_per_scoop, tax_percent)
        self.topping_name = str(topping_name)
        self.topping_price = float(topping_price)

    def calculate_cost(self):
        cost = round(self.price_per_scoop * self.scoop_count + self.topping_price, 2)
        return cost
