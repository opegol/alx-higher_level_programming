#!/usr/bin/python3

"""Template for a class square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): Size (dimension) of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
