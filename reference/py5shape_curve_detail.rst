.. title: Py5Shape.curve_detail()
.. slug: py5shape_curve_detail
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.curve_detail() documentation
.. type: text

Sets the resolution at which a ``Py5Shape`` object's curves display.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_curve_detail_0.png
    :alt: example picture for curve_detail()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        py5.shape(draw_curves(30, 2, py5.color(255, 0, 0)))
        py5.shape(draw_curves(70, 20, py5.color(0, 0, 255)))


    def draw_curves(y, detail, color):
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.stroke(color)
        s.curve_detail(detail)
        s.curve_vertex(0, y)
        s.curve_vertex(10, y-10)
        s.curve_vertex(20, y)
        s.curve_vertex(50, y+20)
        s.curve_vertex(80, y)
        s.curve_vertex(90, y+10)
        s.curve_vertex(100, y)
        s.end_shape()
        return s

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the resolution at which a ``Py5Shape`` object's curves display. The default value is 20.

Drawing 2D curves requires using the ``P2D`` renderer and drawing 3D curves requires using the ``P3D`` renderer. When drawing directly with ``Py5Shape`` objects, curves do not work at all using the default renderer.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.curveDetail

Syntax
======

.. code:: python

    curve_detail(detail: int, /) -> None

Parameters
==========

* **detail**: `int` - resolution of the curves


Updated on June 28, 2021 15:16:14pm UTC

