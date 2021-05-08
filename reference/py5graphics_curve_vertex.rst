.. title: Py5Graphics.curve_vertex()
.. slug: py5graphics_curve_vertex
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.curve_vertex() documentation
.. type: text

Specifies vertex coordinates for curves.

Description
===========

Specifies vertex coordinates for curves. This method may only be used between :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5graphics_begin_shape`. The first and last points in a series of ``curve_vertex()`` lines will be used to guide the beginning and end of the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with ``curve_vertex()`` will draw the curve between the second, third, and fourth points. The ``curve_vertex()`` method is an implementation of Catmull-Rom splines. Using the 3D version requires rendering with ``P3D``.

This method is the same as :doc:`curve_vertex` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`curve_vertex`.

Underlying Java method: PGraphics.curveVertex

Syntax
======

.. code:: python

    curve_vertex(x: float, y: float, /) -> None
    curve_vertex(x: float, y: float, z: float, /) -> None

Parameters
==========

* **x**: `float` - the x-coordinate of the vertex
* **y**: `float` - the y-coordinate of the vertex
* **z**: `float` - the z-coordinate of the vertex


Updated on May 04, 2021 20:06:05pm UTC

