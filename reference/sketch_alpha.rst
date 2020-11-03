.. title: alpha()
.. slug: sketch_alpha
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 alpha() documentation
.. type: text

Extracts the alpha value from a color.

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

    no_stroke()
    c = color(0, 126, 255, 102)
    fill(c)
    rect(15, 15, 35, 70)
    value = alpha(c)  # sets 'value' to 102
    fill(value)
    rect(50, 15, 35, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the alpha value from a color.

Syntax
======

.. code:: python

    alpha(rgb: int) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 03, 2020 22:19:57pm UTC

