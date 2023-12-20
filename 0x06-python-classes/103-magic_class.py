#!/usr/bin/python3

"""MagicClass tranlated from bytecode"""


import math


class MagicClass:
    """MagicClass circle."""
    def __init__(self, radius=0):
        """Initialize MagicClass.


        Arg:
            radius (float/int): radius of new MagicClass.
        """
        self.__radius = 0
        if ((type(radius) is not int) and (type(radius) is not float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Returns MagicClass circle area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns MagicClass circle circumference"""
        return (2 * math.pi * self.__radius)
