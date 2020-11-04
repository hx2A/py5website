.. title: screen_y()
.. slug: sketch_screen_y
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 screen_y() documentation
.. type: text

Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.

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
        size(100, 100, P3D)


    def draw():
        background(204)

        x = mouse_x
        y = mouse_y
        z = -100

        # draw "X" at z = -100
        stroke(255)
        line(x-10, y-10, z, x+10, y+10, z)
        line(x+10, y-10, z, x-10, y+10, z)

        # draw gray line at z = 0 and same
        # y value. notice the parallax
        stroke(102)
        line(0, y, 0, width, y, 0)

        # draw black line at z = 0 to match
        # the y value element drawn at z = -100
        stroke(0)
        the_y = screen_y(x, y, z)
        line(0, the_y, 0, width, the_y, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.

Underlying Java method: `screenY <https://processing.org/reference/screenY_.html>`_

Syntax
======

.. code:: python

    screen_y(x: float, y: float) -> float
    screen_y(x: float, y: float, z: float) -> float

Parameters
==========

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on November 04, 2020 20:45:44pm UTC

