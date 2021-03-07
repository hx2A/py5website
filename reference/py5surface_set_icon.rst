.. title: set_icon()
.. slug: py5surface_set_icon
.. date: 2021-03-07 16:29:38 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_icon() documentation
.. type: text

Set the Sketch window icon.

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
        surface.set_title("py5 window")
        surface.set_always_on_top(True)
        surface.set_icon(py5.load_image("logo-64x64.png"))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(200, 200, py5.P2D)


    def setup():
        surface = py5.get_surface()
        surface.set_title("py5 window")
        surface.set_always_on_top(True)


    # run this before calling run_sketch()
    PJOGL = py5.JClass("processing.opengl.PJOGL")
    PJOGL.setIcon("data/logo-64x64.png")

    py5.run_sketch(block=False)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set the Sketch window icon. This will typically appear in the window's title bar. The default window icon is the same as Processing's.

This method will not work for the ``P2D`` or ``P3D`` renderers. Setting the icon for those renderers is a bit tricky; see the second example to learn how to do that.

Underlying Java method: PSurface.setIcon

Syntax
======

.. code:: python

    set_icon(icon: Py5Image, /) -> None

Parameters
==========

* **icon**: `Py5Image` - image to use as the window icon


Updated on March 07, 2021 16:29:38pm UTC

