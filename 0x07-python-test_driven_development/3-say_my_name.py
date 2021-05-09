#!/usr/bin/python3
"""
Module for say_my_name function
Prints a first name then last name
Uses args of type str first_name and last_name
"""


def say_my_name(first_name, last_name=""):
    """
    prints "My name is <first_name> <last_name>"
    """

    if type(first_name) is not str:
        """ verifies arg is of type str """
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        """ verifies arg is of type str """
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
