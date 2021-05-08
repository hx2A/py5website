.. title: Py5Graphics.curve_point()
.. slug: py5graphics_curve_point
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.curve_point() documentation
.. type: text

Evaluates the curve at point ``t`` for points ``a``, ``b``, ``c``, ``d``.

Description
===========

Evaluates the curve at point ``t`` for points ``a``, ``b``, ``c``, ``d``. The parameter ``t`` may range from 0 (the start of the curve) and 1 (the end of the curve). ``a`` and ``d`` are the control points, and ``b`` and ``c`` are points on the curve. As seen in the example, this can be used once with the ``x`` coordinates and a second time with the ``y`` coordinates to get the location of a curve at ``t``.

This method is the same as :doc:`curve_point` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`curve_point`.

Underlying Java method: PGraphics.curvePoint

Syntax
======

.. code:: python

    curve_point(a: float, b: float, c: float, d: float, t: float, /) -> float

Parameters
==========

* **a**: `float` - coordinate of first control point
* **b**: `float` - coordinate of first point on the curve
* **c**: `float` - coordinate of second point on the curve
* **d**: `float` - coordinate of second control point
* **t**: `float` - value between 0 and 1


Updated on May 04, 2021 20:06:05pm UTC

