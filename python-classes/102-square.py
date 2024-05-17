#!/usr/bin/python3
"""Python script to define class.
"""


class Square:
    """Class that define square
    """
    def __init__(self, size=0):
        """initiation of the class square with the size"""

        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Getter method to retrieve the value of size"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter method to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        if isinstance(other, Square):
            return(self.area() == other.area())

    def __gt__(self, other):
        if isinstance(other, Square):
            return(self.area() > other.area())

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()

    def __ne__(self, other):
        if isinstance(other, Square):
            return(self.area() != other.area())

    def __ge__(self, other):
        if isinstance(other, Square):
            return(self.area() >= other.area())

    def __le__(self, other):
        if isinstance(other, Square):
            return(self.area() <= other.area())
