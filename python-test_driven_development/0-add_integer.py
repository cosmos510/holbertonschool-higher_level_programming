#!/usr/bin/python3
"""Module to create a function to add two number"""


def add_integer(a, b=98):
    """
        Function to add two integer
        Float are cassed to int
        Raise type error is a or b ar not int either float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
