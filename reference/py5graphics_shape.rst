.. title: Py5Graphics.shape()
.. slug: py5graphics_shape
.. date: 2021-05-08 14:06:36 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.shape() documentation
.. type: text

Draws shapes to the Py5Graphics drawing surface.

Description
===========

Draws shapes to the Py5Graphics drawing surface. Shapes must be in the Sketch's "data" directory to load correctly. Py5 currently works with SVG, OBJ, and custom-created shapes. The ``shape`` parameter specifies the shape to display and the coordinate parameters define the location of the shape from its upper-left corner. The shape is displayed at its original size unless the ``c`` and ``d`` parameters specify a different size. The :doc:`py5graphics_shape_mode` function can be used to change the way these parameters are interpreted.

This method is the same as :doc:`shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`shape`.

Underlying Java method: PGraphics.shape

Syntax
======

.. code:: python

    shape(shape: Py5Shape, /) -> None
    shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None
    shape(shape: Py5Shape, x: float, y: float, /) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the shape
* **b**: `float` - y-coordinate of the shape
* **c**: `float` - width to display the shape
* **d**: `float` - height to display the shape
* **shape**: `Py5Shape` - the shape to display
* **x**: `float` - x-coordinate of the shape
* **y**: `float` - y-coordinate of the shape


Updated on May 08, 2021 14:06:36pm UTC

