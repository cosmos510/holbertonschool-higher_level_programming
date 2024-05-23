#!/usr/bin/python3
"""
    Module that defines a custom list class with verbose operations
"""

from typing import SupportsIndex


class VerboseList(list):
    """
    A custom list class that extends the Python list class.
    This class prints a notification message every time an item is added
    (using the append or extend methods) or
    removed (using the remove or pop methods).
    """

    def append(self, object):
        """
        Add an item to the end of the list and print a notification.
        Args:
            object: The item to be added to the list.
        """
        print("Added [{}] to the list".format(object))
        return super().append(object)

    def remove(self, value):
        """
        Remove the first occurrence of a value from
        the list and print a notification.
        Args:
            value: The value to be removed from the list.
        """
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a notification.
        Args:
            iterable: An iterable whose elements will be added to the list.
        """
        count = len(iterable)
        print("Extended the list with [{}] items.".format(count))
        return super().extend(iterable)

    def pop(self, index: SupportsIndex = -1):
        """
        Remove and return an item at the given index (default is the last item)
        and print a notification.
        Args:
            index (SupportsIndex, optional): The index of the item
            to be removed. Defaults to -1.
        Returns:
            The item that was removed from the list.
        """

        popped = super().pop(index)
        print("Popped [{}] from the list".format(popped))
        return popped
