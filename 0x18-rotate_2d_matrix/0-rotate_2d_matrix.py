#!/usr/bin/python3
"""
Rotate a 3D matrix
"""
from copy import copy, deepcopy


def rotate_2d_matrix(matrix):
    matrix1 = deepcopy(matrix)
    l = len(matrix)
    for i in range(0, l):
        for j in range(0, l):
            matrix1[i][j] = matrix[l-j-1][i]
    for i in range(0, l):
        matrix[i] = matrix1[i]
