.. title: quadratic_vertices()
.. slug: quadratic_vertices
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 quadratic_vertices() documentation
.. type: text

Create a collection of quadratic vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quadratic_vertices_0.png
    :alt: example picture for quadratic_vertices()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_quadratic_vertices = 100 * np.random.rand(25, 4)
        py5.begin_shape()
        py5.vertex(py5.width / 2, py5.height / 2)
        py5.quadratic_vertices(random_quadratic_vertices)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Create a collection of quadratic vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`quadratic_vertex` in a loop. For a large number of quadratic vertices, the performance of ``quadratic_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each quadratic vertex. The first few columns are for the control point and the next few columns are for the anchor point. There should be four or six columns for 2D or 3D points, respectively.

Underlying Java method: quadraticVertices

Syntax
======

.. code:: python

    quadratic_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of quadratic vertex coordinates


Updated on April 06, 2021 18:19:03pm UTC

