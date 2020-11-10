.. title: bezier_point()
.. slug: bezier_point
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 bezier_point() documentation
.. type: text

Evaluates the Bezier at point t for points a, b, c, d.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_point_0.png
    :alt: example picture for bezier_point()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    bezier(85, 20, 10, 10, 90, 90, 15, 80)
    fill(255)
    steps = 10
    for i in range(0, steps + 1):
        t = i / float(steps)
        x = bezier_point(85, 10, 90, 15, t)
        y = bezier_point(20, 10, 90, 80, t)
        ellipse(x, y, 5, 5)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Evaluates the Bezier at point t for points a, b, c, d. The parameter t varies between 0 and 1, a and d are points on the curve, and b and c are the control points. This can be done once with the x coordinates and a second time with the y coordinates to get the location of a bezier curve at t.

Underlying Java method: `bezierPoint <https://processing.org/reference/bezierPoint_.html>`_

Syntax
======

.. code:: python

    bezier_point(a: float, b: float, c: float, d: float, t: float) -> float

Parameters
==========

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on November 10, 2020 15:41:45pm UTC

