#!/usr/bin/python3
"""
    Module that create a class
"""


class Student:
    """
    class that define a Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that retrieves a dictionary representation of a Student
        """
        if isinstance(attrs, list) and all(isinstance(ele, str)
                                           for ele in attrs):
            result = {}
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
            return result
        return self.__dict__
