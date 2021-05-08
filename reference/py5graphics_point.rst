.. title: Py5Graphics.point()
.. slug: py5graphics_point
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.point() documentation
.. type: text

Draws a point, a coordinate in space at the dimension of one pixel.

Description
===========

Draws a point, a coordinate in space at the dimension of one pixel. The first parameter is the horizontal value for the point, the second value is the vertical value for the point, and the optional third value is the depth value. Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

Use :doc:`py5graphics_stroke` to set the color of a ``point()``.

Point appears round with the default ``stroke_cap(ROUND)`` and square with ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no cap).

Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the Py5Graphics drawing surface, depending on the graphics settings of the computer. Workarounds include setting the pixel using the :doc:`py5graphics_pixels` or :doc:`py5graphics_np_pixels` arrays or drawing the point using either :doc:`py5graphics_circle` or :doc:`py5graphics_square`.

This method is the same as :doc:`point` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`point`.

Underlying Java method: PGraphics.point

Syntax
======

.. code:: python

    point(x: float, y: float, /) -> None
    point(x: float, y: float, z: float, /) -> None

Parameters
==========

* **x**: `float` - x-coordinate of the point
* **y**: `float` - y-coordinate of the point
* **z**: `float` - z-coordinate of the point


Updated on May 06, 2021 16:39:27pm UTC

