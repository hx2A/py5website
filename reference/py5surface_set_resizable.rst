.. title: set_resizable()
.. slug: py5surface_set_resizable
.. date: 2021-03-07 15:23:06 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_resizable() documentation
.. type: text

Set the Sketch window as resizable by the user.

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
        surface = py5.get_surface()
        surface.set_resizable(True)


    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set the Sketch window as resizable by the user. The user will be able to resize the window in the same way as they do for many other windows on their computer. By default, the Sketch window is not resizable.

Changing the window size will clear the drawing canvas. If your Sketch uses this, the :doc:`width` and :doc:`height` variables will change.

Underlying Java method: PSurface.setResizable

Syntax
======

.. code:: python

    set_resizable(resizable: bool, /) -> None

Parameters
==========

* **resizable**: `bool` - should the Sketch window be resizable


Updated on March 07, 2021 15:23:06pm UTC

