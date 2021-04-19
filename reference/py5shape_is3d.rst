.. title: is3d()
.. slug: py5shape_is3d
.. date: 2021-04-19 15:09:09 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 is3d() documentation
.. type: text

Boolean value reflecting if the shape is or is not a 3D shape.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_is3d_0.png
    :alt: example picture for is3d()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(30, 20)
        s.vertex(85, 20)
        s.vertex(85, 75)
        s.vertex(30, 75)
        s.end_shape(py5.CLOSE)

        print(s.is2d(), s.is3d())
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_is3d_1.png
    :alt: example picture for is3d()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(30, 20)
        s.vertex(85, 20)
        s.vertex(85, 75)
        s.vertex(30, 75)
        s.end_shape(py5.CLOSE)

        print(s.is2d(), s.is3d())
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Boolean value reflecting if the shape is or is not a 3D shape.

If the shape is created in a Sketch using the ``P3D`` renderer, this will be ``True``, even if it only uses 2D coordinates.

Underlying Java method: PShape.is3D

Syntax
======

.. code:: python

    is3d() -> bool

Updated on April 19, 2021 15:09:09pm UTC

