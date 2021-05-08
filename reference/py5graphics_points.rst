.. title: Py5Graphics.points()
.. slug: py5graphics_points
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.points() documentation
.. type: text

Draw a collection of points, each a coordinate in space at the dimension of one pixel.

Description
===========

Draw a collection of points, each a coordinate in space at the dimension of one pixel. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_point` in a loop. For a large number of points, the performance of ``points()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each point. There should be two or three columns for 2D or 3D points, respectively.

This method is the same as :doc:`points` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`points`.

Underlying Java method: PGraphics.points

Syntax
======

.. code:: python

    points(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of point coordinates


Updated on May 04, 2021 20:06:05pm UTC

