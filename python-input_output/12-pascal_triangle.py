#!/usr/bin/python3
"""
    Module that create a function
"""


def pascal_triangle(n):
    """
        Function that returns a list of lists of integers
        representing the Pascal's triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    for num_row in range(n):
        row = [1]
        if num_row > 0:
            last = triangle[-1]
            for num in range(1, num_row):
                row.append(last[num - 1] + last[num])
            row.append(1)
        triangle.append(row)
    return triangle
