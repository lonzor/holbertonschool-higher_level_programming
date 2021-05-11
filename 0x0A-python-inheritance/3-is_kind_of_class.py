#!/usr/bin/python3
"""
module for function is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of a the class
    or of a class that is inherited
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
