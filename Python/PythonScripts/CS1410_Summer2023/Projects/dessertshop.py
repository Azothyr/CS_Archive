from desserts import *


class Order:
    """
    order: list of DessertItem objects
    A constructor that creates an empty Order
    add() method that takes a single DessertItem argument and adds it to the order list
    """
    def __init__(self, order_list=[]):
        self.order_list = order_list

    def __len__(self):
        return len(self.order_list)

    def __iter__(self):
        return iter(self.order_list)

    def __next__(self):
        return next(iter(self.order_list))

    def add(self, dessert_item: DessertItem = None):
        if not isinstance(dessert_item, DessertItem):
            raise ValueError("Error: Item to add is not a DessertItem")
        self.order_list.append(dessert_item)


def main():
    """
    Main function.
    """
    order_list = [Candy("Candy Corn", 1.5, .25),
                  Candy("Gummy Bears", .25, .35),
                  Cookie("Chocolate Chip", 6, 3.99),
                  IceCream("Pistachio", 2, .79),
                  Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29),
                  Cookie("Oatmeal Raisin", 2, 3.45)]

    my_order = Order()
    for order in order_list:
        my_order.add(order)
    for item in my_order:
        print(item.name)
    length = len(my_order)
    print(f"Total number of items in order: {length}")


if __name__ == "__main__":
    main()
