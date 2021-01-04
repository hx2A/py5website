.. title: rotate()
.. slug: py5shape_rotate
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 rotate() documentation
.. type: text

Rotates the shape the amount specified by the ``angle`` parameter.

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
        global s
        size(100, 100)
        s = load_shape("ohio.svg")


    def draw():
        background(204)
        shape(s)


    def mouse_pressed():
        # rotate the shape each time the mouse is pressed
        s.rotate(0.1)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Rotates the shape the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to TWO_PI) or converted from degrees to radians with the ``radians()`` method.

Shapes are always rotated around the upper-left corner of their bounding box. Positive numbers rotate objects in a clockwise direction. Transformations apply to everything that happens after and subsequent calls to the method accumulates the effect. For example, calling ``rotate(HALF_PI)`` and then ``rotate(HALF_PI)`` is the same as ``rotate(PI)``. This transformation is applied directly to the shape, it's not refreshed each time ``draw()`` is run.

Underlying Java method: `PShape.rotate <https://processing.org/reference/PShape_rotate_.html>`_

Syntax
======

.. code:: python

    rotate(angle: float, /) -> None
    rotate(angle: float, v0: float, v1: float, v2: float, /) -> None

Parameters
==========

* **angle**: `float` - angle of rotation specified in radians
* **v0**: `float` - missing variable description
* **v1**: `float` - missing variable description
* **v2**: `float` - missing variable description


Updated on November 24, 2020 21:22:32pm UTC
