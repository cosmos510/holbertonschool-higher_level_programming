#!/usr/bin/python3
"""
    Module that define a class
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
        Class that defines a shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
        class that defines circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
        class that defines rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return ((self.width + self.height) * 2)


def shape_info(shape):
    print("Area: {} ".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
