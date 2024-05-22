#!/usr/bin/python3
"""
    Python script to define class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class that define a rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.integer_validator("width", width)
        self.height = height
        self.integer_validator("height", height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.width, self.height)
