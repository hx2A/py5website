.. title: Py5Graphics.quadratic_vertices()
.. slug: py5graphics_quadratic_vertices
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.quadratic_vertices() documentation
.. type: text

Create a collection of quadratic vertices.

Description
===========

Create a collection of quadratic vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_quadratic_vertex` in a loop. For a large number of quadratic vertices, the performance of ``quadratic_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each quadratic vertex. The first few columns are for the control point and the next few columns are for the anchor point. There should be four or six columns for 2D or 3D points, respectively.

This method is the same as :doc:`quadratic_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`quadratic_vertices`.

Underlying Java method: PGraphics.quadraticVertices

Syntax
======

.. code:: python

    quadratic_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of quadratic vertex coordinates


Updated on May 04, 2021 20:06:05pm UTC

