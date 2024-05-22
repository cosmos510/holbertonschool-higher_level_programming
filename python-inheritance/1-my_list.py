#!/usr/bin/python3
"""Module that create a class Mylist"""


class MyList(list):
    """
    Class that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))
