.. title: get_normal()
.. slug: py5shape_get_normal
.. date: 2021-04-27 15:39:47 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_normal() documentation
.. type: text

Get the normal vector for one of a ``Py5Shape`` object's vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_normal_0.png
    :alt: example picture for get_normal()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.directional_light(255, 255, 255, -1, -1, -1)

        py5.sphere_detail(5)
        s1 = py5.create_shape(py5.SPHERE, 30)

        for i in range(s1.get_vertex_count()):
            print(s1.get_normal(i))

        py5.shape(s1, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the normal vector for one of a ``Py5Shape`` object's vertices. A normal vector is used for drawing three dimensional shapes and surfaces, and specifies a vector perpendicular to a shape's surface which, in turn, determines how lighting affects it. Py5 attempts to automatically assign normals to shapes, and this method can be used to inspect that vector.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getNormal

Syntax
======

.. code:: python

    get_normal(index: int, /) -> NDArray[(Any,), Float]
    get_normal(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

Parameters
==========

* **index**: `int` - vertex index
* **vec**: `NDArray[(Any,), Float]` - correctly sized numpy array to store normal vector


Updated on April 27, 2021 15:39:47pm UTC

