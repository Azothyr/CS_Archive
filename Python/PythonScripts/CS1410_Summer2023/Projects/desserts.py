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

    def __eq__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() == other.calculate_cost()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() != other.calculate_cost()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() < other.calculate_cost()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() > other.calculate_cost()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() >= other.calculate_cost()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() <= other.calculate_cost()
        return NotImplemented

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
        self.__name__ = f"{self.name} {self.__class__.__name__}"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.candy_weight} lbs"
        price = "${:.2f}".format(self.price_per_pound) + "/lb"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {self.packaging}, {quantity}, {price}, {item_cost}, {item_tax}"

    def __repr__(self):
        name = self.__name__
        quantity = f"{self.candy_weight} lbs."
        price = "${:.2f}".format(self.price_per_pound) + "/lb."
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())

        representation = f"{name} ({self.packaging}) {quantity} @ {price}:" \
                         f" {item_cost} [Tax: {item_tax}]"
        return representation

    def calculate_cost(self):
        cost = round(self.candy_weight * self.price_per_pound, 2)
        return cost

    def can_combine(self, other: "Candy") -> bool:
        if isinstance(other, Candy):
            return (self.name, self.price_per_pound) == (other.name, other.price_per_pound)
        return False

    def combine(self, other: "Candy") -> "Candy":
        if self.can_combine(other):
            self.candy_weight += other.candy_weight
        return self


class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0, packaging="Box", tax_percent=7.25):
        super().__init__(name, packaging, tax_percent)
        self.cookie_quantity = int(cookie_quantity)
        self.price_per_dozen = float(price_per_dozen)
        self.packaging = str(packaging)
        self.__name__ = f"{self.name} {self.__class__.__name__}"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.cookie_quantity} cookies"
        price = "${:.2f}".format(self.price_per_dozen) + "/dozen"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {self.packaging}, {quantity}, {price}, {item_cost}, {item_tax}"

    def __repr__(self):
        name = self.__name__
        quantity = f"{self.cookie_quantity} cookies"
        price = "${:.2f}".format(self.price_per_dozen) + "/dozen"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())

        representation = f"{name} ({self.packaging}) {quantity} @ {price}:" \
                         f" {item_cost} [Tax: {item_tax}]"
        return representation

    def calculate_cost(self):
        cost = round(round(self.price_per_dozen / 12, 5) * self.cookie_quantity, 2)
        return cost

    def can_combine(self, other: "Cookie") -> bool:
        if isinstance(other, Cookie):
            return (self.name, self.price_per_dozen) == (other.name, other.price_per_dozen)
        return False

    def combine(self, other: "Cookie") -> "Cookie":
        if self.can_combine(other):
            self.cookie_quantity += other.cookie_quantity
            return self


class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0, packaging="Bowl", tax_percent=7.25):
        super().__init__(name, packaging, tax_percent)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)
        self.packaging = str(packaging)
        self.__name__ = f"{self.name} {self.__class__.__name__}"

    def __str__(self):
        name = self.__name__
        quantity = f"{self.scoop_count} scoops"
        price = "${:.2f}".format(self.price_per_scoop) + "/scoop"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{name}, {self.packaging}, {quantity}, {price}, {item_cost}, {item_tax}"

    def __repr__(self):
        name = self.__name__
        quantity = f"{self.scoop_count} scoops"
        price = "${:.2f}".format(self.price_per_scoop) + "/scoop"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())

        representation = f"{name} ({self.packaging}) {quantity} @ {price}:" \
                         f" {item_cost} [Tax: {item_tax}]"
        return representation

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
        self.__name__ = f"{self.name} {self.__class__.__name__} with {self.topping_name}"

    def __str__(self):
        quantity = f"{self.scoop_count} scoops"
        price = "${:.2f}".format(self.price_per_scoop) + "/scoop:"
        topping = f"{self.topping_name} (Topping)"
        topping_price = "${:.2f}".format(self.topping_price)
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())
        return f"{self.__name__}, {self.packaging}, {quantity}, {price}, {item_cost}, {item_tax}\n" \
               f"{topping}, , , , {topping_price}"

    def __repr__(self):
        quantity = f"{self.scoop_count} scoops"
        price = "${:.2f}".format(self.price_per_scoop) + "/scoop:"
        item_cost = "${:.2f}".format(self.calculate_cost())
        item_tax = "${:.2f}".format(self.calculate_tax())

        representation = f"{self.__name__} ({self.packaging}) {quantity} @ {price}:" \
                         f" {item_cost} [Tax: {item_tax}]"
        return representation

    def calculate_cost(self):
        cost = round(self.price_per_scoop * self.scoop_count + self.topping_price, 2)
        return cost
