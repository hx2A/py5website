.. title: dist()
.. slug: dist
.. date: 2021-03-12 15:52:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 dist() documentation
.. type: text

Calculates the distance between two points.

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

    # Sets the background gray value based on the distance 
    # of the mouse from the center of the screen
    def draw():
      py5.no_stroke()
      d = py5.dist(py5.width/2, py5.height/2, py5.mouse_x, py5.mouse_y)
      max_dist = py5.dist(0, 0, py5.width/2, py5.height/2)
      gray = py5.remap(d, 0, max_dist, 0, 255)
      py5.fill(gray)
      py5.rect(0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the distance between two points.

Syntax
======

.. code:: python

    dist(x1: float, y1: float, x2: float, y2: float) -> float
    dist(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float

Parameters
==========

* **x1**: `float` - x-coordinate of the first point
* **x2**: `float` - x-coordinate of the second point
* **y1**: `float` - y-coordinate of the first point
* **y2**: `float` - y-coordinate of the second point
* **z1**: `float` - z-coordinate of the first point
* **z2**: `float` - z-coordinate of the second point


Updated on March 12, 2021 15:52:46pm UTC

