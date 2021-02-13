#!/usr/bin/python3
"""
Module for matrix division
"""


def matrix_divided(matrix, div):

    """
    Function for matri division
    """

    len_wos = len(matrix[0])
    for i in range(0, len(matrix)):
        if len(matrix[i]) != len_wos:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ValueError("division by zero")

    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if type(matrix[i][j]) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    Matrix = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

    for i in range(0, len(Matrix)):
        for j in range(0, len(Matrix[0])):
            Matrix[i][j] = round(matrix[i][j]/div, 2)
    return Matrix
