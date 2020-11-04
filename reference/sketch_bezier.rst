.. title: bezier()
.. slug: sketch_bezier
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 bezier() documentation
.. type: text

Draws a Bezier curve on the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_0.png
    :alt: example picture for bezier()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    stroke(255, 102, 0)
    line(85, 20, 10, 10)
    line(90, 90, 15, 80)
    stroke(0, 0, 0)
    bezier(85, 20, 10, 10, 90, 90, 15, 80)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_1.png
    :alt: example picture for bezier()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()
    stroke(255, 102, 0)
    line(30, 20, 80, 5)
    line(80, 75, 30, 75)
    stroke(0, 0, 0)
    bezier(30, 20,  80, 5,  80, 75,  30, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws a Bezier curve on the screen. These curves are defined by a series of anchor and control points. The first two parameters specify the first anchor point and the last two parameters specify the other anchor point. The middle parameters specify the control points which define the shape of the curve. Bezier curves were developed by French engineer Pierre Bezier. Using the 3D version requires rendering with P3D (see the Environment reference for more information).

Underlying Java method: `bezier <https://processing.org/reference/bezier_.html>`_

Syntax
======

.. code:: python

    bezier(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None
    bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float) -> None

Parameters
==========

* **x1**: `float` - coordinates for the first anchor point
* **x2**: `float` - coordinates for the first control point
* **x3**: `float` - coordinates for the second control point
* **x4**: `float` - coordinates for the second anchor point
* **y1**: `float` - coordinates for the first anchor point
* **y2**: `float` - coordinates for the first control point
* **y3**: `float` - coordinates for the second control point
* **y4**: `float` - coordinates for the second anchor point
* **z1**: `float` - coordinates for the first anchor point
* **z2**: `float` - coordinates for the first control point
* **z3**: `float` - coordinates for the second control point
* **z4**: `float` - coordinates for the second anchor point


Updated on November 04, 2020 20:45:44pm UTC

