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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
