.. title: mask()
.. slug: py5image_mask
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 mask() documentation
.. type: text

Masks part of an image from displaying by loading another image and using it as an alpha channel.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_mask_0.png
    :alt: example picture for mask()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global photo
        global mask_image
        photo = py5.load_image("test.jpg")
        mask_image = py5.load_image("mask.jpg")
        photo.mask(mask_image)


    def draw():
        py5.image(photo, 0, 0)
        py5.image(photo, py5.width/4, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Masks part of an image from displaying by loading another image and using it as an alpha channel. This mask image should only contain grayscale data, but only the blue color channel is used. The mask image needs to be the same size as the image to which it is applied.

In addition to using a mask image, an integer array containing the alpha channel data can be specified directly. This method is useful for creating dynamically generated alpha masks. This array must be of the same length as the target image's pixels array and should contain only grayscale data of values between 0-255.

Underlying Java method: `PImage.mask <https://processing.org/reference/PImage_mask_.html>`_

Syntax
======

.. code:: python

    mask(img: Py5Image, /) -> None
    mask(mask_array: JArray(JInt), /) -> None

Parameters
==========

* **img**: `Py5Image` - image to use as the mask
* **mask_array**: `JArray(JInt)` - array of integers used as the alpha channel, needs to be the same length as the image's pixel array.


Updated on February 13, 2021 18:02:35pm UTC

