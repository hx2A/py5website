.. title: Py5Graphics.circle()
.. slug: py5graphics_circle
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.circle() documentation
.. type: text

Draws a circle to the screen.

Description
===========

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the :doc:`py5graphics_ellipse_mode` function.

This method is the same as :doc:`circle` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`circle`.

Underlying Java method: PGraphics.circle

Syntax
======

.. code:: python

    circle(x: float, y: float, extent: float, /) -> None

Parameters
==========

* **extent**: `float` - width and height of the ellipse by default
* **x**: `float` - x-coordinate of the ellipse
* **y**: `float` - y-coordinate of the ellipse


Updated on May 04, 2021 20:06:05pm UTC

