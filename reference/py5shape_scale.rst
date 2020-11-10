.. title: scale()
.. slug: py5shape_scale
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 scale() documentation
.. type: text

Increases or decreases the size of a shape by expanding and contracting vertices.

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
        s = load_shape("bot.svg")


    def draw():
        background(204)
        shape(s)


    def mouse_pressed():
        # shrink the shape 90% each time the mouse is pressed
        s.scale(0.9)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Increases or decreases the size of a shape by expanding and contracting vertices. Shapes always scale from the relative origin of their bounding box. Scale values are specified as decimal percentages. For example, the method call ``scale(2.0)`` increases the dimension of a shape by 200%. Subsequent calls to the method multiply the effect. For example, calling ``scale(2.0)`` and then ``scale(1.5)`` is the same as ``scale(3.0)``. This transformation is applied directly to the shape; it's not refreshed each time ``draw()`` is run. 

Using this method with the ``z`` parameter requires using the P3D parameter in combination with size.

Underlying Java method: `PShape.scale <https://processing.org/reference/PShape_scale_.html>`_

Syntax
======

.. code:: python

    scale(s: float) -> None
    scale(x: float, y: float) -> None
    scale(x: float, y: float, z: float) -> None

Parameters
==========

* **s**: `float` - percentate to scale the object
* **x**: `float` - percentage to scale the object in the x-axis
* **y**: `float` - percentage to scale the object in the y-axis
* **z**: `float` - percentage to scale the object in the z-axis


Updated on November 10, 2020 15:41:45pm UTC

