#!/usr/bin/env python3
"""Performs pooling on images."""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Perform pooling on multiple images.

    Args:
        images (numpy.ndarray): Array with shape (m, h, w, c).
        kernel_shape (tuple): Tuple containing (kh, kw).
        stride (tuple): Tuple containing (sh, sw).
        mode (str): Pooling type:
            - 'max' for maximum pooling
            - 'avg' for average pooling

    Returns:
        numpy.ndarray: The pooled images.
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = ((h - kh) // sh) + 1
    output_w = ((w - kw) // sw) + 1

    pooled_images = np.zeros((m, output_h, output_w, c))

    for i in range(output_h):
        for j in range(output_w):
            row_start = i * sh
            column_start = j * sw

            image_section = images[
                :,
                row_start:row_start + kh,
                column_start:column_start + kw,
                :
            ]

            if mode == 'max':
                pooled_images[:, i, j, :] = np.max(
                    image_section,
                    axis=(1, 2)
                )
            elif mode == 'avg':
                pooled_images[:, i, j, :] = np.mean(
                    image_section,
                    axis=(1, 2)
                )

    return pooled_images