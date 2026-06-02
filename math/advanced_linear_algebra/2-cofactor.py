#!/usr/bin/env python3
"""Calculate the cofactor matrix of a matrix."""


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
        sub_matrix = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)

    return det


def cofactor(matrix):
    """Returns the cofactor matrix of a matrix."""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    cofactor_mat = []

    for i in range(len(matrix)):
        cofactor_row = []

        for j in range(len(matrix)):
            sub_matrix = [
                row[:j] + row[j + 1:]
                for index, row in enumerate(matrix)
                if index != i
            ]

            minor_value = determinant(sub_matrix)
            cofactor_value = ((-1) ** (i + j)) * minor_value

            cofactor_row.append(cofactor_value)

        cofactor_mat.append(cofactor_row)

    return cofactor_mat
