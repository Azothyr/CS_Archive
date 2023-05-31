class DessertItem:
    def __init__(self, name=""):
        self.name = str(name)


class Candy(DessertItem):
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.candy_weight = float(candy_weight)
        self.price_per_pound = float(price_per_pound)


class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.cookie_quantity = int(cookie_quantity)
        self.price_per_dozen = float(price_per_dozen)


class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)


class Sundae(IceCream):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0, topping_name="", topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = str(topping_name)
        self.topping_price = float(topping_price)
