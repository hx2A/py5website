.. title: Py5Shape.set_stroke_weight()
.. slug: py5shape_set_stroke_weight
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.set_stroke_weight() documentation
.. type: text

Sets the width of the stroke used for lines and points in a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_stroke_weight_0.png
    :alt: example picture for set_stroke_weight()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.stroke_weight(1)
        s.vertex(20, 0)
        s.vertex(80, 0)
        s.end_shape()

        py5.shape(s, 0, 20)
        s.set_stroke_weight(4)
        py5.shape(s, 0, 40)
        s.set_stroke_weight(10)
        py5.shape(s, 0, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the width of the stroke used for lines and points in a ``Py5Shape`` object. All widths are set in units of pixels. Attempting to set this for individual vertices may not work, depending on the renderer used and other factors.

This method differs from :doc:`py5shape_stroke_weight` in that it is only to be used outside the :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` methods.

Underlying Java method: PShape.setStrokeWeight

Syntax
======

.. code:: python

    set_stroke_weight(index: int, weight: float, /) -> None
    set_stroke_weight(weight: float, /) -> None

Parameters
==========

* **index**: `int` - vertex index
* **weight**: `float` - the weight (in pixels) of the stroke


Updated on May 01, 2021 20:51:42pm UTC

