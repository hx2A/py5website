.. title: Py5Shape.get_vertex_x()
.. slug: py5shape_get_vertex_x
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_vertex_x() documentation
.. type: text

Get the value of the x coordinate for the vertex ``index``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_vertex_x_0.png
    :alt: example picture for get_vertex_x()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s1 = py5.create_shape()
        s1.begin_shape()
        s1.vertex(20, 80)
        s1.vertex(80, 80)
        s1.vertex(50, 20)
        s1.end_shape(py5.CLOSE)
        py5.shape(s1)
        x_values = [s1.get_vertex_x(i) for i in range(s1.get_vertex_count())]
        print(s1.get_width(), min(x_values), max(x_values))  # 80, 20, 80

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_vertex_x_1.png
    :alt: example picture for get_vertex_x()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.sphere_detail(8)
        s1 = py5.create_shape(py5.SPHERE, 40)
        x_values = [s1.get_vertex_x(i) for i in range(s1.get_vertex_count())]
        py5.shape(s1, 50, 50)
        print(s1.get_width(), min(x_values), max(x_values))  # 80, -40, 40

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the value of the x coordinate for the vertex ``index``.

Underlying Java method: PShape.getVertexX

Syntax
======

.. code:: python

    get_vertex_x(index: int, /) -> float

Parameters
==========

* **index**: `int` - vertex index


Updated on May 01, 2021 20:51:42pm UTC

