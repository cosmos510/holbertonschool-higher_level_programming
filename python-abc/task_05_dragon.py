#!/usr/bin/env python3
"""
Module that defines mixin classes for swimming and flying behaviors,
and a Dragon class that incorporates these behaviors.
"""


class SwimMixin:
    """
    Mixin class that provides swimming behavior.
    """

    def swim(self):
        """
        Prints a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying behavior.
    """

    def fly(self):
        """
        Prints a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class that defines a Dragon, which can both swim and fly.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon roars.
        """
        print("The dragon roars!")
