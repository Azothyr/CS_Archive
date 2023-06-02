from desserts import *
from receipt import make_receipt


class Order:
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

    def order_cost(self):
        total_cost = 0.00
        for item in self.order_list:
            total_cost += item.calculate_cost()
        return total_cost

    def order_tax(self):
        total_tax = 0
        for item in self.order_list:
            total_tax += item.calculate_tax()
        return total_tax


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
    receipt_list = [["Name", "Item Cost", "Tax"]]

    my_order = Order()
    for order in order_list:
        my_order.add(order)
    cost_subtotal = 0
    tax_subtotal = 0
    for item in my_order:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        cost_subtotal += cost
        tax_subtotal += tax
        receipt_list.append([item.name, "${:.2f}".format(cost), "${:.2f}".format(tax)])
    receipt_list.append(["--------------------------------------------------------", "", ""])
    receipt_list.append(["Order Subtotals", "${:.2f}".format(cost_subtotal), "${:.2f}".format(tax_subtotal)])
    receipt_list.append(["Order Total", "", "${:.2f}".format(cost_subtotal + tax_subtotal)])
    receipt_list.append(["Total items in the order", "", len(my_order)])

    make_receipt(receipt_list, "receipt.pdf")


if __name__ == "__main__":
    main()
