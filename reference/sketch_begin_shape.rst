.. title: begin_shape()
.. slug: begin_shape
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_shape() documentation
.. type: text

Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more complex forms.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_0.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape()
    vertex(30, 20)
    vertex(85, 20)
    vertex(85, 75)
    vertex(30, 75)
    end_shape(CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_1.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(POINTS)
    vertex(30, 20)
    vertex(85, 20)
    vertex(85, 75)
    vertex(30, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_2.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(LINES)
    vertex(30, 20)
    vertex(85, 20)
    vertex(85, 75)
    vertex(30, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_3.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    begin_shape()
    vertex(30, 20)
    vertex(85, 20)
    vertex(85, 75)
    vertex(30, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_4.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    begin_shape()
    vertex(30, 20)
    vertex(85, 20)
    vertex(85, 75)
    vertex(30, 75)
    end_shape(CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_5.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(TRIANGLES)
    vertex(30, 75)
    vertex(40, 20)
    vertex(50, 75)
    vertex(60, 20)
    vertex(70, 75)
    vertex(80, 20)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_6.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(TRIANGLE_STRIP)
    vertex(30, 75)
    vertex(40, 20)
    vertex(50, 75)
    vertex(60, 20)
    vertex(70, 75)
    vertex(80, 20)
    vertex(90, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_7.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(TRIANGLE_FAN)
    vertex(57.5, 50)
    vertex(57.5, 15)
    vertex(92, 50)
    vertex(57.5, 85)
    vertex(22, 50)
    vertex(57.5, 15)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_8.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(QUADS)
    vertex(30, 20)
    vertex(30, 75)
    vertex(50, 75)
    vertex(50, 20)
    vertex(65, 20)
    vertex(65, 75)
    vertex(85, 75)
    vertex(85, 20)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_9.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(QUAD_STRIP)
    vertex(30, 20)
    vertex(30, 75)
    vertex(50, 20)
    vertex(50, 75)
    vertex(65, 20)
    vertex(65, 75)
    vertex(85, 20)
    vertex(85, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_shape_10.png
    :alt: example picture for begin_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape()
    vertex(20, 20)
    vertex(40, 20)
    vertex(40, 40)
    vertex(60, 40)
    vertex(60, 60)
    vertex(20, 60)
    end_shape(CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more complex forms. ``begin_shape()`` begins recording vertices for a shape and ``end_shape()`` stops recording. The value of the ``kind`` parameter tells it which types of shapes to create from the provided vertices. With no mode specified, the shape can be any irregular polygon. The parameters available for ``begin_shape()`` are POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, and QUAD_STRIP. After calling the ``begin_shape()`` function, a series of ``vertex()`` commands must follow. To stop drawing the shape, call ``end_shape()``. The ``vertex()`` function with two parameters specifies a position in 2D and the ``vertex()`` function with three parameters specifies a position in 3D. Each shape will be outlined with the current stroke color and filled with the fill color. 

Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not work within ``begin_shape()``. It is also not possible to use other shapes, such as ``ellipse()`` or ``rect()`` within ``begin_shape()``. 

The P2D and P3D renderers allow ``stroke()`` and ``fill()`` to be altered on a per-vertex basis, but the default renderer does not. Settings such as ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be changed while inside a ``begin_shape()``/``end_shape()`` block with any renderer.

Underlying Java method: `beginShape <https://processing.org/reference/beginShape_.html>`_

Syntax
======

.. code:: python

    begin_shape() -> None
    begin_shape(kind: int) -> None

Parameters
==========

* **kind**: `int` - Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP


Updated on November 10, 2020 15:41:45pm UTC

