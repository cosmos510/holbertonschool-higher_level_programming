#!/usr/bin/python3
"""Module to create a function to print last name and first name"""


def say_my_name(first_name, last_name=""):
    """
    Function to print last name follow by first name
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
