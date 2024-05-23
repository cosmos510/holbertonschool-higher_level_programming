#!/usr/bin/python3
"""
    Module that define a class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
        class that define a class Animal
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Class that defines a Dog, which is a subclass of Animal
    """

    def sound(self):
        self.sound = "Bark"
        return self.sound


class Cat(Animal):
    """
    Class that defines a Cat, which is a subclass of Animal
    """

    def sound(self):
        self.sound = "Meow"
        return self.sound
