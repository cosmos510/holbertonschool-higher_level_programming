#!/usr/bin/python3
"""Module to create a function """


def add_attribute(cla, name, objet):
    if not hasattr(cla, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cla, name, objet)
