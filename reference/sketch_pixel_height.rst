.. title: pixel_height
.. slug: sketch_pixel_height
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pixel_height documentation
.. type: text

When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OS X or high-dpi on Windows and Linux), the width and height of the sketch do not change, but the number of pixels is doubled.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(600, 400)
        pixel_density(2)
        print(width, height)
        print(pixel_width, pixel_height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(600, 400)
        pixel_density(2)  # double the pixel density
        print(width, height)
        print(pixel_width, pixel_height)


    def draw():
        load_pixels()
        # fill all the pixels to blue with using
        # pixel_width and pixel_height
        for i in range(0, pixel_width * pixel_height):
            pixels[i] = color(0, 0, 255)

        # fill one quarter of the pixels to yellow
        # because the pixel density is set to 2 in setup()
        # and 'width' and 'height' don't reflect the pixel
        # dimensions of the sketch
        for i in range(0, width * height):
            pixels[i] = color(255, 255, 0)

        update_pixels()
        no_loop()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OS X or high-dpi on Windows and Linux), the width and height of the sketch do not change, but the number of pixels is doubled. As a result, all operations that use pixels (like ``load_pixels()``, ``get()``, ``set()``, etc.) happen in this doubled space. As a convenience, the variables ``pixel_width`` and ``pixel_height`` hold the actual width and height of the sketch in pixels. This is useful for any sketch that uses the ``pixels[]`` array, for instance, because the number of elements in the array will be ``pixel_width*pixel_height``, not ``width*height``.


Updated on November 03, 2020 22:19:57pm UTC

