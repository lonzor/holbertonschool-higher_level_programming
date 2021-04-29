#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    for elmnt in my_list:
        if elmnt == search:
            list2.append(replace)
        else:
            list2.append(elmnt)
    return list2
