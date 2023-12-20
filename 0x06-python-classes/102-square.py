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

    def __eq__(self, square2):
        """Compares two squares with == operator."""
        return self.area() == square2.area()

    def __ne__(self, square2):
        """Compares two squares with != operator."""
        return self.area() != square2.area()

    def __lt__(self, square2):
        """Compares two squares with < operator."""
        return self.area() < square2.area()

    def __le__(self, square2):
        """Compares two squares with <= operator."""
        return self.area() <= square2.area()

    def __gt__(self, square2):
        """Compares two squares with > operator."""
        return self.area() > square2.area()

    def __ge__(self, square2):
        """Compares two squares with >= operator."""
        return self.area() >= square2.area()
