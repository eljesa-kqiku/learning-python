import data


def check_resources(coffee):
    ingredients = data.MENU[coffee]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > data.resources[ingredient]["amount"]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins(coffee):
    price = data.MENU[coffee]["cost"]
    print(f"That will be ${price}. Please insert coins.")

    total_inserted_amount = 0
    for coin in data.coins:
        amount = int(input(f"{coin}? : "))
        total_inserted_amount += amount * data.coins[coin]

    if total_inserted_amount < price:
        print("Sorry that's not enough money. Money refund.")
        return False
    else:
        change = round(total_inserted_amount - price, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        return True


def reduce_resources(coffee):
    ingredients = data.MENU[coffee]["ingredients"]
    for ingredient in ingredients:
        data.resources[ingredient]["amount"] -= ingredients[ingredient]
    data.resources["money"]["amount"] += data.MENU[coffee]["cost"]


def make_coffe(coffee):
    if check_resources(coffee):
        if process_coins(coffee):
            reduce_resources(coffee)
            print(f"Here is your {coffee}. Enjoy! ☕")

    ask_for_input()


def print_report():
    for key in data.resources:
        print(f"{key.title()}: {data.resources[key]['amount']}{data.resources[key]['units']}")
    ask_for_input()


def ask_for_input():
    input_text = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if input_text == 'off':
        exit()
    elif input_text == 'report':
        print_report()
    elif input_text in ['espresso', 'latte', 'cappuccino']:
        make_coffe(input_text)
    else:
        print("Opps! Typo.")
        ask_for_input()


def start():
    print(data.coffee_logo)
    ask_for_input()


start()
