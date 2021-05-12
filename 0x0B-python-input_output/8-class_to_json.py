#!/usr/bin/python3
"""
Module for class_to_json(obj).
Returns dictionary description for JSON object.
"""


def class_to_json(obj):
    """
    Returns dictionary description for JSON object.
    """
    return obj.__dict__
