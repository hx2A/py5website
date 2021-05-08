.. title: Py5Graphics.load_pixels()
.. slug: py5graphics_load_pixels
.. date: 2021-05-08 14:06:36 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.load_pixels() documentation
.. type: text

Loads the pixel data of the current Py5Graphics drawing surface into the :doc:`py5graphics_pixels` array.

Description
===========

Loads the pixel data of the current Py5Graphics drawing surface into the :doc:`py5graphics_pixels` array. This function must always be called before reading from or writing to :doc:`py5graphics_pixels`. Subsequent changes to the Py5Graphics drawing surface will not be reflected in :doc:`py5graphics_pixels` until ``load_pixels()`` is called again.

This method is the same as :doc:`load_pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`load_pixels`.

Underlying Java method: PGraphics.loadPixels

Syntax
======

.. code:: python

    load_pixels() -> None

Updated on May 08, 2021 14:06:36pm UTC

