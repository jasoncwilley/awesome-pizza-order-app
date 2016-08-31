
from menu import get_menu_selection, Display_selection_error
from toppings import Topping

class Topping():
    """
    What goes on a pizza
    """

    def __init__(self, name, price=1.00):
        self.name = name
        self.price = price

    def __str__(self):
        return "{} ${:,.2f}".format(self.name, self.price)

class Pizza():
    MENU_ITEMS = (
        "1: Add Toppings",
        "2: Display Toppings",
        "3: Remove Toppings",
        "4: Add Pizza to Cart",
        "0: Cancel",
    )

    AVAILABLE_TOPPINGS = (
        Topping("Cheese"),
        Topping("Pepperoni", 2.00),
        Topping(name="Sausage", price=2.50),
    )

    def __init__(self, base_price=5.00):
        self.toppings = []
        self.base_price = base_price

    @classmethod