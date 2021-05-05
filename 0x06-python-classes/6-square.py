#!/usr/bin/python3
"""
Defines the class Square
"""


class Square:
    """ defines class with private attribute size """
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

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

    """ gets position """
    @property
    def position(self):
        return(self.__position)

    """ sets position """
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ prints square using hashtags """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            pos0 = self.position[0]
            pos1 = self.position[1]
            for index in range(pos1):
                print("")
            for r in range(self.size):
                for x in range(pos0):
                    print(" ", end="")
                for c in range(self.size):
                    print("#", end="")
                print()
