from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from CoffeMachine import data

coffeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()


def ask_for_input():
    input_text = input(f"What would you like? ({menu.get_items()}): ").lower()
    if input_text == 'off':
        exit()
    elif input_text == 'report':
        coffeMaker.report()
        moneyMachine.report()
    else:
        coffe_order = menu.find_drink(input_text)
        if coffe_order:
            if coffeMaker.is_resource_sufficient(coffe_order):
                if moneyMachine.make_payment(coffe_order.cost):
                    coffeMaker.make_coffee(coffe_order)
    ask_for_input()


def start():
    print(data.coffee_logo)
    ask_for_input()


start()
