.. title: atan2()
.. slug: atan2
.. date: 2021-03-09 14:45:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 atan2() documentation
.. type: text

Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis.

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

    def draw():
        py5.background(204)
        py5.translate(py5.width/2, py5.height/2)
        a = py5.atan2(py5.mouse_y - py5.height/2, py5.mouse_x - py5.width/2)
        py5.rotate(a)
        py5.rect(-30, -5, 60, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis. Values are returned as a float in the range from ``PI`` to ``-PI``. The ``atan2()`` function is most often used for orienting geometry to the position of the cursor. Note: The y-coordinate of the point is the first parameter, and the x-coordinate is the second parameter, due the the structure of calculating the tangent.

This function makes a call to the numpy ``atan2()`` function.

Syntax
======

.. code:: python

    atan2(y: float, x: float) -> float

Parameters
==========

* **x**: `float` - x-coordinate of the point
* **y**: `float` - y-coordinate of the point


Updated on March 09, 2021 14:45:46pm UTC

