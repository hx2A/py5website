.. title: circle()
.. slug: circle
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 circle() documentation
.. type: text

Draws a circle to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_circle_0.png
    :alt: example picture for circle()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    circle(56, 46, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the ``ellipse_mode()`` function.

Underlying Java method: `circle <https://processing.org/reference/circle_.html>`_

Syntax
======

.. code:: python

    circle(x: float, y: float, extent: float, /) -> None

Parameters
==========

* **extent**: `float` - width and height of the ellipse by default
* **x**: `float` - x-coordinate of the ellipse
* **y**: `float` - y-coordinate of the ellipse


Updated on November 24, 2020 21:22:32pm UTC
