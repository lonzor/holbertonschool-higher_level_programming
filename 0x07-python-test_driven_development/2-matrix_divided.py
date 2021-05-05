#!/usr/bin/python3
"""
Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix and returns
    a new matrix.
    """
    matrix2 = []

    for r in matrix:
        for digit in r:
            if type(matrix) is not list:
                """ checks lists make up matrix """
                raise TypeError("mastrix must be a matrix "
                                "(list o flists) of integers/floats")
            if type(digit) is not int and type(digit) is not float:
                """ checks type of data in matrix is only numbers """
                raise TypeError("mastrix must be a matrix "
                                "(list o flists) of integers/floats")
            if len(matrix[0]) != len(matrix[1]):
                """ checks length of rows and columns match """
                raise TypeError("each row of matrix must have "
                                "the same size")
        if type(div) is not int and type(div) is not float:
            """ check if div is a number """
            raise TypeError("div must be a number")
        if type(div) == 0:
            """ checks for ZeroDivision """
            raise ZeroDivisionError("division by zero")
        if type(div) is None:
            """ check if a data was given for div """
            raise TypeError("div must be a number")
        for r in range(len(matrix)):
            matrix2.append(list(map(lambda x: round(x / div, 2), matrix[r])))
        return matrix2
