.. title: no_smooth()
.. slug: no_smooth
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def settings():
        py5.size(100, 100, py5.P2D)
        py5.no_smooth()


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

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.  Note that ``smooth()`` is active by default, so it is necessary to call ``no_smooth()`` to disable smoothing of geometry, fonts, and images. Since the release of Processing 3.0, the ``no_smooth()`` function can only be run once for each sketch and must be called in ``settings()``.

Underlying Java method: `noSmooth <https://processing.org/reference/noSmooth_.html>`_

Syntax
======

.. code:: python

    no_smooth() -> None

Updated on February 13, 2021 18:02:35pm UTC

