.. title: update_pixels()
.. slug: sketch_update_pixels
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 update_pixels() documentation
.. type: text

Updates the display window with the data in the ``pixels[]`` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_update_pixels_0.png
    :alt: example picture for update_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("rockies.jpg")
    image(img, 0, 0)
    half_image = img.width * img.height//2
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

Updates the display window with the data in the ``pixels[]`` array. Use in conjunction with ``load_pixels()``. If you're only reading pixels from the array, there's no need to call ``update_pixels()`` — updating is only necessary to apply changes.

Syntax
======

.. code:: python

    update_pixels() -> None
    update_pixels(x1: int, y1: int, x2: int, y2: int) -> None

Parameters
==========

* **x1**: `int` - x-coordinate of the upper-left corner
* **x2**: `int` - width of the region
* **y1**: `int` - y-coordinate of the upper-left corner
* **y2**: `int` - height of the region


Updated on November 03, 2020 22:19:57pm UTC

