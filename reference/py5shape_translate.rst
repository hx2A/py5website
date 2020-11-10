.. title: translate()
.. slug: py5shape_translate
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 translate() documentation
.. type: text

Specifies an amount to displace the shape.

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
        # move the shape 10 pixels right each time the mouse is pressed
        s.translate(10, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies an amount to displace the shape. The ``x`` parameter specifies left/right translation, the ``y`` parameter specifies up/down translation, and the ``z`` parameter specifies translations toward/away from the screen. Subsequent calls to the method accumulates the effect. For example, calling ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as ``translate(70, 0)``. This transformation is applied directly to the shape, it's not refreshed each time ``draw()`` is run. 

Using this method with the ``z`` parameter requires using the P3D parameter in combination with size.

Underlying Java method: `PShape.translate <https://processing.org/reference/PShape_translate_.html>`_

Syntax
======

.. code:: python

    translate(x: float, y: float) -> None
    translate(x: float, y: float, z: float) -> None

Parameters
==========

* **x**: `float` - left/right translation
* **y**: `float` - up/down translation
* **z**: `float` - forward/back translation


Updated on January 01, 1970 00:00:00am UTC

