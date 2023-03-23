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


def is_resources_sufficient(oder_ingredients):
    for item in oder_ingredients:
        if oder_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def proces_coin():
    print("Please insert coins.:")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, oder_ingredients):
    for item in oder_ingredients:
        resources[item] -= oder_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    oder = input("What would you like? (espresso/latte/cappuccino):")
    if oder == "off":
        is_on = False
    elif oder == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[oder]
        if is_resources_sufficient(drink["ingredients"]):
            payment = proces_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(oder, drink["ingredients"])

# water = 100
# milk = 50
# coffee = 76
# money = 2.5
#
# def oder_drink(drink):
#     water2 = drink["water"]
#     milk2 = drink["milk"]
#     coffee2 = drink["coffee"]
#
# def drink(water):
# 　if oder == "espresso":
#      water -= water2
#
#
#   elif oder == "latte":
#        water -= 250
#        coffee -= 24
#        milk -= 100
#
#   elif oder == "cappuccino":
#        water -= 300
#        coffee -= 100
#        milk -= 300
#
# cost = ["cost"]
#
# # ingredients {'Water': "100m", 'Milk': '50ml', 'Coffee': '76g', 'Money': '$2.5'}
#
# print(f"Water:{water}ml, Milk: {milk}ml, Coffee: {coffee}g, Money: ${money}")
#
# change = 0.00
# # def ask_oder():
# oder = input("What would you like? (espresso/latte/cappuccino):")

# change = (quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)
# change1 = float(change)
# print(f"Here is {change2} in change.")
# change1 - cost = chang2
#
#
# # inserted_coins - cost = change
#
#
#     #
#     #
#
#
