#!/usr/bin/env python3
from art import logo

print(logo)


def add(n1, n2):
    """Function That Adds"""
    return n1 + n2


def subtract(n1, n2):
    """Function That Subtracts"""
    return n1 - n2


def multiply(n1, n2):
    """Function That Multiplies"""
    return n1 * n2


def divide(n1, n2):
    """Function that Divides"""
    return n1 * n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

calc_program = False

while not calc_program:
    num1 = int(input("Enter a Number: "))
    num2 = int(input("Enter a Number: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick a Symbol from above: ")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    end_program = input("Finished: y/n ")

    if end_program == 'y':
        end_program = False
