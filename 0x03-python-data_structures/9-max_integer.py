#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_list.sort(reverse=True)  # makes list max first #
        return my_list[0]
