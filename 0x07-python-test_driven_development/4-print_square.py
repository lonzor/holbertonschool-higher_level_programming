#!/usr/bin/python3
"""
Module for print_square function
"""


def print_square(size):
    """
    prints a square with the hashtag from arg size
    """

    if size < 0:
        """ check if arg size is a negative value """
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        """ check if arg size is of type int """
        raise TypeError("size must be an integer")

    for idx in range(size):
        """ prints a hashtag times the value of size """
        print("#" * size)
