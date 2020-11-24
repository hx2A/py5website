.. title: box()
.. slug: box
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 box() documentation
.. type: text

A box is an extruded rectangle.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_box_0.png
    :alt: example picture for box()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    translate(58, 48, 0)
    rotate_y(0.5)
    no_fill()
    box(40)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_box_1.png
    :alt: example picture for box()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    translate(58, 48, 0)
    rotate_y(0.5)
    no_fill()
    box(40, 20, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

A box is an extruded rectangle. A box with equal dimensions on all sides is a cube.

Underlying Java method: `box <https://processing.org/reference/box_.html>`_

Syntax
======

.. code:: python

    box(size: float, /) -> None
    box(w: float, h: float, d: float, /) -> None

Parameters
==========

* **d**: `float` - dimension of the box in the z-dimension
* **h**: `float` - dimension of the box in the y-dimension
* **size**: `float` - dimension of the box in all dimensions (creates a cube)
* **w**: `float` - dimension of the box in the x-dimension


Updated on November 24, 2020 21:22:32pm UTC

