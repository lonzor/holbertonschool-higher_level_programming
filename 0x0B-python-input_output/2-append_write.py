#!/usr/bin/python3
"""
Module for append_write function.
Appends a string at the end of a text file (UTF8) and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, mode='a', encoding='UTF-8') as input_file:
        return input_file.write(text)
