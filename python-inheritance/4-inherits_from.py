#!/usr/bin/python3
"""
    Module to create a function inherits_from
"""


def inherits_from(obj, a_class):
    """
        unction that returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class ;
        otherwise False.
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
