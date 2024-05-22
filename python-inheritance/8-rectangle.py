#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    Python script to define class.
"""


class Rectangle(BaseGeometry):
    """
        Class that define a rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
