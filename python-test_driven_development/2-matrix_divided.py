#!/usr/bin/python3
"""Module to create a function to divide elements in matrix"""


def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix.
        Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    for row in matrix:
        for j in row:
            if not isinstance(j, int) and not isinstance(j, int):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = [[round(j / div, 2) for j in row] for row in matrix]
    return new_list
