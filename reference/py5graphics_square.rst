.. title: Py5Graphics.square()
.. slug: py5graphics_square
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.square() documentation
.. type: text

Draws a square to the Py5Graphics drawing surface.

Description
===========

Draws a square to the Py5Graphics drawing surface. A square is a four-sided shape with every angle at ninety degrees and each side is the same length. By default, the first two parameters set the location of the upper-left corner, the third sets the width and height. The way these parameters are interpreted, however, may be changed with the :doc:`py5graphics_rect_mode` function.

This method is the same as :doc:`square` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`square`.

Underlying Java method: PGraphics.square

Syntax
======

.. code:: python

    square(x: float, y: float, extent: float, /) -> None

Parameters
==========

* **extent**: `float` - width and height of the rectangle by default
* **x**: `float` - x-coordinate of the rectangle by default
* **y**: `float` - y-coordinate of the rectangle by default


Updated on May 07, 2021 21:23:50pm UTC

