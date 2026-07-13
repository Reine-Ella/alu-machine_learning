#!/usr/bin/env python3
"""Performs a convolution on grayscale images with custom padding."""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Perform a convolution on grayscale images using custom padding.

    Args:
        images (numpy.ndarray): Array with shape (m, h, w).
        kernel (numpy.ndarray): Array with shape (kh, kw).
        padding (tuple): Tuple containing (ph, pw), where:
            ph is the padding for the image height.
            pw is the padding for the image width.

    Returns:
        numpy.ndarray: The convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    padded_images = np.pad(
        images,
        (
            (0, 0),
            (ph, ph),
            (pw, pw)
        ),
        mode='constant',
        constant_values=0
    )

    output_h = h + (2 * ph) - kh + 1
    output_w = w + (2 * pw) - kw + 1

    convolved_images = np.zeros((m, output_h, output_w))

    for row in range(output_h):
        for column in range(output_w):
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