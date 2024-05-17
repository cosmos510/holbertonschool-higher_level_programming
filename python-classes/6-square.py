#!/usr/bin/python3
"""Module to define a Square class."""

class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a size and a position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the value of position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the value of position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        if self.__size == 0:
            print("")
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
