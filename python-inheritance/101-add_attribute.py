#!/usr/bin/python3
"""Module to create a function """


def add_attribute(cla, name, objet):
    """
        Function  that adds a new attribute to an object if it’s possible
    """
    if not hasattr(cla, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cla, name, objet)
