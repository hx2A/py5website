.. title: display_density()
.. slug: display_density
.. date: 2021-03-04 20:16:29 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 display_density() documentation
.. type: text

This function returns the number "2" if the screen is a high-density screen (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if not.

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

    def settings():
        py5.pixel_density(py5.display_density())


    def setup():
        py5.no_stroke()


    def draw():
        py5.background(0)
        py5.ellipse(30, 48, 36, 36)
        py5.ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

This function returns the number "2" if the screen is a high-density screen (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if not. This information is useful for a program to adapt to run at double the pixel density on a screen that supports it.

Underlying Java method: `displayDensity <https://processing.org/reference/displayDensity_.html>`_

Syntax
======

.. code:: python

    display_density() -> int
    display_density(display: int, /) -> int

Parameters
==========

* **display**: `int` - the display number to check (1-indexed to match the Preferences dialog box)


Updated on March 04, 2021 20:16:29pm UTC

