"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)# raise ValueError if a < 0
    except ValueError:
        print("A < 0")

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a < 0 or b < 0:
        raise ValueError
    if b == 1:
        raise ValueError

    return math.log(a, b)# use math library/raise ValueError

def exponent(a, b):
    return a ** b