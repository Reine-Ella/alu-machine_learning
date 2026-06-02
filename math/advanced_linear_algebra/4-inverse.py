#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix"""
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
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix"""
    n = len(matrix)

    if n == 1:
        return [[1]]

    cofactors = []

    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = [
                row[:j] + row[j + 1:]
                for index, row in enumerate(matrix)
                if index != i
            ]

            cofactor = ((-1) ** (i + j)) * determinant(minor)
            cofactor_row.append(cofactor)

        cofactors.append(cofactor_row)

    return [
        [cofactors[j][i] for j in range(n)]
        for i in range(n)
    ]


def inverse(matrix):
    """Calculates the inverse of a matrix"""
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or any(row == [] for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)

    if det == 0:
        return None

    adj = adjugate(matrix)

    return [
        [element / det for element in row]
        for row in adj
    ]
