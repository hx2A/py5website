.. title: red()
.. slug: sketch_red
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 red() documentation
.. type: text

Extracts the red value from a color, scaled to match current ``color_mode()``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_red_0.png
    :alt: example picture for red()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    c = color(255, 204, 0)  # define color 'c'
    fill(c)  # use color variable 'c' as fill color
    rect(15, 20, 35, 60)  # draw left rectangle

    red_value = red(c)  # get red in 'c'
    print(red_value)  # print "255.0"
    fill(red_value, 0, 0)  # use 'red_value' in new fill
    rect(50, 20, 35, 60)  # draw right rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the red value from a color, scaled to match current ``color_mode()``. The value is always returned as a float, so be careful not to assign it to an int value.

The ``red()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can acheive the same results as ``red()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, the following two lines of code are equivalent means of getting the red value of the color value ``c``:

``r1 = red(c)  # simpler, but slower to calculate
r2 = c >> 16 & 0xFF  # very fast to calculate``

Underlying Java method: `red <https://processing.org/reference/red_.html>`_

Syntax
======

.. code:: python

    red(rgb: int) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 04, 2020 20:45:44pm UTC

