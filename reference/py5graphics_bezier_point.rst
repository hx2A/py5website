.. title: Py5Graphics.bezier_point()
.. slug: py5graphics_bezier_point
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.bezier_point() documentation
.. type: text

Evaluates the Bezier at point t for points a, b, c, d.

Description
===========

Evaluates the Bezier at point t for points a, b, c, d. The parameter t varies between 0 and 1, a and d are points on the curve, and b and c are the control points. This can be done once with the x coordinates and a second time with the y coordinates to get the location of a bezier curve at t.

This method is the same as :doc:`bezier_point` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`bezier_point`.

Underlying Java method: PGraphics.bezierPoint

Syntax
======

.. code:: python

    bezier_point(a: float, b: float, c: float, d: float, t: float, /) -> float

Parameters
==========

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on May 04, 2021 20:06:05pm UTC

