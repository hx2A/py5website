.. title: blue()
.. slug: sketch_blue
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 blue() documentation
.. type: text

Extracts the blue value from a color, scaled to match current ``color_mode()``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_blue_0.png
    :alt: example picture for blue()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    c = color(175, 100, 220)  # define color 'c'
    fill(c)  # use color variable 'c' as fill color
    rect(15, 20, 35, 60)  # draw left rectangle

    blue_value = blue(c)  # get blue in 'c'
    print(blue_value)  # prints "220.0"
    fill(0, 0, blue_value)  # use 'blue_value' in new fill
    rect(50, 20, 35, 60)  # draw right rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the blue value from a color, scaled to match current ``color_mode()``. The value is always returned as a float, so be careful not to assign it to an int value.

The ``blue()`` function is easy to use and understand, but it is slower than a technique called bit masking. When working in ``color_mode(RGB, 255)``, you can acheive the same results as ``blue()`` but with greater speed by using a bit mask to remove the other color components. For example, the following two lines of code are equivalent means of getting the blue value of the color value ``c``:

``b1 = blue(c)   # simpler, but slower to calculate
b2 = c & 0xFF  # very fast to calculate``

Syntax
======

.. code:: python

    blue(rgb: int) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 03, 2020 22:19:57pm UTC

