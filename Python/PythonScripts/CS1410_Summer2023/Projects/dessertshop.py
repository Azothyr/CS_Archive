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


class DessertShop:
    """
    prompt user for enough input to create the required line item on the receipt
    get user input
    validate the input
    convert input values to the proper types as-needed
    create an object of the proper type
    return the newly created object to the caller
    """

    def __init__(self):
        self.dessert_class = DessertItem

    def gather_input(self, dessert_type):
        bad_name_char = ("(", ")", "!", "@", "#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        dessert_class = self.dessert_class

        class InvalidInputError(Exception):
            """Exception raised for invalid input errors."""
            pass

        def get_input(prompt_func, error, only_letters=False, must_positive=False):
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
            return get_input(lambda: str(input(f"Enter the type of {dessert_type}: ")),
                             "Must be a string. Try again.",
                             True,
                             False)

        def pass_weight():
            return get_input(lambda: float(input(f"Enter the weight: ")),
                             "Must be a positive float (0.00) value. Try again.",
                             False,
                             True)

        def pass_quantity(prompt):
            return get_input(lambda: int(input(f"Enter the {prompt}: ")),
                             "Must be a positive integer (0) value. Try again.",
                             False,
                             True)

        def pass_price(prompt=""):
            return get_input(lambda: float(input(f"Enter the {prompt}: ")),
                             "Must be a positive float (0.00) value. Try again.",
                             False,
                             True)

        def pass_topping():
            return get_input(lambda: str(input(f"Enter the topping: ")),
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


def main():
    """
    Main function.
    """
    shop = DessertShop()
    order = Order()

    done = False
    # build the prompt string once
    prompt = '\n'.join(['\n',
                        '1: Candy',
                        '2: Cookie',
                        '3: Ice Cream',
                        '4: Sunday',
                        '\nWhat would you like to add to the order? (1-4, Enter for done): '
                        ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
                print("\n--------------------PROCESSING--------------------"
                      "\n---------------------COMPLETE---------------------"
                      "\nThanks for your order!")
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f"{item.name}'has been added to your order.")
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name}has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name}has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name}has been added to your order.')
            case _:
                print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    print()

    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))

    receipt_list = [["Name", "Item Cost", "Tax"]]

    cost_subtotal = 0
    tax_subtotal = 0
    for item in order:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        cost_subtotal += cost
        tax_subtotal += tax
        receipt_list.append([item.name, "${:.2f}".format(cost), "${:.2f}".format(tax)])
    receipt_list.append(["--------------------------------------------------------", "", ""])
    receipt_list.append(["Order Subtotals", "${:.2f}".format(cost_subtotal), "${:.2f}".format(tax_subtotal)])
    receipt_list.append(["Order Total", "", "${:.2f}".format(cost_subtotal + tax_subtotal)])
    receipt_list.append(["Total items in the order", "", len(order)])

    make_receipt(receipt_list, "receipt.pdf")


if __name__ == "__main__":
    main()
