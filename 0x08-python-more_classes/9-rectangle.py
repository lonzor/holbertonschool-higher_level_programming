#!/usr/bin/python3
"""
module for the class Rectangle
"""


class Rectangle:
    """
    Creates rectangle with attributes width and height.
    number_of_instances public class increases
    when a rectangle is made. Decreases when one is deleted.
    print_symbol is used for string representation, and can
    be of any type.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize rectange with width and height
        increments number_of_instances by 1
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ find width """
        return self.__width

    @width.setter
    def width(self, value):
        """ check value is int and greater than zero """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ find height """
        return self.__height

    @height.setter
    def height(self, value):
        """ check value is in and greater than zero """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ width * height to get area of rectangele """
        return self.width * self.height

    def perimeter(self):
        """ checks if width and height are 0, and calculates perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ creates rectangle with hashtag string """
        string2 = ""

        if self.width == 0 or self.height == 0:
            return string2
        for i in range(self.height):
            string2 += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string2 = string2 + "\n"
        return string2

    def __repr__(self):
        """ returns a copy of the rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        prints this message when a rectangle is deleted
        decrements number_of_instances by 1
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ finds the rectangle instance with biggest area value """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ find rectangle that is a square. Equal height and width """
        return cls(width=size, height=size)