#!/usr/bin/python3
"""
Module contains the class Student.
Instantiates object with first_name, last_name, and age.
Returns dictionary description of Studen object - to_json().
Replaces all attributes of Student object - reload_from_json().
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

    def to_json(self, attrs=None):
        """
        Returns dictionary description of Student object (JSON).
        """
        if attrs is None and type(attrs) is not list:
            return self.__dict__

        else:
            descrip_dict = {}
            for data in attrs:
                if hasattr(self, data):
                    descrip_dict[data] = getattr(self, data)

            return descrip_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with json attrs.
        Arg json will always be a dictionary.
        """
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
