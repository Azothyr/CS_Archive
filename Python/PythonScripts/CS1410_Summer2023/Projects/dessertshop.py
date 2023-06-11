from desserts import *
from receipt import make_receipt
from payable import *
from combine import Combinable


class Order:
    def __init__(self, order_list: list[DessertItem] = None):
        self.order_list = order_list or []

    def __str__(self):
        items_str = "\n".join(str(item) for item in self.order_list)
        return items_str

    def __repr__(self):
        items_str = "\n".join(str(item) for item in self.order_list)
        return items_str

    def __len__(self):
        return len(self.order_list)

    def __iter__(self):
        return iter(self.order_list)

    def __next__(self):
        return next(iter(self.order_list))

    def add(self, dessert_item: DessertItem = None):
        if isinstance(dessert_item, Combinable):
            for item in self.order_list:
                if hasattr(item, 'can_combine') and item.can_combine(dessert_item):
                    item.combine(dessert_item)
                    return
        if not isinstance(dessert_item, DessertItem):
            raise ValueError("Error: Item to add is not a DessertItem")
        self.order_list.append(dessert_item)

    def sort(self):
        self.order_list = sorted(self.order_list, key=lambda item: item.calculate_cost())

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


class Customer:
    id_counter = 1000

    def __init__(self, customer_name: str = ""):
        self.customer_name = customer_name
        self.order_history: list[Order] = []
        self.id: int = Customer.id_counter
        Customer.id_counter += 1

    def add2history(self, order: Order) -> "Customer":
        self.order_history.append(order)
        return self


