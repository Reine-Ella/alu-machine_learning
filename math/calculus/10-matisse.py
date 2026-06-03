#!/usr/bin/env python3
"""Module for calculating the derivative of a polynomial"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = [
        coef * power
        for power, coef in enumerate(poly)
        if power != 0
    ]

    if derivative == []:
        return [0]

    return derivative
