.. title: set_stroke()
.. slug: py5shape_set_stroke
.. date: 2021-03-04 18:02:19 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_stroke() documentation
.. type: text

The ``set_stroke()`` method defines the outline color of a ``Py5Shape``.

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

    def settings():
        py5.size(640, 360, py5.P2D)


    def setup():
        global c
        c = py5.create_shape(py5.ELLIPSE, 0, 0, 200, 200)
        c.set_stroke(py5.color(255))


    def draw():
        py5.background(51)
        c.set_fill(py5.color(py5.random(255)))
        py5.translate(py5.mouse_x, py5.mouse_y)
        py5.shape(c)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``set_stroke()`` method defines the outline color of a ``Py5Shape``. This method is used after shapes are created or when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example. When a shape is created with :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape`, its attributes may be changed with :doc:`py5shape_fill` and :doc:`py5shape_stroke` within :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape`. However, after the shape is created, only the ``set_stroke()`` method can define a new stroke value for the ``Py5Shape``.

Underlying Java method: `PShape.setStroke <https://processing.org/reference/PShape_setStroke_.html>`_

Syntax
======

.. code:: python

    set_stroke(index: int, stroke: int, /) -> None
    set_stroke(stroke: bool, /) -> None
    set_stroke(stroke: int, /) -> None

Parameters
==========

* **index**: `int` - missing variable description
* **stroke**: `bool` - missing variable description
* **stroke**: `int` - missing variable description


Updated on March 04, 2021 18:02:19pm UTC

