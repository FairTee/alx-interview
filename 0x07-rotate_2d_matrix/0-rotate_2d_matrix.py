#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise.
"""


def turn_matrix(matrix, n):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """
    Reverse the rows of a 2D matrix in place
    Args:
        matrix (list of list of int):
        The 2D matrix to reverse. The matrix is
        assumed to be a list of lists where
        each sublist represents a row.
    """

    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
    """
    n = len(matrix)

    turn_matrix(matrix, n)

    reverse_matrix(matrix)

    return matrix
