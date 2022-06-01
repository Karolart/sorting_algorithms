#!/usr/bin/python3
"""A module to divides all elements of a matrix.

This module is in charge of dividing all the values of a matrix
according to a divisor given by the user. For the program to work
properly, the following aspects must be taken into account:
    * The matrix must  must be a list of lists of integers or floats.
    * Each row of the matrix must be of the same size.
    * The divisor must be a number (integer or float) other than 0.
    * The division of all elements of the matrix is rounded off
    to 2 decimal places.
    * The result is delivered in a new matrix.

"""


def matrix_divided(matrix, div):
    """

     Function that divides all elements of a matrix.
    Args:
        matrix (int, float): Matrix to divide elements of
    Returns:
        list: New matrix

    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/fl\
oats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        for i in row:
            if (type(i) != int and type(i) != float) or i != i:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div != div or div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nonemptyflag = 0
    for row in matrix:
        if len(row) != 0:
            nonemptyflag = 1
    if nonemptyflag == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(i/div, 2) for i in row] for row in (matrix)]
