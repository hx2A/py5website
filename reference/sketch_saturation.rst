.. title: saturation()
.. slug: saturation
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 saturation() documentation
.. type: text

Extracts the saturation value from a color.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_saturation_0.png
    :alt: example picture for saturation()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_stroke()
    color_mode(HSB, 255)
    c = color(0, 126, 255)
    fill(c)
    rect(15, 20, 35, 60)
    value = saturation(c)  # sets 'value' to 126
    fill(value)
    rect(50, 20, 35, 60)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Extracts the saturation value from a color.

Underlying Java method: `saturation <https://processing.org/reference/saturation_.html>`_

Syntax
======

.. code:: python

    saturation(rgb: int, /) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on November 24, 2020 21:22:32pm UTC

