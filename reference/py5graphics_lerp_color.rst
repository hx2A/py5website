.. title: Py5Graphics.lerp_color()
.. slug: py5graphics_lerp_color
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.lerp_color() documentation
.. type: text

Calculates a color between two colors at a specific increment.

Description
===========

Calculates a color between two colors at a specific increment. The ``amt`` parameter is the amount to interpolate between the two values where 0.0 is equal to the first point, 0.1 is very near the first point, 0.5 is halfway in between, etc. 

An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped at 1. This is different from the behavior of :doc:`lerp`, but necessary because otherwise numbers outside the range will produce strange and unexpected colors.

This method is the same as :doc:`lerp_color` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`lerp_color`.

Underlying Java method: PGraphics.lerpColor

Syntax
======

.. code:: python

    lerp_color(c1: int, c2: int, amt: float, /) -> int
    lerp_color(c1: int, c2: int, amt: float, mode: int, /) -> int

Parameters
==========

* **amt**: `float` - between 0.0 and 1.0
* **c1**: `int` - interpolate from this color
* **c2**: `int` - interpolate to this color
* **mode**: `int` - either RGB or HSB


Updated on May 04, 2021 20:06:05pm UTC

