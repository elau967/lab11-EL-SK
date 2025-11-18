"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b): 
    return a+b
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b==1:
        raise ValueError
    if b<0:
        raise ValueError
    if a<0:
        raise ValueError
    return math.log(a,b)

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

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if a < 0 or b < 0:
        raise ValueError
    if b == 1:
        raise ValueError

    return math.log(a, b)

def exponent(a, b):
    return a ** b