.. title: points()
.. slug: points
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 points() documentation
.. type: text

Draw a collection of points, each a coordinate in space at the dimension of one pixel.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_points_0.png
    :alt: example picture for points()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_points = 100 * np.random.rand(500, 2)
        py5.points(random_points)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draw a collection of points, each a coordinate in space at the dimension of one pixel. The purpose of this method is to provide an alternative to repeatedly calling :doc:`point` in a loop. For a large number of points, the performance of ``points()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each point. There should be two or three columns for 2D or 3D points, respectively.

Underlying Java method: points

Syntax
======

.. code:: python

    points(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of point coordinates


Updated on April 06, 2021 18:19:03pm UTC

