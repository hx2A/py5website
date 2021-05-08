.. title: Py5Graphics.curve_vertices()
.. slug: py5graphics_curve_vertices
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.curve_vertices() documentation
.. type: text

Create a collection of curve vertices.

Description
===========

Create a collection of curve vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_curve_vertex` in a loop. For a large number of curve vertices, the performance of ``curve_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each curve vertex.  There should be two or three columns for 2D or 3D points, respectively.

This method is the same as :doc:`curve_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`curve_vertices`.

Underlying Java method: PGraphics.curveVertices

Syntax
======

.. code:: python

    curve_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of curve vertex coordinates


Updated on May 04, 2021 20:06:05pm UTC

