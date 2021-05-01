.. title: Py5Shape.set_stroke_join()
.. slug: py5shape_set_stroke_join
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.set_stroke_join() documentation
.. type: text

Sets the style of the joints which connect line segments in a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_stroke_join_0.png
    :alt: example picture for set_stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.stroke_weight(10.0)
        s.stroke_join(py5.MITER)
        s.vertex(10, 20)
        s.vertex(40, 50)
        s.vertex(10, 80)
        s.end_shape()

        py5.shape(s)
        s.set_stroke_join(py5.BEVEL)
        py5.shape(s, 25, 0)
        s.set_stroke_join(py5.ROUND)
        py5.shape(s, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the style of the joints which connect line segments in a ``Py5Shape`` object. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters ``MITER``, ``BEVEL``, and ``ROUND``. The default joint is ``MITER``.

This method differs from :doc:`py5shape_stroke_join` in that it is only to be used outside the :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` methods.

Underlying Java method: PShape.setStrokeJoin

Syntax
======

.. code:: python

    set_stroke_join(join: int, /) -> None

Parameters
==========

* **join**: `int` - either MITER, BEVEL, ROUND


Updated on May 01, 2021 20:51:42pm UTC

