#!/usr/bin/python3
"""
Module for function read_file(filename="")
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints to stdout
    """
    with open(filename, encoding='utf-8') as input_file:
        for line in input_file:
            print(line, end="")
