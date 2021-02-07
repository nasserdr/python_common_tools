#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for i in range(0, len(matrix)):
        new_mat[i] = list(map(lambda x: x**2, matrix[i]))
    return new_mat
