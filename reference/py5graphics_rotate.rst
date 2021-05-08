.. title: Py5Graphics.rotate()
.. slug: py5graphics_rotate
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.rotate() documentation
.. type: text

Rotates the amount specified by the ``angle`` parameter.

Description
===========

Rotates the amount specified by the ``angle`` parameter. Angles must be specified in radians (values from ``0`` to ``TWO_PI``), or they can be converted from degrees to radians with the :doc:`radians` function. 
 
The coordinates are always rotated around their relative position to the origin. Positive numbers rotate objects in a clockwise direction and negative numbers rotate in the couterclockwise direction. Transformations apply to everything that happens afterward, and subsequent calls to the function compound the effect. For example, calling ``rotate(PI/2.0)`` once and then calling ``rotate(PI/2.0)`` a second time is the same as a single ``rotate(PI)``. All tranformations are reset when ``draw()`` begins again. 
 
Technically, ``rotate()`` multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by :doc:`py5graphics_push_matrix` and :doc:`py5graphics_pop_matrix`.

This method is the same as :doc:`rotate` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`rotate`.

Underlying Java method: PGraphics.rotate

Syntax
======

.. code:: python

    rotate(angle: float, /) -> None
    rotate(angle: float, x: float, y: float, z: float, /) -> None

Parameters
==========

* **angle**: `float` - angle of rotation specified in radians
* **x**: `float` - x-coordinate of vector to rotate around
* **y**: `float` - y-coordinate of vector to rotate around
* **z**: `float` - z-coordinate of vector to rotate around


Updated on May 04, 2021 20:06:05pm UTC

