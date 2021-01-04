.. title: bezier_detail()
.. slug: bezier_detail
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 bezier_detail() documentation
.. type: text

Sets the resolution at which Beziers display.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # move the mouse left and right to see the detail change

    def setup():
        size(100, 100, P3D)
        no_fill()


    def draw():
        background(204)
        d = int(map(mouse_x, 0, 100, 1, 20))
        bezier_detail(d)
        bezier(85, 20, 10, 10, 90, 90, 15, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the resolution at which Beziers display. The default value is 20. This function is only useful when using the ``P3D`` renderer; the default ``P2D`` renderer does not use this information.

Underlying Java method: `bezierDetail <https://processing.org/reference/bezierDetail_.html>`_

Syntax
======

.. code:: python

    bezier_detail(detail: int, /) -> None

Parameters
==========

* **detail**: `int` - resolution of the curves


Updated on November 24, 2020 21:22:32pm UTC
