#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if k < len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][k]), end=" ")
            else:
                print("{:d}".format(matrix[i][k]), end="")
        print("")
