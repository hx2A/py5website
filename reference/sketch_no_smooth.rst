.. title: no_smooth()
.. slug: no_smooth
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_smooth() documentation
.. type: text

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.

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
        py5.size(100, 100, py5.P2D)
        py5.no_smooth()
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

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.  Note that :doc:`smooth` is active by default, so it is necessary to call ``no_smooth()`` to disable smoothing of geometry, fonts, and images.

The ``no_smooth()`` function can only be called once within a Sketch. It is intended to be called from the ``settings()`` function. The :doc:`smooth` function follows the same rules.

When programming in module mode and imported mode, py5 will allow calls to ``no_smooth()`` from the ``setup()`` function if it is called at the beginning of ``setup()``. This allows the user to omit the ``settings()`` function, much like what can be done while programming in the Processing IDE. Py5 does this by inspecting the ``setup()`` function and attempting to split it into synthetic ``settings()`` and ``setup()`` functions if both were not created by the user and the real ``setup()`` function contains a call to ``no_smooth()``, or calls to :doc:`size`, :doc:`full_screen`, :doc:`smooth`, or :doc:`pixel_density`. Calls to those functions must be at the very beginning of ``setup()``, before any other Python code (but comments are ok). This feature is not available when programming in class mode.

Underlying Java method: `noSmooth <https://processing.org/reference/noSmooth_.html>`_

Syntax
======

.. code:: python

    no_smooth() -> None

Updated on June 28, 2021 15:16:14pm UTC

