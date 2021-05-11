#!/usr/bin/python3
"""
module for class Square
Square inherits from class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines Square class """

    def __init__(self, size):
        """
        initializes a Square object
        uses integer_validator to make sure
        size is of type int
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Prints description of square object """
        return "[Square] {}/{}".format(self.__size, self.__size)
