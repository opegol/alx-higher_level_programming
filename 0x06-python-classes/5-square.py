#!/usr/bin/python3

"""Template for a class square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a new square.


        Args:
            size (int): Size (dimension) of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve or set square size."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
