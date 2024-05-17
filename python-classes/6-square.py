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
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position == ():
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Getter method to retrieve the value of size"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter method to retrieve the value of size"""
        return self.__size

    @property
    def position(self):
        """Getter method to retrieve the value of position"""
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
        """Setter method to set the value of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """function to print the square"""
        for x in range(self.position[1]):
            if self.__position[1] > 0:
                print("")
            else:
                print(" ")
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
