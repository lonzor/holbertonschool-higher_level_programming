#!/usr/bin/python3
"""
Module contains the class Student.
Instantiates object with first_name, last_name, and age.
"""


class Student:
    """
    Definition of class Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new object from class Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary description of Student object (JSON).
        """
        return self.__dict__
