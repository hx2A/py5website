.. title: Py5Shape.get_normal_x()
.. slug: py5shape_get_normal_x
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_normal_x() documentation
.. type: text

Get the normal vector's x value for one of a ``Py5Shape`` object's vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_normal_x_0.png
    :alt: example picture for get_normal_x()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.directional_light(255, 255, 255, -1, -1, -1)

        py5.sphere_detail(5)
        s1 = py5.create_shape(py5.SPHERE, 30)

        for i in range(s1.get_vertex_count()):
            py5.println(s1.get_normal_x(i), s1.get_normal_y(i), s1.get_normal_z(i))

        py5.shape(s1, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the normal vector's x value for one of a ``Py5Shape`` object's vertices. A normal vector is used for drawing three dimensional shapes and surfaces, and specifies a vector perpendicular to a shape's surface which, in turn, determines how lighting affects it. Py5 attempts to automatically assign normals to shapes, and this method can be used to inspect that vector.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getNormalX

Syntax
======

.. code:: python

    get_normal_x(index: int, /) -> float

Parameters
==========

* **index**: `int` - vertex index


Updated on July 06, 2021 22:46:12pm UTC

