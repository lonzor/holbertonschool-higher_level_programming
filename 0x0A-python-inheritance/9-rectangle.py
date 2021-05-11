#!/usr/bin/python3
"""
module for class Rectange that is
inherited from class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    definition for class Rectangle
    """

    def __init__(self, width, height):
        """
        initializes a object for Rectangle
        validates that args are an int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        finds the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a printed statement with width/height
        and the area on a new line
        """
        return "[Rectangel] {}/{}".format(self.__width, self.__height)
