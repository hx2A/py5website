.. title: hot_reload_draw()
.. slug: hot_reload_draw
.. date: 2021-04-12 18:46:58 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 hot_reload_draw() documentation
.. type: text

Perform a hot reload of the Sketch's draw function.

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

    import time


    def draw():
        py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)


    def draw2():
        py5.circle(py5.mouse_x, py5.mouse_y, 10)


    py5.run_sketch()

    time.sleep(10)
    py5.hot_reload_draw(draw2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Perform a hot reload of the Sketch's draw function. This method allows you to replace a running Sketch's draw function with a different one.

Syntax
======

.. code:: python

    hot_reload_draw(draw: Callable) -> None

Parameters
==========

* **draw**: `Callable` - function to replace existing draw function


Updated on April 12, 2021 18:46:58pm UTC

