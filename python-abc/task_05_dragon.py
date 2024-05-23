#!/usr/bin/env python3
"""
    Module that define a class
"""


class SwimMixin:
    """
        Class that create  a swimMixin
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
        Class that create  a swimMixin
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
        Class that create a dragon
    """

    def roar(self):
        print("The dragon roars!")
