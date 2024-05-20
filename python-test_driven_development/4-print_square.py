#!/usr/bin/python3
"""Module to create a function to print square"""


def print_square(size):
    """function to print square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for x in range(size):
        print("#" * size)
