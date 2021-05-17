#!/usr/bin/python3
"""
Module for class Square
Inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initializes an empty square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for 'size'
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """
        prints data about the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        if len(args) != 0:
            i = 0
            new_square = ["id", "size", "x", "y"]
            for k in args:
                setattr(self, new_square[i], args[i])
                i = i + 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
