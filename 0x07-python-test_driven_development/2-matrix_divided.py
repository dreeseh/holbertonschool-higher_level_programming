#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides matrix by div and rounds to the hundredths
    """

    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) of integers\
                         /floats')

    matrix_length = len(matrix[0])
    for i in matrix:
        if len(i) != matrix_length:
            raise TypeError('Each row of the matrix must have the same size')
        for y in i:
            if not isinstance(y, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of\
                                 integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    final_matrix = []
    for i in matrix:
        new_matrix = []
        for y in i:
            new_matrix.append(round(y / div, 2))
        final_matrix.append(new_matrix)

    return final_matrix
