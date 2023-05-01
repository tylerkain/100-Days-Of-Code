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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def check_resource(order_ingredients):
    """Check Resources of Coffee Machine"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"There is not enough {item}")
            return False
        return True


def process_coins():
    print("insert payment")
    total = int(input("insert quarters: ")) * 0.25
    total += int(input(f"insert dimes: ")) * 0.10
    total += int(input(f"Insert Nickels: ")) * 0.05
    total += int(input("Insert Pennies: ")) * 0.01
    return total


def complete_transaction(payment, cost):
    """Completes Transaction"""
    global profit
    if payment >= cost:
        print("making coffee")
        change = round(payment - cost, 2)
        print(f"your change is: {change}")
        profit += cost
        return True
    else:
        print("Not Enough Money")


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your Drink: {drink_name}")


choice = input("What would you like? (espresso/latte/cappuccino): ")
if choice == "report":
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffe: {resources['coffee']}")

drink = MENU[choice]
if check_resource(drink["ingredients"]):
    payment = process_coins()
    if complete_transaction(payment, drink["cost"]):
        make_coffee(drink, resources)
