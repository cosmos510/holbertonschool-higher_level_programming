#!/usr/bin/python3
"""
Module that defines Animal, Dog, and Cat classes
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class that defines an Animal
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses
        to return the sound the animal makes
        """
        pass


class Dog(Animal):
    """
    Class that defines a Dog, which is a subclass of Animal
    """

    def sound(self):
        """
        Method that returns the sound a Dog makes
        """
        self.sound = "Bark"
        return self.sound


class Cat(Animal):
    """
    Class that defines a Cat, which is a subclass of Animal
    """

    def sound(self):
        """
        Method that returns the sound a Cat makes
        """
        self.sound = "Meow"
        return self.sound
