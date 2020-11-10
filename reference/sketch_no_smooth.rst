.. title: no_smooth()
.. slug: no_smooth
.. date: 2020-11-10 15:41:45 UTC+00:00
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

    size(100, 100)
    no_smooth()
    no_stroke()
    background(0)
    ellipse(30, 48, 36, 36)
    ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(100, 100, P2D)
        no_smooth()
        no_stroke()


    def draw():
        background(0)
        ellipse(30, 48, 36, 36)
        ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.  Note that ``smooth()`` is active by default, so it is necessary to call ``no_smooth()`` to disable smoothing of geometry, fonts, and images. Since the release of Processing 3.0, the ``no_smooth()`` function can only be run once for each sketch, either at the top of a sketch without a ``setup()``, or after the ``size()`` function when used in a sketch with ``setup()``. See the examples above for both scenarios.

Underlying Java method: `noSmooth <https://processing.org/reference/noSmooth_.html>`_

Syntax
======

.. code:: python

    no_smooth() -> None

Updated on November 10, 2020 15:41:45pm UTC

