#!/usr/bin/env python3
"""Performs a convolution on images with channels."""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Perform a convolution on images with multiple channels.

    Args:
        images (numpy.ndarray): Array with shape (m, h, w, c).
        kernel (numpy.ndarray): Array with shape (kh, kw, c).
        padding (tuple or str): Either:
            - 'same' for same convolution
            - 'valid' for valid convolution
            - (ph, pw) for custom padding
        stride (tuple): Tuple containing (sh, sw).

    Returns:
        numpy.ndarray: The convolved images.
    """
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(np.ceil(((h - 1) * sh + kh - h) / 2))
        pw = int(np.ceil(((w - 1) * sw + kw - w) / 2))
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding

    padded_images = np.pad(
        images,
        (
            (0, 0),
            (ph, ph),
            (pw, pw),
            (0, 0)
        ),
        mode='constant',
        constant_values=0
    )

    output_h = ((h + (2 * ph) - kh) // sh) + 1
    output_w = ((w + (2 * pw) - kw) // sw) + 1

    convolved_images = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            row_start = i * sh
            column_start = j * sw

            image_section = padded_images[
                :,
                row_start:row_start + kh,
                column_start:column_start + kw,
                :
            ]

            convolved_images[:, i, j] = np.sum(
                image_section * kernel,
                axis=(1, 2, 3)
            )

    return convolved_images