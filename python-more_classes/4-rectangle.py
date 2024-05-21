#!/usr/bin/python3
"""
    Python script to define class.
"""


class Rectangle:
    """
        Class that define rectangle
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
