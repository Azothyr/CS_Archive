from abc import ABC, abstractmethod
from packaging import Packaging


class DessertItem(ABC, Packaging):
    def __init__(self, name="", packaging=None, tax_percent=7.25):
        super().__init__(packaging)
        self.name = str(name)
        self.packaging = packaging
        self.tax_percent = float(tax_percent)

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def calculate_tax(self):
        cost = self.calculate_cost()
        tax = round(cost * round(self.tax_percent / 100, 5), 2)
        return tax


class Candy(DessertItem):
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0, packaging="Bag", tax_percent=7.25):
        super().__init__(name, packaging, tax_percent)
        self.candy_weight = float(candy_weight)
        self.price_per_pound = float(price_per_pound)
        self.packaging = str(packaging)
        self.__name__ = f"{self.name} Candy ({self.packaging})"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.candy_weight}lbs"
        price = "${:.2f}".format(self.price_per_pound) + "/lb"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {quantity}, {price}, {item_cost}, {item_tax}"

    def calculate_cost(self):
        cost = round(self.candy_weight * self.price_per_pound, 2)
        return cost


class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0, packaging="Box", tax_percent=7.25):
        super().__init__(name, packaging, tax_percent)
        self.cookie_quantity = int(cookie_quantity)
        self.price_per_dozen = float(price_per_dozen)
        self.packaging = str(packaging)
        self.__name__ = f"{self.name} Cookie ({self.packaging})"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.cookie_quantity} cookies"
        price = "${:.2f}".format(self.price_per_dozen) + "/dozen"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {quantity}, {price}, {item_cost}, {item_tax}"

    def calculate_cost(self):
        cost = round(round(self.price_per_dozen / 12, 5) * self.cookie_quantity, 2)
        return cost


class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0, packaging="Bowl", tax_percent=7.25):
        super().__init__(name, packaging, tax_percent)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)
        self.packaging = str(packaging)
        self.__name__ = f"{self.name} IceCream ({self.packaging})"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.scoop_count} scoops"
        price = "${:.2f}".format(self.price_per_scoop) + "/scoop"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {quantity}, {price}, {item_cost}, {item_tax}"

    def calculate_cost(self):
        cost = round(self.price_per_scoop * self.scoop_count, 2)
        return cost


class Sundae(IceCream):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0,
                 topping_name="", topping_price=0.0, packaging="Boat", tax_percent=7.25):
        super().__init__(name, scoop_count, price_per_scoop, packaging, tax_percent)
        self.topping_name = str(topping_name)
        self.topping_price = float(topping_price)
        self.packaging = str(packaging)
        self.__name__ = f"{self.topping_name} {self.name} Sundae ({self.packaging})"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.scoop_count} scoops"
        price = "${:.2f}".format(self.price_per_scoop) + "/scoop:"
        topping = f"{self.topping_name} topping"
        topping_price = "${:.2f}".format(self.topping_price)
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {quantity}, {price}, {item_cost}, {item_tax}\n{topping}, 1, {topping_price}"

    def calculate_cost(self):
        cost = round(self.price_per_scoop * self.scoop_count + self.topping_price, 2)
        return cost
