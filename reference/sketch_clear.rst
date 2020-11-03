.. title: clear()
.. slug: sketch_clear
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 clear() documentation
.. type: text

Clears the pixels within a buffer.

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
        pg = create_graphics(width, height)


    def draw():
        background(204)

        # clear the Py5Graphics when the mouse is pressed
        if mouse_pressed:
            pg.begin_draw()
            pg.clear()
            pg.end_draw()
        else:
            pg.begin_draw()
            pg.stroke(0, 102, 153)
            pg.line(width//2, height//2, mouse_x, mouse_y)
            pg.end_draw()

        image(pg, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Clears the pixels within a buffer. This function only works on ``Py5Graphics`` objects created with the ``create_graphics()`` function. Unlike the main graphics context (the display window), pixels in additional graphics areas created with ``create_graphics()`` can be entirely or partially transparent. This function clears everything in a ``Py5Graphics`` object to make all of the pixels 100% transparent.

Syntax
======

.. code:: python

    clear() -> None

Updated on November 03, 2020 22:19:57pm UTC

