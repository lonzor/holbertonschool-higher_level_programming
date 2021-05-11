#!/usr/bin/python3
"""
module for class MyList that inherits from list
"""


class MyList(list):
    """ defined class MyList """
    def __init__(self):
        """ initializes MyList """
        pass

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
