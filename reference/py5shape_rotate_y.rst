.. title: rotate_y()
.. slug: py5shape_rotate_y
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 rotate_y() documentation
.. type: text

Rotates the shape around the y-axis the amount specified by the ``angle`` parameter.

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
        size(100, 100, P3D)
        s = load_shape("ohio.svg")


    def draw():
        background(204)
        shape(s)


    def mouse_pressed():
        # rotate the shape around the y-axis each time the mouse is pressed
        s.rotate_y(0.1)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Rotates the shape around the y-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to TWO_PI) or converted from degrees to radians with the ``radians()`` method.

Shapes are always rotated around the upper-left corner of their bounding box. Positive numbers rotate objects in a clockwise direction. Subsequent calls to the method accumulates the effect. For example, calling ``rotate_y(HALF_PI)`` and then ``rotate_y(HALF_PI)`` is the same as ``rotate_y(PI)``. This transformation is applied directly to the shape, it's not refreshed each time ``draw()`` is run. 

This method requires a 3D renderer. You need to use P3D as a third parameter for the ``size()`` function as shown in the example above.

Underlying Java method: `PShape.rotateY <https://processing.org/reference/PShape_rotateY_.html>`_

Syntax
======

.. code:: python

    rotate_y(angle: float) -> None

Parameters
==========

* **angle**: `float` - angle of rotation specified in radians


Updated on January 01, 1970 00:00:00am UTC

