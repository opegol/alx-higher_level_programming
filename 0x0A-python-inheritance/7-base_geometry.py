#!/usr/bin/python3

""" Definition of BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Computes area of Geometrical figure."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
