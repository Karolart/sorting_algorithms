#!/usr/bin/python3
def matrix_divided(matrix, div):
    """This function takes the data entered by the user and checks that there are only integer and float numbers in the array.
       The result is then taken to an array with parameters similar to those of the previous structure.
       In case the format of the matrix is incorrect
       or the divisor is not a number, this function
       will raise an error.
      Args:
        matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
        div (int): The divisor number.
     Returns:
        list: A new matrix with all elements divided.
     Raises:
        TypeError: If `matrix` list of lists of integers or floats or
            if `div` is not a number.
        ZeroDivisionError: If `div` is equal to `0`.
    """
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
