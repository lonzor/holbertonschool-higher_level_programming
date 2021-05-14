#!/usr/bin/python3
"""
Modle for class Base
Will be the "base" for all other classes
"""


class Base:
    """
    private class attribute for Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor - makes object
        id of type int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
