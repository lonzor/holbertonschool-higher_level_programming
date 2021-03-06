#!/usr/bin/python3
"""
Module for class Rectangle
Class Rectangle inherits from class Base
"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for object
        id is of type int
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for 'width' """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for 'width'
        Validating for negative value and type int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for 'height' """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for 'height'
        Validating for negative value and type int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for 'x' """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for 'x'
        Validating for negative value and type int
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for 'y' """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for 'y'
        Validating for negative value and type int
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns area of Rectangle object
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle object/instance with # symbol
        """
        if self.width == 0 or self.height == 0:
            return
        print("\n" * self.y, end="")
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Returns a printed statement with width/height
        and the area on a new line
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates class Rectange by assigning an argument to each att
        """
        if len(args) != 0:
            i = 0
            new_att = ["id", "width", "height", "x", "y"]
            for k in args:
                setattr(self, new_att[i], args[i])
                i = i + 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of Retangle instance
        """
        rect_dict = {"id": self.id, "width": self.width, "height": self.height,
                     "x": self.x, "y": self.y}
        return rect_dict