class DessertShop:
    def __init__(self, customer_db: dict[str, Customer] = None):
        self.dessert_class = DessertItem
        self.customer_db = customer_db or {}

    def gather_input(self, dessert_type):
        bad_name_char = ("(", ")", "!", "@", "#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        dessert_class = self.dessert_class

        class InvalidInputError(Exception):
            """Exception raised for invalid input errors."""
            pass

        def get_dessert_input(prompt_func, error, only_letters=False, must_positive=False):
            while True:
                try:
                    user_input = prompt_func()
                    if only_letters:
                        if any(char in user_input for char in bad_name_char):
                            raise InvalidInputError(f"Input must be only letters. Try again.")
                        break
                    elif must_positive:
                        if user_input <= 0:
                            raise InvalidInputError("Weight must be positive. Try again.")
                        break
                except ValueError:
                    print(error)
                except InvalidInputError as err:
                    print(err)
            return user_input

        def pass_name():
            return get_dessert_input(lambda: str(input(f"Enter the type of {dessert_type}: ")),
                                     "Must be a string. Try again.",
                                     True,
                                     False)

        def pass_weight():
            return get_dessert_input(lambda: float(input(f"Enter the weight: ")),
                                     "Must be a positive float (0.00) value. Try again.",
                                     False,
                                     True)

        def pass_quantity(prompt):
            return get_dessert_input(lambda: int(input(f"Enter the {prompt}: ")),
                                     "Must be a positive integer (0) value. Try again.",
                                     False,
                                     True)

        def pass_price(prompt=""):
            return get_dessert_input(lambda: float(input(f"Enter the {prompt}: ")),
                                     "Must be a positive float (0.00) value. Try again.",
                                     False,
                                     True)

        def pass_topping():
            return get_dessert_input(lambda: str(input(f"Enter the topping: ")),
                                     "Must be a positive float (0.00) value. Try again.",
                                     True,
                                     False)

        prompt_function = {
            "candy": lambda: dessert_class(pass_name(), pass_weight(), pass_price("price per pound")),
            "cookie": lambda: dessert_class(pass_name(), pass_quantity("quantity purchased"),
                                            pass_price("price per dozen")),
            "icecream": lambda: dessert_class(pass_name(), pass_quantity("number of scoops"),
                                              pass_price("price per scoop")),
            "sundae": lambda: dessert_class(pass_name(), pass_quantity("number of scoops"),
                                            pass_price("price per scoop"), pass_topping(),
                                            pass_price("price for the topping"))
        }.get(dessert_type)

        return prompt_function()

    def user_prompt_candy(self):
        self.dessert_class = Candy
        return self.gather_input("candy")

    def user_prompt_cookie(self):
        self.dessert_class = Cookie
        return self.gather_input("cookie")

    def user_prompt_icecream(self):
        self.dessert_class = IceCream
        return self.gather_input("icecream")

    def user_prompt_sundae(self):
        self.dessert_class = Sundae
        return self.gather_input("sundae")


def user_input_interface(shop: DessertShop, receipt: list):
    order = Order()
    payment = PaymentProcessor()
    new_receipt = receipt

    class InvalidInputError(Exception):
        """Exception raised for invalid input errors."""
        pass

    done = False
    prompt = "\n".join(["\n",
                        "1: Candy",
                        "2: Cookie",
                        "3: Ice Cream",
                        "4: Sundae",
                        "5: Admin Module",
                        "\nWhat would you like to add to the order? (1-4, Enter for done): "
                        ])

    payment_prompt = "\n".join(["1: Cash",
                                "2: Card",
                                "3: Phone",
                                "\nWhat form of payment will be used? (CASH, CARD, PHONE):"
                                ])
    pay_option_mapping = {
        "1": PayType.CASH,
        "cash": PayType.CASH,
        "2": PayType.CARD,
        "card": PayType.CARD,
        "3": PayType.PHONE,
        "phone": PayType.PHONE,
    }

    name_prompt = "\nEnter the customer's name: "

    def print_receipt_to_console():
        # order.add(Candy("Candy Corn", 1.5, 0.25))
        order.add(Candy("Gummy Bears", 0.25, 0.35))
        # order.add(Candy("Candy Corn", .25, 0.25))
        # order.add(Cookie("Oatmeal Raisin", 6, 3.45))
        # order.add(Cookie("Chocolate Chip", 6, 3.99))
        order.add(IceCream("Pistachio", 2, 0.79))
        # order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
        order.add(Cookie("Oatmeal Raisin", 2, 3.45))
        # order.add(Candy("Gummy Bears", 1.5, 0.25))

        cost_total = sum(_.calculate_cost() for _ in order)
        tax_total = sum(_.calculate_tax() for _ in order)
        _total = "${:.2f}".format(cost_total + tax_total)

        print_text = ["----------------------------------Receipt----------------------------------",
                      "ORDERS INSERT HERE",
                      "---------------------------------------------------------------------------",
                      f"Total number of items in order: {len(order)}",
                      f"Order Subtotals: {cost_total} [Tax: {tax_total}]",
                      f"Order Total: {_total}",
                      "---------------------------------------------------------------------------",
                      f"Paid for with {payment}.",
                      "--------------------------------------------------------------------------------",
                      f"Customer Name: {customer_name}          Customer ID: {cur_customer.id}"
                      f"         Total Orders: {len(cur_customer.order_history)}",
                      ]
        order.sort()
        order_items = []
        for _item in order:
            order_items.append(repr(_item))
        print_text[1:2] = order_items

        print("\n".join(print_text))

    def print_shop_customers(shop: DessertShop):
        for _name, customer in shop.customer_db.items():
            print(f"Name: {_name}, ID: {customer.id}")

    def print_customer_order_history(shop: DessertShop, _name):
        if _name in shop.customer_db.keys():
            customer = shop.customer_db[customer_name]
            print(f"\nOrder history for {customer_name} (Customer ID: {customer.id}):")

            for i, order in enumerate(customer.order_history):
                print(f"Order {i + 1}:")
                for item in order:
                    print(f"- {item}")
                print()
        else:
            print("Customer not found.")

    def print_best_customer(self):
        best_customer = None
        max_spent = 0.0

        for customer_name, customer in self.customer_db.items():
            total_spent = sum(order.order_cost() for order in customer.order_history)
            if total_spent > max_spent:
                max_spent = total_spent
                best_customer = customer_name

        print(f"\nThe Dessert Shop's most valued customer is: {best_customer}")

    def admin_module(shop: DessertShop):
        admin_prompt = "\n".join([
            "\n",
            "1: Shop Customer List",
            "2: Customer Order History",
            "3: Best Customer",
            "4: Exit Admin Module",
            "\nWhat would you like to do? (1-4): "
        ])

        while True:
            admin_console_input = input(admin_prompt)
            match admin_console_input:
                case "1":
                    print_shop_customers(shop)
                case "2":
                    name = input("Enter the customer's name: ")
                    print_customer_order_history(shop, name)
                case "3":
                    print_best_customer(shop)
                case "4":
                    return
                case _:
                    print("Invalid response: Please enter a choice from the menu (1-4)")

    while not done:
        choice = input(prompt)
        match choice:
            case "":
                customer_name = input(name_prompt)
                if customer_name in shop.customer_db.keys():
                    cur_customer = shop.customer_db.get(customer_name)
                else:
                    cur_customer = Customer(customer_name)
                    shop.customer_db[customer_name] = cur_customer
                while True:
                    try:
                        pay_options = input(payment_prompt).lower()
                        try:
                            payment.set_pay_type(pay_option_mapping[pay_options])
                            order.sort()
                            cur_customer.add2history(order)
                            print_receipt_to_console()
                            break
                        except KeyError:
                            raise InvalidInputError("Invalid response: Please enter a choice from the menu (1-3)")
                    except InvalidInputError as err:
                        print(err)
                done = True
            case "1":
                item = shop.user_prompt_candy()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "2":
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "3":
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "4":
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "5":
                admin_module(shop)
            case _:
                print("Invalid response: Please enter a choice from the menu (1-4) or Enter")
    print()

    cost_total = sum(_.calculate_cost() for _ in order)
    tax_total = sum(_.calculate_tax() for _ in order)
    orders = [item.split(", ") for item in str(order).split("\n")]

    receipt_makeup = [
        [f"Customer Name: {customer_name}", f"Customer ID: {Customer.id_counter}",
         f"Total Orders: {len(orders)}"],
        ["Name", "Packaging", "Quantity", "Unit Price", "Cost", "Tax"],
        ["------------", "------------", "------------", "------------", "------------", "------------"],
        ["Total items in the order", "", f"-- {len(order)} --", "Order Subtotals:", "${:.2f}".format(cost_total),
         "${:.2f}".format(tax_total)],
        [f"paid for with {payment}.", "", "", "Order Total:",
         "${:.2f}".format(cost_total + tax_total)]
    ]

    receipt_makeup[2:2] = orders
    for line in receipt_makeup:
        new_receipt.append(line)
    return new_receipt


def main():
    """
    Main function.
    """
    shop = DessertShop()

    receipt_list = []
    receipt_list = user_input_interface(shop, receipt_list)
    while True:
        try:
            start_over = input("Press y and Enter to start a new order.")
            if start_over == "y":
                user_input_interface(shop, receipt_list)
            else:
                break
        except None:
            print("error")

    make_receipt(receipt_list, "receipt.pdf")
    print("\n--------------------PROCESSING--------------------"
          "\n---------------------COMPLETE---------------------"
          "\nThanks for your order!")


if __name__ == "__main__":
    main()
