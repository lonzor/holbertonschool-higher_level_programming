#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    for r in matrix:
        for idx in range(len(r)):
            if idx == len(r) - 1:
                print("{:d}".format(r[idx]), end="")
            else:
                print("{:d}".format(r[idx]), end="")
        print()
