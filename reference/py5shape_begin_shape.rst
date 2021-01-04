.. title: begin_shape()
.. slug: py5shape_begin_shape
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_shape() documentation
.. type: text

This method is used to start a custom shape created with the ``create_shape()`` function.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s  # the Py5Shape object
        size(100, 100)
        s = create_shape()
        s.begin_shape()
        s.fill(0, 0, 255)
        s.no_stroke()
        s.vertex(0, 0)
        s.vertex(0, 50)
        s.vertex(50, 0)
        s.end_shape()


    def draw():
        shape(s, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

This method is used to start a custom shape created with the ``create_shape()`` function. It's always and only used with ``create_shape()``.

Underlying Java method: `PShape.beginShape <https://processing.org/reference/PShape_beginShape_.html>`_

Syntax
======

.. code:: python

    begin_shape() -> None
    begin_shape(kind: int, /) -> None

Parameters
==========

* **kind**: `int` - missing variable description


Updated on November 24, 2020 21:22:32pm UTC
