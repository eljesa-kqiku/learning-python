import os
from logo import logo

# Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print("Division by 0 not allowed")
        return
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def start_calcluator(num1, num2):
    if num1 is None:
        num1 = float(input("num1 = "))
    num2 = float(input("num2 = "))

    print("Choose the operation: ")
    for key in operations:
        print(key)
    operation = input("")
    res = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {res}")
    return res


stop = False
num1, num2 = [None, None]
print(logo)
while not stop:
    num1 = start_calcluator(num1, num2)
    cont = input("Do you want to continue? Type 'y' for yes, 'n' for no, 'r' to reset: ")
    if cont == 'n':
        stop = True
    if cont == 'r':
        os.system('cls' if os.name == 'nt' else 'clear')
        num1 = None