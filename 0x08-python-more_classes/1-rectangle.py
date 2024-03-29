#!/usr/bin/python3

"""Template for a class rectangle."""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): breadth of the new rectangle.
            height (int): length of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve or set rectangle size."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve or set rectangle size."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
