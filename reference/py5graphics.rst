.. title: Py5Graphics
.. slug: py5graphics
.. date: 2021-02-23 15:51:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics documentation
.. type: text

Main graphics and rendering context, as well as the base API implementation for processing "core".

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
        pg = py5.create_graphics(40, 40)


    def draw():
        pg.begin_draw()
        pg.background(100)
        pg.stroke(255)
        pg.line(20, 20, py5.mouse_x, py5.mouse_y)
        pg.end_draw()
        py5.image(pg, 9, 30)
        py5.image(pg, 51, 30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Main graphics and rendering context, as well as the base API implementation for processing "core". Use this class if you need to draw into an off-screen graphics buffer. A Py5Graphics object can be constructed with the ``create_graphics()`` function. The ``begin_draw()`` and ``end_draw()`` methods (see example) are necessary to set up the buffer and to finalize it. The fields and methods for this class are extensive.

To create a new graphics context, use the ``create_graphics()`` function. Do not use the syntax ``Py5Graphics()``.

Underlying Java class: `PGraphics <https://processing.org/reference/PGraphics.html>`_

This class provides the following methods and fields:

.. include:: include/py5graphics_include.rst

Updated on February 23, 2021 15:51:57pm UTC

