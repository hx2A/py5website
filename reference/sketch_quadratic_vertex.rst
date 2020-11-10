.. title: quadratic_vertex()
.. slug: quadratic_vertex
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 quadratic_vertex() documentation
.. type: text

Specifies vertex coordinates for quadratic Bezier curves.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quadratic_vertex_0.png
    :alt: example picture for quadratic_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    stroke_weight(4)
    begin_shape()
    vertex(20, 20)
    quadratic_vertex(80, 20, 50, 50)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quadratic_vertex_1.png
    :alt: example picture for quadratic_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    stroke_weight(4)
    begin_shape()
    vertex(20, 20)
    quadratic_vertex(80, 20, 50, 50)
    quadratic_vertex(20, 80, 80, 80)
    vertex(80, 60)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies vertex coordinates for quadratic Bezier curves. Each call to ``quadratic_vertex()`` defines the position of one control point and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``quadratic_vertex()`` is used within a ``begin_shape()`` call, it must be prefaced with a call to ``vertex()`` to set the first anchor point. This function must be used between ``begin_shape()`` and ``end_shape()`` and only when there is no MODE parameter specified to ``begin_shape()``. Using the 3D version requires rendering with P3D (see the Environment reference for more information).

Underlying Java method: `quadraticVertex <https://processing.org/reference/quadraticVertex_.html>`_

Syntax
======

.. code:: python

    quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float) -> None
    quadratic_vertex(cx: float, cy: float, x3: float, y3: float) -> None

Parameters
==========

* **cx**: `float` - the x-coordinate of the control point
* **cy**: `float` - the y-coordinate of the control point
* **cz**: `float` - the z-coordinate of the control point
* **x3**: `float` - the x-coordinate of the anchor point
* **y3**: `float` - the y-coordinate of the anchor point
* **z3**: `float` - the z-coordinate of the anchor point


Updated on January 01, 1970 00:00:00am UTC

