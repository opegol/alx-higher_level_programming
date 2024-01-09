#!/usr/bin/python3

""" Definition of a Square class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class inherits from Rctangle"""

    def __init__(self, size):
        """ Instantiates square class.

        Args:
            size (int): Width of new Square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
