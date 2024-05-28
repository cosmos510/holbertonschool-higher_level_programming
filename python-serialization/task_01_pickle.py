#!/usr/bin/python3
"""
    Module that create class to serialize and deserialize
    custom Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """
        Class that define a custom object
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes a Object
        Args:
            name: first name of the student
            age: age of the student
            is_student: student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
            function that display the object's attribute
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
            This method will take a filename as its parameter.
            Using the pickle module, it will serialize the current instance
            of the object and save it to the provided filename
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
            This class method will take a filename as its parameter.
            Using the pickle module, it will load and return an instance
            of the CustomObject from the provided filename.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
