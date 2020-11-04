.. title: get_child()
.. slug: py5shape_get_child
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_child() documentation
.. type: text

Extracts a child shape from a parent shape.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_child_0.png
    :alt: example picture for get_child()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global states
        global ohio
        size(100, 100)
        states = load_shape("tristate.svg")
        ohio = states.get_child("OH")
        ohio.disable_style()


    def draw():
        background(0)
        shape(states, -48, 5)
        fill(102, 0, 0)
        shape(ohio, -48, 5)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts a child shape from a parent shape. Specify the name of the shape with the ``target`` parameter. The shape is returned as a ``Py5Shape`` object, or ``None`` is returned if there is an error.

Underlying Java method: `PShape.getChild <https://processing.org/reference/PShape_getChild_.html>`_

Syntax
======

.. code:: python

    get_child(index: int) -> Py5Shape
    get_child(target: str) -> Py5Shape

Parameters
==========

* **index**: `int` - the layer position of the shape to get
* **target**: `str` - the name of the shape to get


Updated on November 04, 2020 20:45:44pm UTC

