.. title: bezier_tangent()
.. slug: sketch_bezier_tangent
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 bezier_tangent() documentation
.. type: text

Calculates the tangent of a point on a Bezier curve.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_tangent_0.png
    :alt: example picture for bezier_tangent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    bezier(85, 20, 10, 10, 90, 90, 15, 80)
    steps = 6
    fill(255)
    for i in range(0, steps + 1):
        t = i / float(steps)
        # get the location of the point
        x = bezier_point(85, 10, 90, 15, t)
        y = bezier_point(20, 10, 90, 80, t)
        # get the tangent points
        tx = bezier_tangent(85, 10, 90, 15, t)
        ty = bezier_tangent(20, 10, 90, 80, t)
        # calculate an angle from_ the tangent points
        a = atan2(ty, tx)
        a += PI
        stroke(255, 102, 0)
        line(x, y, cos(a)*30 + x, sin(a)*30 + y)
        # the following line of code makes a line
        # inverse of the above line
        #line(x, y, cos(a)*-30 + x, sin(a)*-30 + y)
        stroke(0)
        ellipse(x, y, 5, 5)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_tangent_1.png
    :alt: example picture for bezier_tangent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    bezier(85, 20, 10, 10, 90, 90, 15, 80)
    stroke(255, 102, 0)
    steps = 16
    for i in range(0, steps + 1):
        t = i / float(steps)
        x = bezier_point(85, 10, 90, 15, t)
        y = bezier_point(20, 10, 90, 80, t)
        tx = bezier_tangent(85, 10, 90, 15, t)
        ty = bezier_tangent(20, 10, 90, 80, t)
        a = atan2(ty, tx)
        a -= HALF_PI
        line(x, y, cos(a)*8 + x, sin(a)*8 + y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the tangent of a point on a Bezier curve. There is a good definition of *tangent* on Wikipedia.

Syntax
======

.. code:: python

    bezier_tangent(a: float, b: float, c: float, d: float, t: float) -> float

Parameters
==========

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on November 03, 2020 22:19:57pm UTC

