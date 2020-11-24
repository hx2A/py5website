.. title: curve_detail()
.. slug: curve_detail
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 curve_detail() documentation
.. type: text

Sets the resolution at which curves display.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_curve_detail_0.png
    :alt: example picture for curve_detail()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(100, 100, P3D)
        no_fill()
        no_loop()


    def draw():
        curve_detail(1)
        draw_curves(-15)
        stroke(126)
        curve_detail(2)
        draw_curves(0)
        stroke(255)
        curve_detail(4)
        draw_curves(15)


    def draw_curves(y):
        curve(5, 28+y,  5, 28+y, 73, 26+y, 73, 63+y)
        curve(5, 28+y, 73, 26+y, 73, 63+y, 15, 67+y)
        curve(73, 26+y, 73, 63+y, 15, 67+y, 15, 67+y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the resolution at which curves display. The default value is 20. This function is only useful when using the P3D renderer as the default P2D renderer does not use this information.

Underlying Java method: `curveDetail <https://processing.org/reference/curveDetail_.html>`_

Syntax
======

.. code:: python

    curve_detail(detail: int, /) -> None

Parameters
==========

* **detail**: `int` - resolution of the curves


Updated on November 24, 2020 21:22:32pm UTC

