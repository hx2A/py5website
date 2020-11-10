.. title: alpha()
.. slug: alpha
.. date: 2020-11-10 15:41:45 UTC+00:00
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

Underlying Java method: `alpha <https://processing.org/reference/alpha_.html>`_

Syntax
======

.. code:: python

    alpha(rgb: int) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 10, 2020 15:41:45pm UTC

