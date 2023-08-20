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

isOn = True


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${round(resources["money"], 2)}')


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True


def check_money(money, drink):
    cost = MENU[drink]["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def deduct_ingredients(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def insert_money():
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickels = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

    return total


while isOn:
    userChoice = input('What would you like? (espresso/latte/cappuccino): ')

    if userChoice == 'off':
        isOn = False
    elif userChoice == 'report':
        print_report()
    else:
        check_resources(userChoice)
        currMoney = insert_money()
        if check_money(currMoney, userChoice):
            drinkCost = MENU[userChoice]["cost"]
            currMoney -= drinkCost
            if "money" in resources:
                resources["money"] += drinkCost
            else:
                resources["money"] = drinkCost
            if currMoney > 0:
                print(f'Here is ${round(currMoney, 2)} dollars in change')
            deduct_ingredients(userChoice)
            print(f'Here is your {userChoice}. Enjoy!')
