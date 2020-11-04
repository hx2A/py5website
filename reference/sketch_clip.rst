.. title: clip()
.. slug: sketch_clip
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 clip() documentation
.. type: text

Limits the rendering to the boundaries of a rectangle defined by the parameters.

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
        size(200, 200)
        image_mode(CENTER)


    def draw():
        background(204)
        if is_mouse_pressed():
            clip(mouse_x, mouse_y, 100, 100)
        else:
            no_clip()

        line(0, 0, width, height)
        line(0, height, width, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Limits the rendering to the boundaries of a rectangle defined by the parameters. The boundaries are drawn based on the state of the ``image_mode()`` fuction, either CORNER, CORNERS, or CENTER.

Underlying Java method: `clip <https://processing.org/reference/clip_.html>`_

Syntax
======

.. code:: python

    clip(a: float, b: float, c: float, d: float) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the rectangle, by default
* **b**: `float` - y-coordinate of the rectangle, by default
* **c**: `float` - width of the rectangle, by default
* **d**: `float` - height of the rectangle, by default


Updated on November 04, 2020 20:45:44pm UTC

