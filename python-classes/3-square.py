#!/usr/bin/python3
"""Python script to define class.
"""


class Square():
    """Class that define square
    """
    def __init__(self, size=0):
        """initiation of the class square with the size"""

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
