.. title: hue()
.. slug: hue
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 hue() documentation
.. type: text

Extracts the hue value from a color.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_hue_0.png
    :alt: example picture for hue()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_stroke()
    color_mode(HSB, 255)
    c = color(0, 126, 255)
    fill(c)
    rect(15, 20, 35, 60)
    value = hue(c)  # sets 'value' to "0"
    fill(value)
    rect(50, 20, 35, 60)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the hue value from a color.

Underlying Java method: `hue <https://processing.org/reference/hue_.html>`_

Syntax
======

.. code:: python

    hue(rgb: int, /) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 24, 2020 21:22:32pm UTC

