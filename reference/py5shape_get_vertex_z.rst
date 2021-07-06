.. title: Py5Shape.get_vertex_z()
.. slug: py5shape_get_vertex_z
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_vertex_z() documentation
.. type: text

Get the value of the z coordinate for the vertex ``index``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_vertex_z_0.png
    :alt: example picture for get_vertex_z()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.sphere_detail(8)
        s1 = py5.create_shape(py5.SPHERE, 40)
        z_values = [s1.get_vertex_z(i) for i in range(s1.get_vertex_count())]
        py5.shape(s1, 50, 50)
        py5.println(s1.get_depth(), min(z_values), max(z_values))  # 80, -40, 40

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the value of the z coordinate for the vertex ``index``.

Underlying Java method: PShape.getVertexZ

Syntax
======

.. code:: python

    get_vertex_z(index: int, /) -> float

Parameters
==========

* **index**: `int` - vertex index


Updated on July 06, 2021 22:46:12pm UTC

