#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtrx = []
    for idx in matrix:
        new_mtrx.append(list(map(lambda x: x ** 2, idx)))
    return new_mtrx
