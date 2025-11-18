"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/elau967/lab11-EL-SK.git
# Partner 1: Eric Lau
# Partner 2: Simon Kareng

import math
def add(a, b): 
    return a+b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a**b

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

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a < 0 or b < 0:
        raise ValueError
    if b == 1:
        raise ValueError

    return math.log(a, b)