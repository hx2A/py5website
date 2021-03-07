.. title: full_screen()
.. slug: full_screen
.. date: 2021-03-06 19:17:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 full_screen() documentation
.. type: text

Open a Sketch using the full size of the computer's display.

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

    # run the code at the full dimensions of the screen currently
    # selected inside the preferences window

    x = 0


    def settings():
        py5.full_screen()


    def setup():
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # if more than one screen is attached to the computer, run the
    # code at the full dimensions on the screen defined by the
    # parameter to full_screen()

    x = 0


    def settings():
        py5.full_screen(2)


    def setup():
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # run full screen using the P2D renderer on screen 2

    x = 0


    def settings():
        py5.full_screen(py5.P2D, 2)


    def setup():
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # if more than one screen is attached to the computer, run the
    # code at the full dimensions across all of the attached screens

    x = 0


    def settings():
        py5.full_screen(py5.P2D, py5.SPAN)


    def setup():
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Open a Sketch using the full size of the computer's display. This function must be called in ``settings()``. The :doc:`size` and ``full_screen()`` functions cannot both be used in the same program.

When ``full_screen()`` is used without a parameter on a computer with multiple monitors, it will (probably) draw the Sketch to the primary display. When it is used with a single parameter, this number defines the screen to display to program on (e.g. 1, 2, 3...). When used with two parameters, the first defines the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be used in place of a screen number to draw the Sketch as a full-screen window across all of the attached displays if there are more than one.

Underlying Java method: `fullScreen <https://processing.org/reference/fullScreen_.html>`_

Syntax
======

.. code:: python

    full_screen() -> None
    full_screen(display: int, /) -> None
    full_screen(renderer: str, /) -> None
    full_screen(renderer: str, display: int, /) -> None

Parameters
==========

* **display**: `int` - the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)
* **renderer**: `str` - the renderer to use, e.g. P2D, P3D, JAVA2D (default)


Updated on March 06, 2021 19:17:57pm UTC

