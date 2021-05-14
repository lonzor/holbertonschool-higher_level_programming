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
        """ Setter for 'width' """
        self.__width = value

    @property
    def height(self):
        """ Getter for 'height' """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for 'height' """
        self.__height = value

    @property
    def x(self):
        """ Getter for 'x' """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for 'x' """
        self.__x = value

    @property
    def y(self):
        """ Getter for 'y' """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for 'y' """
        self.__y = value
