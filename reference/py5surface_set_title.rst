.. title: set_title()
.. slug: py5surface_set_title
.. date: 2021-03-07 16:29:38 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_title() documentation
.. type: text

Set the Sketch window's title.

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

    </div>

Description
===========

Set the Sketch window's title. This will typically appear at the window's title bar. The default window title is "Py5Applet".

Underlying Java method: PSurface.setTitle

Syntax
======

.. code:: python

    set_title(title: str, /) -> None

Parameters
==========

* **title**: `str` - new window title


Updated on March 07, 2021 16:29:38pm UTC

