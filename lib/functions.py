#!/usr/bin/env python3

def greet_programmer():
    """Outputs 'Hello, programmer!' to the terminal."""
    print("Hello, programmer!")

def greet(name):
    """Outputs 'Hello, {name}!' to the terminal with the given name."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """Outputs 'Hello, {name}!' to the terminal. Defaults to 'programmer' if no name is provided."""
    print(f"Hello, {name}!")

def add(num1, num2):
    """Returns the sum of num1 and num2."""
    return num1 + num2

def halve(number):
    """Returns half of the number if it's a number; otherwise returns None."""
    if isinstance(number, (int, float)):
        return number / 2
    return None
