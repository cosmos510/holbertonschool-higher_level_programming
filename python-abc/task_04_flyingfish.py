#!/usr/bin/python3
"""
Module that defines classes for Fish, Bird, and FlyingFish
with their respective behaviors
"""


class Fish:
    """
    Defines a class Fish with swimming behavior and habitat information
    """

    def swim(self):
        """
        Prints a message indicating that the fish is swimming
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message indicating that the fish lives in water
        """
        print("The fish lives in water")


class Bird:
    """
    Defines a class Bird with flying behavior and habitat information
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message indicating that the bird lives in the sky
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Defines a class FlyingFish that inherits from both Fish and Bird,
    representing a fish that can both swim and fly
    """

    def fly(self):
        """
        Prints a message indicating that the flying fish is soaring
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the flying fish is swimming
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message indicating that the flying fish lives both
        in water and in the sky
        """
        print("The flying fish lives both in water and the sky!")
