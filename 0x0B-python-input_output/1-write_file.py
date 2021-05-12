#!/usr/bin/python3
"""
Module for function write_file()
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.
    """
    with open(filename, mode='w', encoding='UTF-8') as input_file:
        return input_file.write(text)
