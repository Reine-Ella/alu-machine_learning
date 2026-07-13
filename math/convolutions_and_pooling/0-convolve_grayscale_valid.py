#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Perform a valid convolution on a batch of grayscale images.

    Args:
        images (numpy.ndarray): Array with shape (m, h, w), where:
            m is the number of images.
            h is the height of each image.
            w is the width of each image.
        kernel (numpy.ndarray): Array with shape (kh, kw), where:
            kh is the height of the kernel.
            kw is the width of the kernel.

    Returns:
        numpy.ndarray: The convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    output_h = h - kh + 1
    output_w = w - kw + 1

    convolved_images = np.zeros((m, output_h, output_w))

    for row in range(output_h):
        for column in range(output_w):
            image_section = images[
                :,
                row:row + kh,
                column:column + kw
            ]

            convolved_images[:, row, column] = np.sum(
                image_section * kernel,
                axis=(1, 2)
            )

    return convolved_images