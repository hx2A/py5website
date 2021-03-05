.. title: curve_tangent()
.. slug: curve_tangent
.. date: 2021-03-05 15:12:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 curve_tangent() documentation
.. type: text

Calculates the tangent of a point on a curve.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_curve_tangent_0.png
    :alt: example picture for curve_tangent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.curve(5, 26, 73, 24, 73, 61, 15, 65)
        steps = 6
        for i in range(0, steps+1):
            t = i / steps
            x = py5.curve_point(5, 73, 73, 15, t)
            y = py5.curve_point(26, 24, 61, 65, t)
            #ellipse(x, y, 5, 5)
            tx = py5.curve_tangent(5, 73, 73, 15, t)
            ty = py5.curve_tangent(26, 24, 61, 65, t)
            a = py5.atan2(ty, tx)
            a -= py5.PI/2.0
            py5.line(x, y, py5.cos(a)*8 + x, py5.sin(a)*8 + y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the tangent of a point on a curve. There's a good definition of *tangent* on Wikipedia.

Underlying Java method: `curveTangent <https://processing.org/reference/curveTangent_.html>`_

Syntax
======

.. code:: python

    curve_tangent(a: float, b: float, c: float, d: float, t: float, /) -> float

Parameters
==========

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on March 05, 2021 15:12:39pm UTC

