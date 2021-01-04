.. title: line()
.. slug: line
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 line() documentation
.. type: text

Draws a line (a direct path between two points) to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_line_0.png
    :alt: example picture for line()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    line(30, 20, 85, 75)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_line_1.png
    :alt: example picture for line()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    line(30, 20, 85, 20)
    stroke(126)
    line(85, 20, 85, 75)
    stroke(255)
    line(85, 75, 30, 75)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_line_2.png
    :alt: example picture for line()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # drawing lines in 3D requires P3D
    # as a parameter to size()
    size(100, 100, P3D)
    line(30, 20, 0, 85, 20, 15)
    stroke(126)
    line(85, 20, 15, 85, 75, 0)
    stroke(255)
    line(85, 75, 0, 30, 75, -50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws a line (a direct path between two points) to the screen. The version of ``line()`` with four parameters draws the line in 2D.  To color a line, use the ``stroke()`` function. A line cannot be filled, therefore the ``fill()`` function will not affect the color of a line. 2D lines are drawn with a width of one pixel by default, but this can be changed with the ``stroke_weight()`` function. The version with six parameters allows the line to be placed anywhere within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the P3D parameter in combination with ``size()`` as shown in the above example.

Underlying Java method: `line <https://processing.org/reference/line_.html>`_

Syntax
======

.. code:: python

    line(x1: float, y1: float, x2: float, y2: float, /) -> None
    line(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, /) -> None

Parameters
==========

* **x1**: `float` - x-coordinate of the first point
* **x2**: `float` - x-coordinate of the second point
* **y1**: `float` - y-coordinate of the first point
* **y2**: `float` - y-coordinate of the second point
* **z1**: `float` - z-coordinate of the first point
* **z2**: `float` - z-coordinate of the second point


Updated on November 24, 2020 21:22:32pm UTC
