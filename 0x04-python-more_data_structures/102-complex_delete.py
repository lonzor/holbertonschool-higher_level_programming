#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return None
    else:
        for i, j in list(a_dictionary.items()):
            if j == value:
                del a_dictionary[i]
    return a_dictionary
