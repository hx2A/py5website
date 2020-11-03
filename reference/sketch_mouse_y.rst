.. title: mouse_y
.. slug: sketch_mouse_y
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 mouse_y documentation
.. type: text

The system variable ``mouse_y`` always contains the current vertical coordinate of the mouse.

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
        background(204)
        line(20, mouse_y, 80, mouse_y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The system variable ``mouse_y`` always contains the current vertical coordinate of the mouse.

Note that Processing can only track the mouse position when the pointer is over the current window. The default value of ``mouse_y`` is ``0``, so ``0`` will be returned until the mouse moves in front of the sketch window. (This typically happens when a sketch is first run.)  Once the mouse moves away from the window, ``mouse_y`` will continue to report its most recent position.


Updated on November 03, 2020 22:19:57pm UTC

