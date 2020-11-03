.. title: bezier_vertex()
.. slug: sketch_bezier_vertex
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 bezier_vertex() documentation
.. type: text

Specifies vertex coordinates for Bezier curves.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_vertex_0.png
    :alt: example picture for bezier_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    begin_shape()
    vertex(30, 20)
    bezier_vertex(80, 0, 80, 75, 30, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_vertex_1.png
    :alt: example picture for bezier_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape()
    vertex(30, 20)
    bezier_vertex(80, 0, 80, 75, 30, 75)
    bezier_vertex(50, 80, 60, 25, 30, 20)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies vertex coordinates for Bezier curves. Each call to ``bezier_vertex()`` defines the position of two control points and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``bezier_vertex()`` is used within a ``begin_shape()`` call, it must be prefaced with a call to ``vertex()`` to set the first anchor point. This function must be used between ``begin_shape()`` and ``end_shape()`` and only when there is no MODE parameter specified to ``begin_shape()``. Using the 3D version requires rendering with P3D (see the Environment reference for more information).

Syntax
======

.. code:: python

    bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None
    bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float) -> None

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


Updated on November 03, 2020 22:19:57pm UTC

