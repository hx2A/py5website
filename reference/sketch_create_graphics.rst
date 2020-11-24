.. title: create_graphics()
.. slug: create_graphics
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_graphics() documentation
.. type: text

Creates and returns a new ``Py5Graphics`` object.

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
        size(200, 200)
        pg = create_graphics(100, 100)


    def draw():
        pg.begin_draw()
        pg.background(102)
        pg.stroke(255)
        pg.line(pg.width*0.5, pg.height*0.5, mouse_x, mouse_y)
        pg.end_draw()
        image(pg, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Creates and returns a new ``Py5Graphics`` object. Use this class if you need to draw into an off-screen graphics buffer. The first two parameters define the width and height in pixels. The third, optional parameter specifies the renderer. It can be defined as P2D, P3D, PDF, or SVG. If the third parameter isn't used, the default renderer is set. The PDF and SVG renderers require the filename parameter.

It's important to consider the renderer used with ``create_graphics()`` in relation to the main renderer specified in ``size()``. For example, it's only possible to use P2D or P3D with ``create_graphics()`` when one of them is defined in ``size()``. Unlike Processing 1.0, P2D and P3D use OpenGL for drawing, and when using an OpenGL renderer it's necessary for the main drawing surface to be OpenGL-based. If P2D or P3D are used as the renderer in ``size()``, then any of the options can be used with ``create_graphics()``. If the default renderer is used in ``size()``, then only the default, PDF, or SVG can be used with ``create_graphics()``.

It's important to run all drawing functions between the ``begin_draw()`` and ``end_draw()``. As the exception to this rule, ``smooth()`` should be run on the PGraphics object before ``begin_draw()``. See the reference for ``smooth()`` for more detail. 

The ``create_graphics()`` function should almost never be used inside ``draw()`` because of the memory and time needed to set up the graphics. One-time or occasional use during ``draw()`` might be acceptable, but code that calls ``create_graphics()`` at 60 frames per second might run out of memory or freeze your sketch.

Unlike the main drawing surface which is completely opaque, surfaces created with ``create_graphics()`` can have transparency. This makes it possible to draw into a graphics and maintain the alpha channel. By using ``save()`` to write a PNG or TGA file, the transparency of the graphics object will be honored.

Underlying Java method: `createGraphics <https://processing.org/reference/createGraphics_.html>`_

Syntax
======

.. code:: python

    create_graphics(w: int, h: int, /) -> Py5Graphics
    create_graphics(w: int, h: int, renderer: str, /) -> Py5Graphics
    create_graphics(w: int, h: int, renderer: str, path: str, /) -> Py5Graphics

Parameters
==========

* **h**: `int` - height in pixels
* **path**: `str` - the name of the file (can be an absolute or relative path)
* **renderer**: `str` - Either P2D, P3D, or PDF
* **w**: `int` - width in pixels


Updated on November 24, 2020 21:22:32pm UTC

