#!/usr/bin/python3
"""
Module for load_from_json_file(filename).
Creates an object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".
    """
    with open(filename, encoding='UTF-8') as input_file:
        return json.load(input_file)
