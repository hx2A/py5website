.. title: square()
.. slug: square
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 square() documentation
.. type: text

Draws a square to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_square_0.png
    :alt: example picture for square()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.square(30, 20, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws a square to the screen. A square is a four-sided shape with every angle at ninety degrees and each side is the same length. By default, the first two parameters set the location of the upper-left corner, the third sets the width and height. The way these parameters are interpreted, however, may be changed with the :doc:`rect_mode` function.

Underlying Java method: `square <https://processing.org/reference/square_.html>`_

Syntax
======

.. code:: python

    square(x: float, y: float, extent: float, /) -> None

Parameters
==========

* **extent**: `float` - width and height of the rectangle by default
* **x**: `float` - x-coordinate of the rectangle by default
* **y**: `float` - y-coordinate of the rectangle by default


Updated on March 03, 2021 21:11:14pm UTC

