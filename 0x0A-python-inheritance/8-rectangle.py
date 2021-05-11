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

    def area(self):
        """
        not really doing anything, but now it raises and exception
        """
        raise Exception("area() is not implemented")

    def __init__(self, width, height):
        """
        initializes a object for Rectangle
        validates that args are an int
        """
        if BaseGeometry.integer_validator(self, "width", width):
            self.width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.height = height
