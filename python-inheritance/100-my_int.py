#!/usr/bin/python3
"""
    Python script to define class.
"""


class MyInt(int):
    """Class that defines a class MyInt"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
