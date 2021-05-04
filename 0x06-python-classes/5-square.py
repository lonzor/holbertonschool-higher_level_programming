#!/usr/bin/python3
"""
Defines the class Square
"""


class Square:
    """ defines class with private attribute size """
    def __init__(self, size=0):
        self.__size = size

    """ gets size """
    @property
    def size(self):
        return self.__size

    """ checks int type and value >= 0 """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ gets area of square """
    def area(self):
        return self.__size ** 2

    """ prints a square with hashtags """
    def my_print(self):
        if self.__size == 0:
            print("")
        for r in range(self.__size):
            for c in range(self.__size):
                print("#", end="")
            print("")
