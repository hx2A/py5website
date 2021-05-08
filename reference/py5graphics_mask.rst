.. title: Py5Graphics.mask()
.. slug: py5graphics_mask
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.mask() documentation
.. type: text

Masks part of the Py5Graphics drawing surface from displaying by loading an image and using it as an alpha channel.

Description
===========

Masks part of the Py5Graphics drawing surface from displaying by loading an image and using it as an alpha channel. This mask image should only contain grayscale data, but only the blue color channel is used. The mask image needs to be the same size as the image to which it is applied.

In addition to using a mask image, an integer array containing the alpha channel data can be specified directly. This method is useful for creating dynamically generated alpha masks. This array must be of the same length as the target image's pixels array and should contain only grayscale data of values between 0-255.

Underlying Java method: PGraphics.mask

Syntax
======

.. code:: python

    mask(img: Py5Image, /) -> None
    mask(mask_array: NDArray[(Any,), Int], /) -> None

Parameters
==========

* **img**: `Py5Image` - image to use as the mask
* **mask_array**: `NDArray[(Any,), Int]` - array of integers used as the alpha channel, needs to be the same length as the image's pixel array.


Updated on May 06, 2021 16:39:27pm UTC

