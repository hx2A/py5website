.. title: Py5Shape.curve_vertex()
.. slug: py5shape_curve_vertex
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.curve_vertex() documentation
.. type: text

Specifies a ``Py5Shape`` object's vertex coordinates for curves.

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

    def settings():
        py5.size(100, 100, py5.P2D)


    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.curve_vertex(84, 91)
        s.curve_vertex(84, 91)
        s.curve_vertex(68, 19)
        s.curve_vertex(21, 17)
        s.curve_vertex(32, 100)
        s.curve_vertex(32, 100)
        s.end_shape()
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies a ``Py5Shape`` object's vertex coordinates for curves. This method may only be used between :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5shape_begin_shape`. The first and last points in a series of ``curve_vertex()`` lines will be used to guide the beginning and end of the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with ``curve_vertex()`` will draw the curve between the second, third, and fourth points. The ``curve_vertex()`` method is an implementation of Catmull-Rom splines.

Drawing 2D curves requires using the ``P2D`` renderer and drawing 3D curves requires using the ``P3D`` renderer. When drawing directly with ``Py5Shape`` objects, curves do not work at all using the default renderer.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.curveVertex

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


Updated on May 01, 2021 20:51:42pm UTC

