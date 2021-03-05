.. title: curve_vertex()
.. slug: curve_vertex
.. date: 2021-03-05 15:12:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 curve_vertex() documentation
.. type: text

Specifies vertex coordinates for curves.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_curve_vertex_0.png
    :alt: example picture for curve_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.begin_shape()
        py5.curve_vertex(84, 91)
        py5.curve_vertex(84, 91)
        py5.curve_vertex(68, 19)
        py5.curve_vertex(21, 17)
        py5.curve_vertex(32, 100)
        py5.curve_vertex(32, 100)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies vertex coordinates for curves. This function may only be used between :doc:`begin_shape` and :doc:`end_shape` and only when there is no ``MODE`` parameter specified to :doc:`begin_shape`. The first and last points in a series of ``curve_vertex()`` lines will be used to guide the beginning and end of a the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with ``curve_vertex()`` will draw the curve between the second, third, and fourth points. The ``curve_vertex()`` function is an implementation of Catmull-Rom splines. Using the 3D version requires rendering with ``P3D`` (see the Environment reference for more information).

Underlying Java method: `curveVertex <https://processing.org/reference/curveVertex_.html>`_

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


Updated on March 05, 2021 15:12:39pm UTC

