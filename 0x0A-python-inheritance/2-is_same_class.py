#!/usr/bin/python3
"""
module for function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns true if the object is exactly and instance
    of the specified class. Returns false otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
