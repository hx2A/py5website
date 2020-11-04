.. title: smooth()
.. slug: sketch_smooth
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 smooth() documentation
.. type: text

Draws all geometry with smooth (anti-aliased) edges.

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
        size(100, 100)
        smooth(2)
        no_stroke()


    def draw():
        background(0)
        ellipse(30, 48, 36, 36)
        ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    x = 0


    def setup():
        full_screen(P2D, SPAN)
        smooth(4)


    def draw():
        background(0)
        ellipse(x, height//2, height/4, height/4)
        x += 1

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    x = 0


    def setup():
        global pg
        full_screen(P2D)
        pg = create_graphics(width, height, P2D)
        pg.smooth(4)


    def draw():
        pg.begin_draw()
        pg.background(0)
        pg.ellipse(x, height//2, height/4, height/4)
        pg.end_draw()
        image(pg, 0, 0)
        x += 1

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws all geometry with smooth (anti-aliased) edges. This behavior is the default, so ``smooth()`` only needs to be used when a program needs to set the smoothing in a different way. The ``level`` parameter increases the amount of smoothness. This is the level of over sampling applied to the graphics buffer.

With the P2D and P3D renderers, ``smooth(2)`` is the default, this is called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing level is determined by the hardware of the machine that is running the software, so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing. The other option for the default renderer is ``smooth(2)``, which is bilinear smoothing.

With Processing 3.0, ``smooth()`` is different than before. It was common to use ``smooth()`` and ``no_smooth()`` to turn on and off antialiasing within a sketch. Now, because of how the software has changed, ``smooth()`` can only be set once within a sketch. It can be used either at the top of a sketch without a ``setup()``, or after the ``size()`` function when used in a sketch with ``setup()``. The ``no_smooth()`` function also follows the same rules. 

When ``smooth()`` is used with a ``Py5Graphics`` object, it should be run right after the object is created with ``create_graphics()``, as shown in the Reference in the third example.

Underlying Java method: `smooth <https://processing.org/reference/smooth_.html>`_

Syntax
======

.. code:: python

    smooth() -> None
    smooth(level: int) -> None

Parameters
==========

* **level**: `int` - either 2, 3, 4, or 8 depending on the renderer


Updated on November 04, 2020 20:45:44pm UTC

