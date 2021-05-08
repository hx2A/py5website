.. title: Py5Graphics.quad()
.. slug: py5graphics_quad
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.quad() documentation
.. type: text

A quad is a quadrilateral, a four sided polygon.

Description
===========

A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

This method is the same as :doc:`quad` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`quad`.

Underlying Java method: PGraphics.quad

Syntax
======

.. code:: python

    quad(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None

Parameters
==========

* **x1**: `float` - x-coordinate of the first corner
* **x2**: `float` - x-coordinate of the second corner
* **x3**: `float` - x-coordinate of the third corner
* **x4**: `float` - x-coordinate of the fourth corner
* **y1**: `float` - y-coordinate of the first corner
* **y2**: `float` - y-coordinate of the second corner
* **y3**: `float` - y-coordinate of the third corner
* **y4**: `float` - y-coordinate of the fourth corner


Updated on May 04, 2021 20:06:05pm UTC

