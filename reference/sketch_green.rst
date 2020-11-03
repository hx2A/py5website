.. title: green()
.. slug: sketch_green
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 green() documentation
.. type: text

Extracts the green value from a color, scaled to match current ``color_mode()``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_green_0.png
    :alt: example picture for green()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    c = color(20, 75, 200)  # define color 'c'
    fill(c)  # use color variable 'c' as fill color
    rect(15, 20, 35, 60)  # draw left rectangle

    green_value = green(c)  # get green in 'c'
    print(green_value)  # print "75.0"
    fill(0, green_value, 0)  # use 'green_value' in new fill
    rect(50, 20, 35, 60)  # draw right rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the green value from a color, scaled to match current ``color_mode()``. The value is always returned as a float, so be careful not to assign it to an int value.

The ``green()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can acheive the same results as ``green()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, the following two lines of code are equivalent means of getting the green value of the color value ``c``:

``g1 = green(c)  # simpler, but slower to calculate
g2 = c >> 8 & 0xFF  # very fast to calculate``

Syntax
======

.. code:: python

    green(rgb: int) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 03, 2020 22:19:57pm UTC

