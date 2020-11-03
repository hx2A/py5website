.. title: full_screen()
.. slug: sketch_full_screen
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 full_screen() documentation
.. type: text

This function is new for Processing 3.0.

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


    def setup():
        full_screen()
        background(0)
        no_stroke()
        fill(102)


    def draw():
        rect(x, height*0.2, 1, height*0.6)
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


    def setup():
        full_screen(2)
        background(0)
        no_stroke()
        fill(102)


    def draw():
        rect(x, height*0.2, 1, height*0.6)
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


    def setup():
        full_screen(P2D, 2)
        background(0)
        no_stroke()
        fill(102)


    def draw():
        rect(x, height*0.2, 1, height*0.6)
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


    def setup():
        full_screen(P2D, SPAN)
        background(0)
        no_stroke()
        fill(102)


    def draw():
        rect(x, height*0.2, 1, height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

This function is new for Processing 3.0. It opens a sketch using the full size of the computer's display. This function must be the first line in ``setup()``. The ``size()`` and ``full_screen()`` functions cannot both be used in the same program, just choose one.

When ``full_screen()`` is used without a parameter, it draws the sketch to the screen currently selected inside the Preferences window. When it is used with a single parameter, this number defines the screen to display to program on (e.g. 1, 2, 3...). When used with two parameters, the first defines the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be used in place of a screen number to draw the sketch as a full-screen window across all of the attached displays if there are more than one.

Prior to Processing 3.0, a full-screen program was defined with ``size(display_width, display_height)``.

Syntax
======

.. code:: python

    full_screen() -> None
    full_screen(display: int) -> None
    full_screen(renderer: str) -> None
    full_screen(renderer: str, display: int) -> None

Parameters
==========

* **display**: `int` - the screen to run the sketch on (1, 2, 3, etc. or on multiple screens using SPAN)
* **renderer**: `str` - the renderer to use, e.g. P2D, P3D, JAVA2D (default)


Updated on November 03, 2020 22:19:57pm UTC

