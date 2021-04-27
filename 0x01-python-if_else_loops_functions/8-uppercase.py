#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in str:
        if ord('a') <= ord(i) and ord(i) <= ord('z'):
            i = ord(i) - 32
            str2 = str2 + chr(i)
        else:
            str2 = str2 + i
    print("{}".format(str2))
