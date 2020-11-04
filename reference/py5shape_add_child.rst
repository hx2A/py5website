.. title: add_child()
.. slug: py5shape_add_child
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 add_child() documentation
.. type: text

Adds a child PShape to a parent PShape that is defined as a GROUP.

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
        global house
        size(200, 200)

        # make a group Py5Shape
        house = create_shape(GROUP)

        # make three shapes
        path = create_shape()
        path.begin_shape()
        path.vertex(-20, -20)
        path.vertex(0, -40)
        path.vertex(20, -20)
        path.end_shape()
        rectangle = create_shape(RECT, -20, -20, 40, 40)
        circle = create_shape(ELLIPSE, 0, 0, 20, 20)

        # add all three as children
        house.add_child(path)
        house.add_child(rectangle)
        house.add_child(circle)


    def draw():
        background(52)
        translate(mouse_x, mouse_y)
        shape(house)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Adds a child PShape to a parent PShape that is defined as a GROUP. In the example, the three shapes ``path``, ``rectangle``, and ``circle`` are added to a parent PShape variable named ``house`` that is a GROUP.

Underlying Java method: `PShape.addChild <https://processing.org/reference/PShape_addChild_.html>`_

Syntax
======

.. code:: python

    add_child(who: Py5Shape) -> None
    add_child(who: Py5Shape, idx: int) -> None

Parameters
==========

* **idx**: `int` - the layer position in which to insert the new child
* **who**: `Py5Shape` - any variable of type PShape


Updated on November 04, 2020 20:45:44pm UTC

