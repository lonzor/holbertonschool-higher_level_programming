#!/usr/bin/python3
def no_c(my_string):
    str2 = ""
    for idx in my_string:
        if idx != "C" and idx != "c":
            str2 = str2 + idx
    return str2
