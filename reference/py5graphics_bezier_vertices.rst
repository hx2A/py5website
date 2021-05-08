.. title: Py5Graphics.bezier_vertices()
.. slug: py5graphics_bezier_vertices
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.bezier_vertices() documentation
.. type: text

Create a collection of bezier vertices.

Description
===========

Create a collection of bezier vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_bezier_vertex` in a loop. For a large number of bezier vertices, the performance of ``bezier_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each bezier vertex. The first few columns are for the first control point, the next few columns are for the second control point, and the final few columns are for the anchor point. There should be six or nine columns for 2D or 3D points, respectively.

This method is the same as :doc:`bezier_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`bezier_vertices`.

Underlying Java method: PGraphics.bezierVertices

Syntax
======

.. code:: python

    bezier_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of bezier vertex coordinates


Updated on May 04, 2021 20:06:05pm UTC

