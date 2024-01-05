#!/usr/bin/python3

"""Template for a class rectangle."""


class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): breadth of the new rectangle.
            height (int): length of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a printable rectangle instance using # char."""
        rec = []
        if self.__height != 0 or self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec.append(str(self.print_symbol))
                if i != self.__height - 1:
                    rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        """Returns canonical string representation of rectangle instance."""
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return r

    def __del__(self):
        """Prints message when instance of rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
