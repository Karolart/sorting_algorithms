#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""



def matrix_divided(matrix, div):
    """This function takes the data entered by the user and checks that there are only integer and float numbers in the array.
       The result is then taken to an array with parameters similar to those of the previous structure.
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

    check_for_list(matrix)
    check_for_divisor(div)

    elem_sizes = set()
    new_list = list()

    for elem in matrix:
        if check_for_list(elem) is False:
            raises_matrix_type_error()

        elem_sizes = check_row_size_inconsistency(elem_sizes, elem)
        values = []

        for value in elem:
            if check_for_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))

        new_list.append(values)

    return new_list


def check_for_list(value):
    """
    Check if the value is of type list
    Args:
        value (any): The value to verify.
    Raises:
        TypeError: If `value` isn't a list.
    """

    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()


def check_for_divisor(div):
    """
    Check if the divisor is integer, float or zero
    Args:
        div (any): The divisor to verify.
    Raises:
        TypeError: If `value` isn't integer or float.
        ZeroDivisionError: If `div` is equal to `0`.
    """

    if check_for_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')


def check_for_number(value):
    """Check if the value is integer or float
    Args:
        value (any): The value to verify.
    Returns:
        bool: True if successful, False otherwise.
    """

    if type(value) is not int and type(value) is not float:
        return False

    """ Check for a NaN value """
    if value != value:
        return False

    return True


def check_row_size_inconsistency(elem_sizes, row):
    """Checks the size consistency of rows in a matrix
    

    elem_sizes.add(len(row))

    if len(elem_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return elem_sizes


def raises_matrix_type_error():
    """Raises a Matrix TypeError
    Raises:
        TypeError: If `matrix` list of lists of integers or floats.
    """

    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
