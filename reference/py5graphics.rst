.. title: Py5Graphics
.. slug: py5graphics
.. date: 1970-01-01 00:00:00 UTC+00:00
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
        size(100, 100)
        pg = create_graphics(40, 40)


    def draw():
        pg.begin_draw()
        pg.background(100)
        pg.stroke(255)
        pg.line(20, 20, mouse_x, mouse_y)
        pg.end_draw()
        image(pg, 9, 30)
        image(pg, 51, 30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Main graphics and rendering context, as well as the base API implementation for processing "core". Use this class if you need to draw into an off-screen graphics buffer. A PGraphics object can be constructed with the ``create_graphics()`` function. The ``begin_draw()`` and ``end_draw()`` methods (see above example) are necessary to set up the buffer and to finalize it. The fields and methods for this class are extensive. For a complete list, visit the developer's reference.

To create a new graphics context, use the ``create_graphics()`` function. Do not use the syntax ``new Py5Graphics()``.

Underlying Java class: `PGraphics <https://processing.org/reference/PGraphics.html>`_

This class provides the following methods and fields:

.. include:: include/py5graphics_include.rst

Updated on January 01, 1970 00:00:00am UTC

