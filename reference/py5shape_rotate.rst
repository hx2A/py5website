.. title: Py5Shape.rotate()
.. slug: py5shape_rotate
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.rotate() documentation
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
        s = py5.load_shape("bot.svg")


    def draw():
        py5.background(204)
        py5.scale(0.2)
        py5.shape(s, py5.width//2, py5.height//2)


    def mouse_pressed():
        # rotate the shape each time the mouse is pressed
        s.rotate(0.1)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Rotates the shape the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to ``TWO_PI``) or converted from degrees to radians with the :doc:`radians` method.

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
* **v0**: `float` - x-coordinate of vector to rotate around
* **v1**: `float` - y-coordinate of vector to rotate around
* **v2**: `float` - z-coordinate of vector to rotate around


Updated on May 01, 2021 20:51:42pm UTC

