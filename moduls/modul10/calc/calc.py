import math

red = "\033[0;31m"
def sum(a, b):
    return a + b
def minus(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return f"{red}Ділення на нуль!"
def power(a, b):
    return a ** b
def root(a, b):
    return a ** (1 / b)
def modul(a, b):
    if b != 0:
        return a % b
    else:
        return f"{red}Ділення на нуль!"
def integer(a, b):
    if b != 0:
        return a // b
    else:
        return f"{red}Ділення на нуль!"