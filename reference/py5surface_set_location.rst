.. title: set_location()
.. slug: py5surface_set_location
.. date: 2021-03-09 15:28:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_location() documentation
.. type: text

Set the Sketch's window location.

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

    py5.run_sketch(block=False)
    surface = py5.get_surface()
    # move the sketch window to the upper left corner of the display
    surface.set_location(0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # this sketch will hide itself and reappear elsewhere on your display.
    def setup():
        global surface
        global visible
        surface = py5.get_surface()
        visible = True


    def draw():
        global visible
        if py5.frame_count % 250 == 0:
            # this negates the visible variable
            visible = not visible
            if visible:
                surface.set_location(py5.random_int(py5.display_width),
                                     py5.random_int(py5.display_height))
            surface.set_visible(visible)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set the Sketch's window location. Calling this repeatedly from the ``draw()`` function may result in a sluggish Sketch. Negative or invalid coordinates are ignored. To hide a Sketch window, use :doc:`py5surface_set_visible`.

Underlying Java method: PSurface.setLocation

Syntax
======

.. code:: python

    set_location(x: int, y: int, /) -> None

Parameters
==========

* **x**: `int` - x-coordinate for window location
* **y**: `int` - y-coordinate for window location


Updated on March 09, 2021 15:28:39pm UTC

