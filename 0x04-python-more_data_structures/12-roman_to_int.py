#!/usr/bin/python3
def roman_to_int(roman_string):
    s = 0
    list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tmp = ""

    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        for r_num in roman_string:
            for value in list:
                if r_num == 'I':
                    tmp = r_num
                if value == r_num:
                    s += list[value]
                    if r_num == 'X' or r_num == 'V':
                        if tmp == 'I':
                            s -= 2
    return s
