#!/usr/bin/python3
"""
    Module that define a class
"""

from typing import SupportsIndex


class VerboseList(list):
    """
        Create a class named VerboseList that extends the Python list class.
        This custom class should print a notification message every time an
        item is added (using the append or extend methods) or removed
        (using the remove or pop methods).
    """

    def append(self, object):
        print("Added [{}] to the list".format(object))
        return super().append(object)

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def extend(self, iterable):
        count = len(iterable)
        print("Extended the list with [{}] items.".format(count))
        return super().extend(iterable)

    def pop(self, index: SupportsIndex = -1):
        popped = super().pop(index)
        print("Popped [{}] from the list".format(popped))
        return popped
