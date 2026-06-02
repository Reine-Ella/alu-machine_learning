#!/usr/bin/env python3
"""Calculate the determinant of a matrix."""


def determinant(matrix):
    """Returns the determinant of a square matrix."""
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    if len(matrix) == 0:
        raise ValueError("matrix must be a square matrix")

    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    det = 0

    for col in range(len(matrix)):
        minor = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(minor)

    return det
