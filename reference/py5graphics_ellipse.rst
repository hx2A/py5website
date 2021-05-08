.. title: Py5Graphics.ellipse()
.. slug: py5graphics_ellipse
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.ellipse() documentation
.. type: text

Draws an ellipse (oval) to the screen.

Description
===========

Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle. By default, the first two parameters set the location, and the third and fourth parameters set the shape's width and height. The origin may be changed with the :doc:`py5graphics_ellipse_mode` function.

This method is the same as :doc:`ellipse` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`ellipse`.

Underlying Java method: PGraphics.ellipse

Syntax
======

.. code:: python

    ellipse(a: float, b: float, c: float, d: float, /) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the ellipse
* **b**: `float` - y-coordinate of the ellipse
* **c**: `float` - width of the ellipse by default
* **d**: `float` - height of the ellipse by default


Updated on May 04, 2021 20:06:05pm UTC

