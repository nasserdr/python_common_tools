def square_matrix_simple(matrix=[]):
    new_mat = matrix
    for i in range(0, len(matrix)):
        new_mat[i] = list(map(lambda x: x**2, matrix[i]))
    return new_mat
