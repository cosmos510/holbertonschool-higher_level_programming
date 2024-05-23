#!/usr/bin/python3
"""
    Module that define a class
"""


class CountedIterator:
    """
        Create a class named CountedIterator that extends the built-in
        iterator obtained from the iter function. The CountedIterator
        should keep track of the number of items that have been iterated
        over. Specifically, you will need to override the __next__ method
        to increment a counter each time an item is fetched.
    """

    def __init__(self, data):
        self.itera_obj = iter(data)
        CountedIterator.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.itera_obj)
        self.counter += 1
        if self.counter == 0:
            raise StopIteration
        return item
