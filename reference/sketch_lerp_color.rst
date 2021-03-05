.. title: lerp_color()
.. slug: lerp_color
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 lerp_color() documentation
.. type: text

Calculates a color between two colors at a specific increment.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lerp_color_0.png
    :alt: example picture for lerp_color()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.stroke(255)
        py5.background(51)
        from_ = py5.color(204, 102, 0)
        to = py5.color(0, 102, 153)
        inter_a = py5.lerp_color(from_, to, .33)
        inter_b = py5.lerp_color(from_, to, .66)
        py5.fill(from_)
        py5.rect(10, 20, 20, 60)
        py5.fill(inter_a)
        py5.rect(30, 20, 20, 60)
        py5.fill(inter_b)
        py5.rect(50, 20, 20, 60)
        py5.fill(to)
        py5.rect(70, 20, 20, 60)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates a color between two colors at a specific increment. The ``amt`` parameter is the amount to interpolate between the two values where 0.0 is equal to the first point, 0.1 is very near the first point, 0.5 is halfway in between, etc. 

An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped at 1. This is different from the behavior of :doc:`lerp`, but necessary because otherwise numbers outside the range will produce strange and unexpected colors.

Underlying Java method: `lerpColor <https://processing.org/reference/lerpColor_.html>`_

Syntax
======

.. code:: python

    lerp_color(c1: int, c2: int, amt: float, /) -> int
    lerp_color(c1: int, c2: int, amt: float, mode: int, /) -> int

Parameters
==========

* **amt**: `float` - between 0.0 and 1.0
* **c1**: `int` - interpolate from this color
* **c2**: `int` - interpolate to this color
* **mode**: `int` - missing variable description


Updated on March 03, 2021 21:11:14pm UTC

