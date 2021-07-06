.. title: Py5Graphics.begin_draw()
.. slug: py5graphics_begin_draw
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.begin_draw() documentation
.. type: text

Sets the default properties for a ``Py5Graphics`` object.

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
        py5.size(200, 200, py5.P2D)
        global pg
        pg = py5.create_graphics(80, 80, py5.P2D)
        pg.begin_draw()
        pg.background(102)
        pg.stroke(255)
        pg.line(20, 20, 80, 80)
        pg.end_draw()


    def draw():
        py5.image(pg, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the default properties for a ``Py5Graphics`` object. It should be called before anything is drawn into the object.

Underlying Java method: `PGraphics.beginDraw <https://processing.org/reference/PGraphics_beginDraw_.html>`_

Syntax
======

.. code:: python

    begin_draw() -> None

Updated on June 28, 2021 15:16:14pm UTC

