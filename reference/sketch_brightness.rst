.. title: brightness()
.. slug: brightness
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def setup():
        py5.no_stroke()
        py5.color_mode(py5.HSB, 255)
        c = py5.color(0, 126, 255)
        py5.fill(c)
        py5.rect(15, 20, 35, 60)
        value = py5.brightness(c)  # sets 'value' to 255
        py5.fill(value)
        py5.rect(50, 20, 35, 60)

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

    brightness(rgb: int, /) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on February 13, 2021 18:02:35pm UTC

