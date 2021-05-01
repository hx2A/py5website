.. title: Py5Surface.set_size()
.. slug: py5surface_set_size
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Surface.set_size() documentation
.. type: text

Set a new width and height for the Sketch window.

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

    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)

    py5.run_sketch(block=False)

    # while the sketch is running, get the surface and change the size
    surface = py5.get_surface()
    surface.set_size(400, 400)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set a new width and height for the Sketch window. You do not need to call :doc:`py5surface_set_resizable` before calling this.

Changing the window size will clear the drawing canvas. If your Sketch uses this, the :doc:`width` and :doc:`height` variables will change.

Underlying Java method: PSurface.setSize

Syntax
======

.. code:: python

    set_size(width: int, height: int, /) -> None

Parameters
==========

* **height**: `int` - new window height
* **width**: `int` - new window width


Updated on May 01, 2021 20:51:42pm UTC

