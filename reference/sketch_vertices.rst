.. title: vertices()
.. slug: vertices
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 vertices() documentation
.. type: text

Create a collection of vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertices_0.png
    :alt: example picture for vertices()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_triangle_vertices = 100 * np.random.rand(25, 2)
        py5.begin_shape(py5.TRIANGLES)
        py5.vertices(random_triangle_vertices)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Create a collection of vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`vertex` in a loop. For a large number of vertices, the performance of ``vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each vertex. There should be two or three columns for 2D or 3D points, respectively.

Underlying Java method: vertices

Syntax
======

.. code:: python

    vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of vertex coordinates


Updated on April 06, 2021 18:19:03pm UTC

