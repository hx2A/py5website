.. title: Py5Shape.bezier_vertex()
.. slug: py5shape_bezier_vertex
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.bezier_vertex() documentation
.. type: text

Specifies a ``Py5Shape`` object's vertex coordinates for Bezier curves.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_bezier_vertex_0.png
    :alt: example picture for bezier_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.vertex(30, 20)
        s.bezier_vertex(80, 0, 80, 75, 30, 75)
        s.end_shape()
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_bezier_vertex_1.png
    :alt: example picture for bezier_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(30, 20)
        s.bezier_vertex(80, 0, 80, 75, 30, 75)
        s.bezier_vertex(50, 80, 60, 25, 30, 20)
        s.end_shape()
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies a ``Py5Shape`` object's vertex coordinates for Bezier curves. Each call to ``bezier_vertex()`` defines the position of two control points and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``bezier_vertex()`` is used within a :doc:`py5shape_begin_shape` call, it must be prefaced with a call to :doc:`py5shape_vertex` to set the first anchor point. This method must be used between :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5shape_begin_shape`.

Drawing 2D bezier curves requires using the ``P2D`` renderer and drawing 3D bezier curves requires using the ``P3D`` renderer. When drawing directly with ``Py5Shape`` objects, bezier curves do not work at all using the default renderer.

Underlying Java method: PShape.bezierVertex

Syntax
======

.. code:: python

    bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
    bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

Parameters
==========

* **x2**: `float` - the x-coordinate of the 1st control point
* **x3**: `float` - the x-coordinate of the 2nd control point
* **x4**: `float` - the x-coordinate of the anchor point
* **y2**: `float` - the y-coordinate of the 1st control point
* **y3**: `float` - the y-coordinate of the 2nd control point
* **y4**: `float` - the y-coordinate of the anchor point
* **z2**: `float` - the z-coordinate of the 1st control point
* **z3**: `float` - the z-coordinate of the 2nd control point
* **z4**: `float` - the z-coordinate of the anchor point


Updated on June 28, 2021 15:16:14pm UTC

