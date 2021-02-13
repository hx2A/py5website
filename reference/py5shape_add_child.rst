.. title: add_child()
.. slug: py5shape_add_child
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def settings():
        py5.size(200, 200)


    def setup():
        global house
        # make a group Py5Shape
        house = py5.create_shape(py5.GROUP)

        # make three shapes
        path = py5.create_shape()
        path.begin_shape()
        path.vertex(-20, -20)
        path.vertex(0, -40)
        path.vertex(20, -20)
        path.end_shape()
        rectangle = py5.create_shape(py5.RECT, -20, -20, 40, 40)
        opening = py5.create_shape(py5.ELLIPSE, 0, 0, 20, 20)

        # add all three as children
        house.add_child(path)
        house.add_child(rectangle)
        house.add_child(opening)


    def draw():
        py5.background(52)
        py5.translate(py5.mouse_x, py5.mouse_y)
        py5.shape(house)

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

    add_child(who: Py5Shape, /) -> None
    add_child(who: Py5Shape, idx: int, /) -> None

Parameters
==========

* **idx**: `int` - the layer position in which to insert the new child
* **who**: `Py5Shape` - any variable of type PShape


Updated on February 13, 2021 18:02:35pm UTC

