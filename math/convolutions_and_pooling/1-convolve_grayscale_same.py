#!/usr/bin/env python3
"""Performs a same convolution on grayscale images."""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Perform a same convolution on a batch of grayscale images.

    Args:
        images (numpy.ndarray): Array with shape (m, h, w).
        kernel (numpy.ndarray): Array with shape (kh, kw).

    Returns:
        numpy.ndarray: The convolved images with shape (m, h, w).
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    pad_h = kh // 2
    pad_w = kw // 2

    padded_images = np.pad(
        images,
        (
            (0, 0),
            (pad_h, pad_h),
            (pad_w, pad_w)
        ),
        mode='constant',
        constant_values=0
    )

    convolved_images = np.zeros((m, h, w))

    for row in range(h):
        for column in range(w):
            image_section = padded_images[
                :,
                row:row + kh,
                column:column + kw
            ]

            convolved_images[:, row, column] = np.sum(
                image_section * kernel,
                axis=(1, 2)
            )

    return convolved_images