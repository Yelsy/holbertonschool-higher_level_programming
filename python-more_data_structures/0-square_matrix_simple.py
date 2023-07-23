#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        matrix_i = []
        new_matrix.append(matrix_i)
        for j in i:
            matrix_i.append(j ** 2)
    return new_matrix
