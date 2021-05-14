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
        for h in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            print("")
