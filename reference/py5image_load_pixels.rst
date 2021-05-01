.. title: Py5Image.load_pixels()
.. slug: py5image_load_pixels
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Image.load_pixels() documentation
.. type: text

Loads the pixel data for the image into its :doc:`py5image_pixels` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_load_pixels_0.png
    :alt: example picture for load_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global my_image
        global half_image
        half_image = py5.width * py5.height//2
        my_image = py5.load_image("apples.jpg")
        my_image.load_pixels()
        for i in range(0, half_image):
            my_image.pixels[i+half_image] = my_image.pixels[i]

        my_image.update_pixels()


    def draw():
        py5.image(my_image, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Loads the pixel data for the image into its :doc:`py5image_pixels` array. This function must always be called before reading from or writing to :doc:`py5image_pixels`.

Underlying Java method: `PImage.loadPixels <https://processing.org/reference/PImage_loadPixels_.html>`_

Syntax
======

.. code:: python

    load_pixels() -> None

Updated on May 01, 2021 20:51:42pm UTC

