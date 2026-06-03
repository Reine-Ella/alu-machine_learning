#!/usr/bin/env python3
"""Module for summation of i squared"""


def summation_i_squared(n):
    """Calculates the sum of i squared from 1 to n"""
    if not isinstance(n, int) or n < 1:
        return None

    return int(n * (n + 1) * (2 * n + 1) / 6)
