.. title: screen_x()
.. slug: screen_x
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 screen_x() documentation
.. type: text

Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.

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
        # x value. notice the parallax
        stroke(102)
        line(x, 0, 0, x, height, 0)

        # draw black line at z = 0 to match
        # the x value element drawn at z = -100
        stroke(0)
        the_x = screen_x(x, y, z)
        line(the_x, 0, 0, the_x, height, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.

Underlying Java method: `screenX <https://processing.org/reference/screenX_.html>`_

Syntax
======

.. code:: python

    screen_x(x: float, y: float) -> float
    screen_x(x: float, y: float, z: float) -> float

Parameters
==========

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on January 01, 1970 00:00:00am UTC

