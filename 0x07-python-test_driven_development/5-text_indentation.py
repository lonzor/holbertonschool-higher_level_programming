#!/usr/bin/python3
"""
module for text_indentation functon
"""


def text_indentation(text):
    """
    prints arg text and new lines when
    characters '?', '.', and ':' are found
    arg 'text' must be of type str
    """

    if type(text) is not str:
        """ checks to make sure arg text is of type str """
        raise TypeError("text must be a string")

    string2 = ""

    if "?" not in text and ":" not in text and "." not in text:
        """ prints text even if there aren't any characters """
        print("{}".format(text))
    else:
        """
        use replace in order remove spaces from characters
        then add the two new lines after the character
        prints the new string
        """
        string2 = text.replace(". ", ".")
        string2 = string2.replace(": ", ":")
        string2 = string2.replace("? ", "?")
        string2 = string2.replace(".", ".\n\n")
        string2 = string2.replace(":", ":\n\n")
        string2 = string2.replace("?", "?\n\n")
        print("{}".format(string2), sep="", end="")
