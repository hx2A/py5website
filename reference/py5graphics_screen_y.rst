.. title: Py5Graphics.screen_y()
.. slug: py5graphics_screen_y
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.screen_y() documentation
.. type: text

Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.

Description
===========

Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.

This method is the same as :doc:`screen_y` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`screen_y`.

Underlying Java method: PGraphics.screenY

Syntax
======

.. code:: python

    screen_y(x: float, y: float, /) -> float
    screen_y(x: float, y: float, z: float, /) -> float

Parameters
==========

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on May 04, 2021 20:06:05pm UTC

