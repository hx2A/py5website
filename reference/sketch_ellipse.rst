.. title: ellipse()
.. slug: sketch_ellipse
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 ellipse() documentation
.. type: text

Draws an ellipse (oval) to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ellipse_0.png
    :alt: example picture for ellipse()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    ellipse(56, 46, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle. By default, the first two parameters set the location, and the third and fourth parameters set the shape's width and height. The origin may be changed with the ``ellipse_mode()`` function.

Underlying Java method: `ellipse <https://processing.org/reference/ellipse_.html>`_

Syntax
======

.. code:: python

    ellipse(a: float, b: float, c: float, d: float) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the ellipse
* **b**: `float` - y-coordinate of the ellipse
* **c**: `float` - width of the ellipse by default
* **d**: `float` - height of the ellipse by default


Updated on November 04, 2020 20:45:44pm UTC

