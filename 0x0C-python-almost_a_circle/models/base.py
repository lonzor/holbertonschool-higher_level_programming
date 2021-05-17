#!/usr/bin/python3
"""
Modle for class Base
Will be the "base" for all other classes
"""
import json


class Base:
    """
    private class attribute for Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor - makes object
        id of type int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of 'list_dictionaries'
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation 'json_string'
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        ml = []
        name_of_file = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                ml.append(cls.to_dictionary(i))
        with open(name_of_file, 'w') as input_file:
            input_file.write(cls.to_json_string(ml))
