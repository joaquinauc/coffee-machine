from menu import MENU, resources


def check_resources(ingredients_in_drink):
    for item in ingredients_in_drink:
        if ingredients_in_drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            resources[item] -= ingredients_in_drink[item]
    return True


def check_money(drink):
    quarter = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    money = quarter + dimes + nickles + pennies
    change = round(money - drink['cost'], 2)
    if change >= 0:
        print(f"Here is {change} in change.")
        return drink['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0.0


def return_resources(ingredients_in_drink):
    for item in ingredients_in_drink:
        resources[item] += ingredients_in_drink[item]


def main():
    turn_off_machine = False

    while not turn_off_machine:
        still_ordering = True

        while still_ordering:
            choice = input("What would you like? (espresso/latte/cappuccino): ")
            if choice == "report":
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print(f"Money: ${resources['money']}")
            elif choice == "off":
                turn_off_machine = True
                still_ordering = False
            else:
                if choice in MENU:
                    drink = MENU[choice]
                    still_ordering = check_resources(drink['ingredients'])
                    cost = check_money(drink)
                    resources['money'] += cost
                    if cost != 0.0:
                        print(f"Here's your {choice}. Enjoy!")
                    else:
                        return_resources(drink['ingredients'])
                else:
                    print("That choice doesn't exist. Try again.")


main()
