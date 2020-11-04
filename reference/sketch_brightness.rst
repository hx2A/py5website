.. title: brightness()
.. slug: sketch_brightness
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 brightness() documentation
.. type: text

Extracts the brightness value from a color.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_brightness_0.png
    :alt: example picture for brightness()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_stroke()
    color_mode(HSB, 255)
    c = color(0, 126, 255)
    fill(c)
    rect(15, 20, 35, 60)
    value = brightness(c)  # sets 'value' to 255
    fill(value)
    rect(50, 20, 35, 60)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the brightness value from a color.

Underlying Java method: `brightness <https://processing.org/reference/brightness_.html>`_

Syntax
======

.. code:: python

    brightness(rgb: int) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 04, 2020 20:45:44pm UTC

