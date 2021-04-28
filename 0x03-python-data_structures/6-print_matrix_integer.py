#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for idx in range(len(r)):
            if idx == len(r) - 1:
                print("{:d}".format(r[idx]), end="")
            else:
                print("{:d}".format(r[idx]), end="")
        print()
