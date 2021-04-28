.. title: get_stroke()
.. slug: py5shape_get_stroke
.. date: 2021-04-28 14:26:43 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_stroke() documentation
.. type: text

Gets the stroke color used for lines and points in a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_stroke_0.png
    :alt: example picture for get_stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.stroke_weight(4)
        py5.stroke(200, 50, 50)
        s = py5.create_shape(py5.RECT, 20, 20, 60, 60)
        py5.shape(s)

        stroke = s.get_stroke(0)
        print(py5.red(stroke), py5.green(stroke), py5.blue(stroke)) # 200, 50, 50

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Gets the stroke color used for lines and points in a ``Py5Shape`` object. This method can get the stroke assigned to each vertex, but most likely the value will be the same for all vertices.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getStroke

Syntax
======

.. code:: python

    get_stroke(index: int, /) -> int

Parameters
==========

* **index**: `int` - vertex index


Updated on April 28, 2021 14:26:43pm UTC

