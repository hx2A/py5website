.. title: Py5Graphics.curve_tangent()
.. slug: py5graphics_curve_tangent
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.curve_tangent() documentation
.. type: text

Calculates the tangent of a point on a curve.

Description
===========

Calculates the tangent of a point on a curve. There's a good definition of *tangent* on Wikipedia.

This method is the same as :doc:`curve_tangent` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`curve_tangent`.

Underlying Java method: PGraphics.curveTangent

Syntax
======

.. code:: python

    curve_tangent(a: float, b: float, c: float, d: float, t: float, /) -> float

Parameters
==========

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on May 04, 2021 20:06:05pm UTC

