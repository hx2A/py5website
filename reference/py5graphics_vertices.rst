.. title: Py5Graphics.vertices()
.. slug: py5graphics_vertices
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.vertices() documentation
.. type: text

Create a collection of vertices.

Description
===========

Create a collection of vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_vertex` in a loop. For a large number of vertices, the performance of ``vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each vertex. There should be two or three columns for 2D or 3D points, respectively.

This method is the same as :doc:`vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`vertices`.

Underlying Java method: PGraphics.vertices

Syntax
======

.. code:: python

    vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of vertex coordinates


Updated on May 04, 2021 20:06:05pm UTC

