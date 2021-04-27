#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = len(argv)
    sum = 0

    for index in range(1, l):
        sum = sum + int(argv[index])
    print("{:d}".format(sum))
