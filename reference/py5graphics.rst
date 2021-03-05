.. title: Py5Graphics
.. slug: py5graphics
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics documentation
.. type: text

Main graphics and rendering context, as well as the base ``API`` implementation for processing "core".

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

Main graphics and rendering context, as well as the base ``API`` implementation for processing "core". Use this class if you need to draw into an off-screen graphics buffer. A Py5Graphics object can be constructed with the :doc:`create_graphics` function. The :doc:`py5graphics_begin_draw` and :doc:`py5graphics_end_draw` methods (see example) are necessary to set up the buffer and to finalize it. The fields and methods for this class are extensive.

To create a new graphics context, use the :doc:`create_graphics` function. Do not use the syntax ``Py5Graphics()``.

Underlying Java class: `PGraphics <https://processing.org/reference/PGraphics.html>`_

This class provides the following methods and fields:

.. include:: include/py5graphics_include.rst

Updated on March 03, 2021 21:11:14pm UTC

