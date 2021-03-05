.. title: pixel_width
.. slug: pixel_width
.. date: 2021-03-05 15:12:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pixel_width documentation
.. type: text

When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OSX or high-dpi on Windows and Linux), the width and height of the sketch do not change, but the number of pixels is doubled.

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

    def settings():
        py5.size(600, 400)
        py5.pixel_density(2)


    def setup():
        print(py5.width, py5.height)
        print(py5.pixel_width, py5.pixel_height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(600, 400)
        py5.pixel_density(2)  # double the pixel density


    def setup():
        print(py5.width, py5.height)
        print(py5.pixel_width, py5.pixel_height)


    def draw():
        py5.load_pixels()
        # fill all the pixels to blue with using
        # pixel_width and pixel_height
        for i in range(0, py5.pixel_width*py5.pixel_height):
            py5.pixels[i] = py5.color(0, 0, 255)

        # fill one quarter of the pixels to yellow
        # because the pixel density is set to 2 in setup()
        # and 'width' and 'height' don't reflect the pixel
        # dimensions of the sketch
        for i in range(0, py5.width*py5.height):
            py5.pixels[i] = py5.color(255, 255, 0)

        py5.update_pixels()
        py5.no_loop()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OSX or high-dpi on Windows and Linux), the width and height of the sketch do not change, but the number of pixels is doubled. As a result, all operations that use pixels (like :doc:`load_pixels`, :doc:`get`, etc.) happen in this doubled space. As a convenience, the variables ``pixel_width`` and :doc:`pixel_height` hold the actual width and height of the sketch in pixels. This is useful for any sketch that use the :doc:`pixels` or :doc:`np_pixels` arrays, for instance, because the number of elements in each array will be ``pixel_width*pixel_height``, not ``width*height``.

Underlying Java field: `pixelWidth <https://processing.org/reference/pixelWidth.html>`_


Updated on March 05, 2021 15:12:39pm UTC

