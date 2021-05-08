.. title: Py5Graphics.update_pixels()
.. slug: py5graphics_update_pixels
.. date: 2021-05-08 14:00:38 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.update_pixels() documentation
.. type: text

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_pixels` array.

Description
===========

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_pixels` array. Use in conjunction with :doc:`py5graphics_load_pixels`. If you're only reading pixels from the array, there's no need to call ``update_pixels()`` — updating is only necessary to apply changes.

Use the ``update_pixels(x, y, w, h)`` syntax to update only a subset of the pixel array. This can be faster if only some of the pixels have been changed.

This method is the same as :doc:`update_pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`update_pixels`.

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


Updated on May 08, 2021 14:00:38pm UTC

