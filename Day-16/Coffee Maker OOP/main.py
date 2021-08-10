from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
CM = CoffeeMaker()
MM = MoneyMachine()

off = False

while not off:
    item = MENU.get_items()
    order = input(f"What would you like to order ({item}):")

    if order == "report":
        CM.report()
    elif order == "off":
        off = True
    else:
        drink = MENU.find_drink(order)
        if drink:
            if CM.is_resource_sufficient(drink):
                if MM.make_payment(drink.cost):
                    CM.make_coffee(drink)
        else:
            print("Invalid Drink\n")