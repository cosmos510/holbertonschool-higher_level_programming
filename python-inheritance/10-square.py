#!/usr/bin/python3
"""
    Python script to define class.
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
        class that defines a square
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
