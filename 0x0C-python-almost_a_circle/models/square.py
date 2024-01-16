#!/usr/bin/python3

""" Definition of a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rctangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiates square class.

        Args:
            size (int): Width of new Square.
            x (int):.
            y (int):.
            id (int):.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve or set rectangle size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__size = value
            self.__width = value
            self.__height = value

    def __str__(self):
        """Returns a print or str format for a square object"""
        rec = "[Square] " + "(" + str(self.id) + ") " + str(self.x) + \
            "/" + str(self.y) + " - " + str(self.__size)
        return rec

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ['id', 'size', 'x', 'y']
        count = len(args)
        if count > len(attrs):
            count = len(attrs)
        for i in range(count):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.size = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]

        if kwargs and count == 0:
            for arg in kwargs.keys():
                if str(arg) in attrs:
                    ind = attrs.index(str(arg))
                    if ind == 0:
                        self.id = kwargs[arg]
                    elif ind == 1:
                        self.size = kwargs[arg]
                    elif ind == 2:
                        self.x = kwargs[arg]
                    elif ind == 3:
                        self.y = kwargs[arg]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        ret = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return ret
