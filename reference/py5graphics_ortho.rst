.. title: Py5Graphics.ortho()
.. slug: py5graphics_ortho
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.ortho() documentation
.. type: text

Sets an orthographic projection and defines a parallel clipping volume.

Description
===========

Sets an orthographic projection and defines a parallel clipping volume. All objects with the same dimension appear the same size, regardless of whether they are near or far from the camera. The parameters to this function specify the clipping volume where left and right are the minimum and maximum x values, top and bottom are the minimum and maximum y values, and near and far are the minimum and maximum z values. If no parameters are given, the default is used: ``ortho(-width/2, width/2, -height/2, height/2)``.

This method is the same as :doc:`ortho` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`ortho`.

Underlying Java method: PGraphics.ortho

Syntax
======

.. code:: python

    ortho() -> None
    ortho(left: float, right: float, bottom: float, top: float, /) -> None
    ortho(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

Parameters
==========

* **bottom**: `float` - bottom plane of the clipping volume
* **far**: `float` - maximum distance from the origin away from the viewer
* **left**: `float` - left plane of the clipping volume
* **near**: `float` - maximum distance from the origin to the viewer
* **right**: `float` - right plane of the clipping volume
* **top**: `float` - top plane of the clipping volume


Updated on May 04, 2021 20:06:05pm UTC

