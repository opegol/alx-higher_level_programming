#!/usr/bin/python3

""" Definition of a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiates rectangle class.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
            x (int): x coordinate
            y (int): y coordinate
            id (int): object identifier
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @property
    def x(self):
        """Retrieve or set rectangle x position."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieve or set rectangle y position."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):

        """Returns the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a print or str format for a rectangle object"""
        rec = "[Rectangle] " + "(" + str(self.id) + ") " + str(self.__x) + \
            "/" + str(self.__y) + " - " + str(self.__width) + "/" + \
            str(self.__height)
        return rec

    def display(self):
        """Returns a printable rectangle instance using # char."""
        rec = []
        if self.__height != 0 or self.__width != 0:
            for k in range(self.__y):
                rec.append("\n")
            for i in range(self.__height):
                for s in range(self.__x):
                    rec.append(" ")
                for j in range(self.__width):
                    rec.append("#")
                if i != (self.__height) - 1:
                    rec.append("\n")
        ret = "".join(rec)
        print(ret)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        count = len(args)
        if count > len(attrs):
            count = len(attrs)
        for i in range(count):
            if i == 0:
                if args[0] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = args[0]
            elif i == 1:
                self.width = args[1]
            elif i == 2:
                self.height = args[2]
            elif i == 3:
                self.x = args[3]
            elif i == 4:
                self.y = args[4]

        if kwargs and count == 0:
            for arg in kwargs.keys():
                if str(arg) in attrs:
                    ind = attrs.index(str(arg))
                    if ind == 0:
                        if kwargs[arg] is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = kwargs[arg]
                    elif ind == 1:
                        self.width = kwargs[arg]
                    elif ind == 2:
                        self.height = kwargs[arg]
                    elif ind == 3:
                        self.x = kwargs[arg]
                    elif ind == 4:
                        self.y = kwargs[arg]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        ret = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return ret
