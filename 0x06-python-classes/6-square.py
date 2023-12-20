#!/usr/bin/python3

"""Template for a class square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.


        Args:
            size (int): Size (dimension) of the new square.
        """
        self.size = size
        self.position = position

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
        for ln in range(self.__position[1]):
            print("")
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print(" " * self.position[0], end='')
            for j in range(self.__size):
                print("#", end='')
            print("")

    @property
    def position(self):
        """Retrieve or set square position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
                type(value[0]) is not int or
                type(value[1]) is not int or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
