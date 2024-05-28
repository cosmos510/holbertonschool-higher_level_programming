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

    def __init__(self, name, age, is_student):
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
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        if not filename:
            return None
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        if not filename:
            return None
        with open(filename, 'rb') as file:
            return pickle.load(file)
