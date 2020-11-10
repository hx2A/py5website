.. title: end_draw()
.. slug: py5graphics_end_draw
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_draw() documentation
.. type: text

Finalizes the rendering of a PGraphics object so that it can be shown on screen.

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

    def setup():
        global pg
        size(100, 100)
        pg = create_graphics(80, 80, P2D)
        pg.begin_draw()
        pg.background(102)
        pg.stroke(255)
        pg.line(20, 20, 80, 80)
        pg.end_draw()
        no_loop()


    def draw():
        image(pg, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Finalizes the rendering of a PGraphics object so that it can be shown on screen.

Underlying Java method: `PGraphics.endDraw <https://processing.org/reference/PGraphics_endDraw_.html>`_

Syntax
======

.. code:: python

    end_draw() -> None

Updated on November 10, 2020 15:41:45pm UTC

