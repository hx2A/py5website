.. title: begin_draw()
.. slug: py5graphics_begin_draw
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_draw() documentation
.. type: text

Sets the default properties for a PGraphics object.

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

Sets the default properties for a PGraphics object. It should be called before anything is drawn into the object.

Underlying Java method: `PGraphics.beginDraw <https://processing.org/reference/PGraphics_beginDraw_.html>`_

Syntax
======

.. code:: python

    begin_draw() -> None

Updated on November 04, 2020 20:45:44pm UTC

