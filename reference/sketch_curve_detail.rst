.. title: curve_detail()
.. slug: curve_detail
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.no_fill()
        py5.no_loop()


    def draw():
        py5.curve_detail(1)
        draw_curves(-15)
        py5.stroke(126)
        py5.curve_detail(2)
        draw_curves(0)
        py5.stroke(255)
        py5.curve_detail(4)
        draw_curves(15)


    def draw_curves(y):
        py5.curve(5, 28+y,  5, 28+y, 73, 26+y, 73, 63+y)
        py5.curve(5, 28+y, 73, 26+y, 73, 63+y, 15, 67+y)
        py5.curve(73, 26+y, 73, 63+y, 15, 67+y, 15, 67+y)

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


Updated on February 13, 2021 18:02:35pm UTC

