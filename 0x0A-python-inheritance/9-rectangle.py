#!/usr/bin/python3

""" Definition of a Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ Instantiates rectangle class.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a print or str format for a rectangle object"""
        rec = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return rec
