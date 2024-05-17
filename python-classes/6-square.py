#!/usr/bin/python3
"""Python script to define class.
"""


class Square():
    """Class that define square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initiation of the class square with the size"""

        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method to set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        if self.__position[1] >= 0:
            pass
        else:
            print(" " * self.__position[1])
