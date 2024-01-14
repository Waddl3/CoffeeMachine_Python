MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_accepted(amount_received, drink_cost):
    """Return True if accepted, else False if insufficient."""
    if amount_received < drink_cost:
        return False
    else:
        change = round(amount_received - drink_cost, 2)
        print(f"Change: {change}")
        global profit
        profit += drink_cost
        return True


def process():
    print("Please insert coin. ")
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    return total


def is_enough(order_ingredient):
    for item in order_ingredient:
        if resources[item] < order_ingredient[item]:
            print(f"Sorry, not enough ingredients.")
            break

    print("Working on order...")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if choice == "off":
        is_on = False

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Price: ${profit}")

    if choice in MENU:
        drink = MENU[choice]
        if is_enough(drink['ingredients']):
            payment = process()
            is_accepted(payment, drink['cost'])