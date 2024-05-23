#!/usr/bin/python3
"""
    Module that defines abstract and concrete classes
    for geometric shapes
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class that defines a shape with methods
    to calculate area and perimeter
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Class that defines a Circle, which is a subclass of Shape

    Attributes:
        radius (float): The radius of the circle
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle
        Returns:
            float: The area of the circle
        """
        return abs(pi * (self.radius ** 2))

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle
        Returns:
            float: The perimeter of the circle
        """
        return abs(2 * pi * self.radius)


class Rectangle(Shape):
    """
    Class that defines a Rectangle, which is a subclass of Shape
    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """

        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            float: The area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            float: The perimeter of the rectangle
        """
        return ((self.width + self.height) * 2)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape
    Args:
        shape (Shape): An instance of a subclass of Shape
    """
    print("Area: {} ".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
