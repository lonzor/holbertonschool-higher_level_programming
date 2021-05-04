#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_list = 0

    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            int_list = int_list + 1
        except (ValueError, TypeError):
            continue
    print("")
    return int_list
