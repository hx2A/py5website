.. title: set_fill()
.. slug: py5shape_set_fill
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_fill() documentation
.. type: text

The ``set_fill()`` method defines the fill color of a ``Py5Shape``.

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
        global circle
        size(640, 360, P2D)
        circle = create_shape(ELLIPSE, 0, 0, 200, 200)
        circle.set_stroke(color(255))


    def draw():
        background(51)
        circle.set_fill(color(random(255)))
        translate(mouse_x, mouse_y)
        shape(circle)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``set_fill()`` method defines the fill color of a ``Py5Shape``. This method is used after shapes are created or when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example. When a shape is created with ``begin_shape()`` and ``end_shape()``, its attributes may be changed with ``fill()`` and ``stroke()`` within ``begin_shape()`` and ``end_shape()``. However, after the shape is created, only the ``set_fill()`` method can define a new fill value for the ``Py5Shape``.

Underlying Java method: `PShape.setFill <https://processing.org/reference/PShape_setFill_.html>`_

Syntax
======

.. code:: python

    set_fill(fill: bool) -> None
    set_fill(fill: int) -> None
    set_fill(index: int, fill: int) -> None

Parameters
==========

* **fill**: `bool` - missing variable description
* **fill**: `int` - missing variable description
* **index**: `int` - missing variable description


Updated on November 10, 2020 15:41:45pm UTC

