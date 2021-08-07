from menu import MENU, resources

WATER = resources['water']
MILK = resources['milk']
COFFEE = resources['coffee']
MONEY = 0

menu = ['l', 'c', 'e']


def report():
    global WATER, MILK, COFFEE, MONEY

    return print(f"WATER: {WATER}\nMILK: {MILK}\nCOFFEE: {COFFEE}\n MONEY: {MONEY}\n")


def available_resources(user_order):
    global WATER, MILK, COFFEE

    WATER -= MENU[user_order]['ingredients']['water']
    MILK -= MENU[user_order]['ingredients']['milk']
    COFFEE -= MENU[user_order]['ingredients']['coffee']


def ordered_item(user_order):
    if user_order == 'l':
        return 'latte'
    elif user_order == 'c':
        return 'cappuccino'
    else:
        return 'espresso'


def check_resources(user_order):
    global WATER, COFFEE, MILK

    water = MENU[user_order]['ingredients']['water']
    milk = MENU[user_order]['ingredients']['milk']
    coffee = MENU[user_order]['ingredients']['coffee']

    if WATER >= water:
        if MILK >= milk:
            if COFFEE >= coffee:
                return True
            else:
                print("\nSorry not enough coffee\n\n")
                return False
        else:
            print("\nNot enough milk\n\n")
            return False
    else:
        print("\nNot enough water\n\n")
        return False


def brew_coffee(user_order, money):
    global MONEY

    available_resources(user_order)

    print(f"\nHere's your {user_order}")
    MONEY += MENU[user_order]['cost']

    if money > MENU[user_order]['cost']:
        print(f"Here's your change {money - MENU[user_order]['cost']}$\n\n")


def coffee_machine():
    off = False

    while not off:

        print("Menu\nLatte(l)\nCappuccino(c)\nEspresso(e)")
        user_order = input("What would you like to order ?: ")

        if user_order in menu:

            user_order = ordered_item(user_order)

            if check_resources(user_order):
                quarter = int(input("Enter quarters: "))
                dime = int(input("Enter dimes: "))
                nickle = int(input("Enter nickles: "))
                penny = int(input("Enter pennies: "))

                money = quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01

                if money >= MENU[user_order]['cost']:
                    brew_coffee(user_order, money)

        elif user_order == 'report' or user_order == 'r':
            report()
        elif user_order == 'off':
            print("Machine is off")
            off = True
        else:
            print("Invalid Order\n")


coffee_machine()
