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


def make_coffee(drink_name, order_ingredients):
    """
    Prepares and serves a coffee based on the specified drink name and order ingredients.

    Parameters:
    - drink_name (str): The name of the chosen coffee drink.
    - order_ingredients (dict): A dictionary representing the required ingredients for the chosen coffee drink.

    Returns:
    - None

    Side Effects:
    - Updates the resources dictionary to reflect the consumption of ingredients.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}! ☕")


def is_accepted(amount_received, drink_cost):
    """
    Checks if the received payment is sufficient for the chosen coffee drink and calculates change if applicable.

    Parameters:
    - amount_received (float): The total amount received from the user.
    - drink_cost (float): The cost of the chosen coffee drink.

    Returns:
    - True if the payment is accepted.
    - False if the payment is insufficient.

    Side Effects:
    - Updates the profit variable.
    """
    if amount_received < drink_cost:
        print("Insufficient Funds. Refunded.")
        return False
    else:
        change = round(amount_received - drink_cost, 2)
        print(f"Change: {change}")
        global profit
        profit += drink_cost
        return True


def process():
    """
    Takes user input for coin denominations and calculates the total payment received.

    Parameters:
    - None

    Returns:
    - The total amount received as a float.

    Side Effects:
    - None
    """
    print("Please insert coin. ")
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    return total


def is_enough(order_ingredient):
    """
    Checks if there are sufficient resources (ingredients) to fulfill a coffee order.

    Parameters:
    - order_ingredient (dict): A dictionary representing the required ingredients for the chosen coffee drink.

    Returns:
    - None

    Side Effects:
    - Prints a message if there are insufficient ingredients for the order.
    """
    for item in order_ingredient:
        if resources[item] < order_ingredient[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


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
            if is_accepted(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
