.. title: Py5Graphics.update_pixels()
.. slug: py5graphics_update_pixels
.. date: 2021-05-11 00:43:18 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.update_pixels() documentation
.. type: text

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_pixels` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_update_pixels_0.png
    :alt: example picture for update_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        g = py5.create_graphics(60, 60)
        g.begin_draw()
        g.background(255, 0, 0)
        g.rect(10, 10, 40, 40)
        g.load_pixels()
        yellow = py5.color(255, 255, 0)
        for i in range(len(g.pixels) // 2):
            g.pixels[i] = yellow
        g.update_pixels()
        g.end_draw()

        py5.background(240)
        py5.image(g, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_pixels` array. Use in conjunction with :doc:`py5graphics_load_pixels`. If you're only reading pixels from the array, there's no need to call ``update_pixels()`` — updating is only necessary to apply changes.

Use the ``update_pixels(x, y, w, h)`` syntax to update only a subset of the pixel array. This can be faster if only some of the pixels have been changed.

This method is the same as :doc:`update_pixels` but linked to a ``Py5Graphics`` object.

Underlying Java method: PGraphics.updatePixels

Syntax
======

.. code:: python

    update_pixels() -> None
    update_pixels(x: int, y: int, w: int, h: int, /) -> None

Parameters
==========

* **h**: `int` - height of pixel rectangle to update
* **w**: `int` - width of pixel rectangle to update
* **x**: `int` - x-coordinate of the upper left hand corner of rectangle to update
* **y**: `int` - y-coordinate of the upper left hand corner of rectangle to update


Updated on May 11, 2021 00:43:18am UTC

