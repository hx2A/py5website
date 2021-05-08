.. title: Py5Graphics.line()
.. slug: py5graphics_line
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.line() documentation
.. type: text

Draws a line (a direct path between two points) to the Py5Graphics drawing surface.

Description
===========

Draws a line (a direct path between two points) to the Py5Graphics drawing surface. The version of ``line()`` with four parameters draws the line in 2D.  To color a line, use the :doc:`py5graphics_stroke` function. A line cannot be filled, therefore the :doc:`py5graphics_fill` function will not affect the color of a line. 2D lines are drawn with a width of one pixel by default, but this can be changed with the :doc:`py5graphics_stroke_weight` function. The version with six parameters allows the line to be placed anywhere within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

This method is the same as :doc:`line` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`line`.

Underlying Java method: PGraphics.line

Syntax
======

.. code:: python

    line(x1: float, y1: float, x2: float, y2: float, /) -> None
    line(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, /) -> None

Parameters
==========

* **x1**: `float` - x-coordinate of the first point
* **x2**: `float` - x-coordinate of the second point
* **y1**: `float` - y-coordinate of the first point
* **y2**: `float` - y-coordinate of the second point
* **z1**: `float` - z-coordinate of the first point
* **z2**: `float` - z-coordinate of the second point


Updated on May 06, 2021 16:39:27pm UTC

