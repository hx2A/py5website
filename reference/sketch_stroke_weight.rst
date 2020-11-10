.. title: stroke_weight()
.. slug: stroke_weight
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 stroke_weight() documentation
.. type: text

Sets the width of the stroke used for lines, points, and the border around shapes.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_weight_0.png
    :alt: example picture for stroke_weight()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    stroke_weight(1)  # default
    line(20, 20, 80, 20)
    stroke_weight(4)  # thicker
    line(20, 40, 80, 40)
    stroke_weight(10)  # beastly
    line(20, 70, 80, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the width of the stroke used for lines, points, and the border around shapes. All widths are set in units of pixels.

Using ``point()`` with strokeWeight(1) or smaller may draw nothing to the screen, depending on the graphics settings of the computer. Workarounds include setting the pixel using ``set()`` or drawing the point using either ``circle()`` or ``square()``.

Underlying Java method: `strokeWeight <https://processing.org/reference/strokeWeight_.html>`_

Syntax
======

.. code:: python

    stroke_weight(weight: float) -> None

Parameters
==========

* **weight**: `float` - the weight (in pixels) of the stroke


Updated on January 01, 1970 00:00:00am UTC

