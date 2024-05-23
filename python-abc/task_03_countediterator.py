#!/usr/bin/python3
"""
Module that defines a custom iterator class with a count feature
"""


class CountedIterator:
    """
    A custom iterator class that extends the built-in iterator.
    The CountedIterator keeps track of the number of items
    that have been iterated over.

    Attributes:
        itera_obj (iterator): The original iterator created from the
        provided data.
        counter (int): The counter to keep track of
        the number of items iterated over.
    """

    def __init__(self, data):
        """
        Initialize the CountedIterator with the provided data.
        Args:
            data (iterable): The data to be iterated over.
        """

        self.itera_obj = iter(data)
        CountedIterator.counter = 0

    def get_count(self):
        """
        Get the current count of items that have been iterated over.
        Returns:
            int: The number of items that have been iterated over.
        """

        return self.counter

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.
        Returns:
            The next item from the iterator.
        Raises:
            StopIteration: If there are no more items in the iterator.
        """
        item = next(self.itera_obj)
        self.counter += 1
        if self.counter == 0:
            raise StopIteration
        return item
