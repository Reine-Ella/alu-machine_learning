#!/usr/bin/env python3
"""Calculate the minor matrix of a matrix."""


def determinant(matrix):
    """Returns the determinant of a square matrix."""

    if matrix == [[]]:
        return 1

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    det = 0

    for col in range(len(matrix)):
        minor_matrix = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        det += ((-1) ** col) * matrix[0][col] * determinant(minor_matrix)

    return det


def minor(matrix):
    """Returns the minor matrix of a matrix."""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    minor_mat = []

    for i in range(len(matrix)):
        row_minors = []

        for j in range(len(matrix)):
            sub_matrix = [
                row[:j] + row[j + 1:]
                for index, row in enumerate(matrix)
                if index != i
            ]

            row_minors.append(determinant(sub_matrix))

        minor_mat.append(row_minors)

    return minor_mat
