#!/usr/bin/python3
"""
module for class BaseGeometry
"""


class BaseGeometry:
    """
    definition for class BaseGeometry
    """

    def area(self):
        """
        not really doing anything, but now it raises and exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates that arg value is an int and positive
        if they fail errors are raised
        arg name will always be a string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
