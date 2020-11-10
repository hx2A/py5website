.. title: redraw()
.. slug: redraw
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 redraw() documentation
.. type: text

Executes the code within ``draw()`` one time.

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

    x = 0


    def setup():
        size(200, 200)
        no_loop()


    def draw():
        background(204)
        line(x, 0, x, height)


    def mouse_pressed():
        x += 1
        redraw()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Executes the code within ``draw()`` one time. This functions allows the program to update the display window only when necessary, for example when an event registered by ``mouse_pressed()`` or ``key_pressed()`` occurs. 

In structuring a program, it only makes sense to call ``redraw()`` within events such as ``mouse_pressed()``. This is because ``redraw()`` does not run ``draw()`` immediately (it only sets a flag that indicates an update is needed). 

The ``redraw()`` function does not work properly when called inside ``draw()``. To enable/disable animations, use ``loop()`` and ``no_loop()``.

Underlying Java method: `redraw <https://processing.org/reference/redraw_.html>`_

Syntax
======

.. code:: python

    redraw() -> None

Updated on January 01, 1970 00:00:00am UTC

