.. title: stroke_weight()
.. slug: stroke_weight
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def setup():
        py5.stroke_weight(1)  # default
        py5.line(20, 20, 80, 20)
        py5.stroke_weight(4)  # thicker
        py5.line(20, 40, 80, 40)
        py5.stroke_weight(10)  # beastly
        py5.line(20, 70, 80, 70)

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

    stroke_weight(weight: float, /) -> None

Parameters
==========

* **weight**: `float` - the weight (in pixels) of the stroke


Updated on February 13, 2021 18:02:35pm UTC

