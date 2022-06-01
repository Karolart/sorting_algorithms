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
  
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l] for l in matrix]
