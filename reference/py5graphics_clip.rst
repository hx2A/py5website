.. title: Py5Graphics.clip()
.. slug: py5graphics_clip
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.clip() documentation
.. type: text

Limits the rendering to the boundaries of a rectangle defined by the parameters.

Description
===========

Limits the rendering to the boundaries of a rectangle defined by the parameters. The boundaries are drawn based on the state of the :doc:`py5graphics_image_mode` fuction, either ``CORNER``, ``CORNERS``, or ``CENTER``.

This method is the same as :doc:`clip` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`clip`.

Underlying Java method: PGraphics.clip

Syntax
======

.. code:: python

    clip(a: float, b: float, c: float, d: float, /) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the rectangle, by default
* **b**: `float` - y-coordinate of the rectangle, by default
* **c**: `float` - width of the rectangle, by default
* **d**: `float` - height of the rectangle, by default


Updated on May 04, 2021 20:06:05pm UTC

