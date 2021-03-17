#!/usr/bin/python3
"""
Rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix
    """
    matrix1 = [[l for l in s] for s in matrix]
    l = len(matrix)
    for i in range(0, l):
        for j in range(0, l):
            matrix1[i][j] = matrix[l-j-1][i]
    for i in range(0, l):
        matrix[i] = matrix1[i]
