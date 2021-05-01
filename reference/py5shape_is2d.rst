.. title: Py5Shape.is2d()
.. slug: py5shape_is2d
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.is2d() documentation
.. type: text

Boolean value reflecting if the shape is or is not a 2D shape.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_is2d_0.png
    :alt: example picture for is2d()

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

.. image:: /images/reference/Py5Shape_is2d_1.png
    :alt: example picture for is2d()

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

Boolean value reflecting if the shape is or is not a 2D shape.

If the shape is created in a Sketch using the ``P3D`` renderer, this will be ``False``, even if it only uses 2D coordinates.

Underlying Java method: PShape.is2D

Syntax
======

.. code:: python

    is2d() -> bool

Updated on May 01, 2021 20:51:42pm UTC

