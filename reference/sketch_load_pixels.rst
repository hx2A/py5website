.. title: load_pixels()
.. slug: sketch_load_pixels
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_pixels() documentation
.. type: text

Loads the pixel data of the current display window into the ``pixels[]`` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_pixels_0.png
    :alt: example picture for load_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    half_image = width*height//2
    my_image = load_image("apples.jpg")
    image(my_image, 0, 0)

    load_pixels()
    for i in range(0, half_image):
        pixels[i+half_image] = pixels[i]

    update_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Loads the pixel data of the current display window into the ``pixels[]`` array. This function must always be called before reading from or writing to ``pixels[]``. Subsequent changes to the display window will not be reflected in ``pixels`` until ``load_pixels()`` is called again.

Syntax
======

.. code:: python

    load_pixels() -> None

Updated on November 03, 2020 22:19:57pm UTC

