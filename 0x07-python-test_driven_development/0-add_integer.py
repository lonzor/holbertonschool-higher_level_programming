#!/user/bin/python3
"""
0-add_integer module
"""


def add_integer(a, b=98):
    """
    gets sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        """ converts a to int if it's a float """
        a = int(a)
    if type(b) is float:
        """ converts b to int if it's a float """
        b = int(b)
    return a + b
