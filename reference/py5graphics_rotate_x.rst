.. title: Py5Graphics.rotate_x()
.. slug: py5graphics_rotate_x
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.rotate_x() documentation
.. type: text

Rotates around the x-axis the amount specified by the ``angle`` parameter.

Description
===========

Rotates around the x-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from ``0`` to ``TWO_PI``) or converted from degrees to radians with the :doc:`radians` function. Coordinates are always rotated around their relative position to the origin. Positive numbers rotate in a clockwise direction and negative numbers rotate in a counterclockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``rotate_x(PI/2)`` and then ``rotate_x(PI/2)`` is the same as ``rotate_x(PI)``. If ``rotate_x()`` is run within the ``draw()``, the transformation is reset when the loop begins again. This function requires using ``P3D`` as a third parameter to :doc:`size` as shown in the example.

This method is the same as :doc:`rotate_x` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`rotate_x`.

Underlying Java method: PGraphics.rotateX

Syntax
======

.. code:: python

    rotate_x(angle: float, /) -> None

Parameters
==========

* **angle**: `float` - angle of rotation specified in radians


Updated on May 04, 2021 20:06:05pm UTC

