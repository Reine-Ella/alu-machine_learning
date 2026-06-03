#!/usr/bin/env python3
"""Module for calculating the integral of a polynomial"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, int):
        return None

    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    integral = [C]

    for power, coef in enumerate(poly):
        new_coef = coef / (power + 1)

        if new_coef == int(new_coef):
            new_coef = int(new_coef)

        integral.append(new_coef)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
