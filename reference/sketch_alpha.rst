.. title: alpha()
.. slug: alpha
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 alpha() documentation
.. type: text

Extracts the alpha value from a color, scaled to match current :doc:`color_mode`.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_alpha_0.png
    :alt: example picture for alpha()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        c = py5.color(0, 126, 255, 102)
        py5.fill(c)
        py5.rect(15, 15, 35, 70)
        value = py5.alpha(c)  # sets 'value' to 102
        py5.fill(value)
        py5.rect(50, 15, 35, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the alpha value from a color, scaled to match current :doc:`color_mode`. The value is always returned as a float, so be careful not to assign it to an int value.

The ``alpha()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``alpha()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``alpha(c)`` and ``c >> 24 & 0xFF`` both extract the alpha value from a color variable ``c`` but the later is faster.

Underlying Java method: `alpha <https://processing.org/reference/alpha_.html>`_

Syntax
======

.. code:: python

    alpha(rgb: int, /) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on March 03, 2021 21:11:14pm UTC

