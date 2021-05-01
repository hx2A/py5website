.. title: Py5Shape.get_fill()
.. slug: py5shape_get_fill
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_fill() documentation
.. type: text

Gets the fill color used for a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_fill_0.png
    :alt: example picture for get_fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.fill(200, 50, 50)
        s = py5.create_shape(py5.RECT, 20, 20, 60, 60)
        py5.shape(s)

        fill = s.get_fill(0)
        print(py5.red(fill), py5.green(fill), py5.blue(fill)) # 200, 50, 50

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Gets the fill color used for a ``Py5Shape`` object. This method can get the fill assigned to each vertex, but most likely the value will be the same for all vertices.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getFill

Syntax
======

.. code:: python

    get_fill(index: int, /) -> int

Parameters
==========

* **index**: `int` - vertex index


Updated on May 01, 2021 20:51:42pm UTC

