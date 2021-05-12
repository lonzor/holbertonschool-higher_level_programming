#!/usr/bin/python3
"""
Module for save_to_json_file(my_obj, filename).
Writes an object to a text file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.
    """
    with open(filename, mode='w', encoding='UTF-8') as input_file:
        input_file.write(json.dumps(my_obj))
