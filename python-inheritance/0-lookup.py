#!/usr/bin/python3
"""Module that create a function to lookup"""


def lookup(obj):
    """
        function that returns the list of available attributes and methods of an object
    """
    return list(obj.__dict__)
