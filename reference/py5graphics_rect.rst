.. title: Py5Graphics.rect()
.. slug: py5graphics_rect
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.rect() documentation
.. type: text

Draws a rectangle to the Py5Graphics drawing surface.

Description
===========

Draws a rectangle to the Py5Graphics drawing surface. A rectangle is a four-sided shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, however, may be changed with the :doc:`py5graphics_rect_mode` function.

To draw a rounded rectangle, add a fifth parameter, which is used as the radius value for all four corners.

To use a different radius value for each corner, include eight parameters. When using eight parameters, the latter four set the radius of the arc at each corner separately, starting with the top-left corner and moving clockwise around the rectangle.

This method is the same as :doc:`rect` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`rect`.

Underlying Java method: PGraphics.rect

Syntax
======

.. code:: python

    rect(a: float, b: float, c: float, d: float, /) -> None
    rect(a: float, b: float, c: float, d: float, r: float, /) -> None
    rect(a: float, b: float, c: float, d: float, tl: float, tr: float, br: float, bl: float, /) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the rectangle by default
* **b**: `float` - y-coordinate of the rectangle by default
* **bl**: `float` - radius for bottom-left corner
* **br**: `float` - radius for bottom-right corner
* **c**: `float` - width of the rectangle by default
* **d**: `float` - height of the rectangle by default
* **r**: `float` - radii for all four corners
* **tl**: `float` - radius for top-left corner
* **tr**: `float` - radius for top-right corner


Updated on May 07, 2021 21:23:50pm UTC

