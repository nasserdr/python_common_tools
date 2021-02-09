#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ncol = len(matrix)
    row = len(matrix[0])
    new_matrix = [[0 for i in range(row)] for i in range(ncol)]
    for i in range(0, ncol):
        for j in range(0, row):
            new_matrix[i][j] = matrix[i][j]**2
    return new_matrix
