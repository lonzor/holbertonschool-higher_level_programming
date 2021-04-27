#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = len(argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(l, "arguments:"))
        for index in range(1, l + 1):
            print("{:d}: {}".format(index, argv[index]))
