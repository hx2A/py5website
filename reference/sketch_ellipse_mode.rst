.. title: ellipse_mode()
.. slug: ellipse_mode
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 ellipse_mode() documentation
.. type: text

Modifies the location from which ellipses are drawn by changing the way in which parameters given to ``ellipse()`` are intepreted.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ellipse_mode_0.png
    :alt: example picture for ellipse_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    ellipse_mode(RADIUS)  # set ellipse_mode to RADIUS
    fill(255)  # set fill to white
    ellipse(50, 50, 30, 30)  # draw white ellipse using RADIUS mode

    ellipse_mode(CENTER)  # set ellipse_mode to CENTER
    fill(100)  # set fill to gray
    ellipse(50, 50, 30, 30)  # draw gray ellipse using CENTER mode

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ellipse_mode_1.png
    :alt: example picture for ellipse_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    ellipse_mode(CORNER)  # set ellipse_mode is CORNER
    fill(255)  # set fill to white
    ellipse(25, 25, 50, 50)  # draw white ellipse using CORNER mode

    ellipse_mode(CORNERS)  # set ellipse_mode to CORNERS
    fill(100)  # set fill to gray
    ellipse(25, 25, 50, 50)  # draw gray ellipse using CORNERS mode

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Modifies the location from which ellipses are drawn by changing the way in which parameters given to ``ellipse()`` are intepreted.

The default mode is ``ellipse_mode(CENTER)``, which interprets the first two parameters of ``ellipse()`` as the shape's center point, while the third and fourth parameters are its width and height.

``ellipse_mode(RADIUS)`` also uses the first two parameters of ``ellipse()`` as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

``ellipse_mode(CORNER)`` interprets the first two parameters of ``ellipse()`` as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

``ellipse_mode(CORNERS)`` interprets the first two parameters of ``ellipse()`` as the location of one corner of the ellipse's bounding box, and the third and fourth parameters as the location of the opposite corner.

The parameter must be written in ALL CAPS because Processing is a case-sensitive language.

Underlying Java method: `ellipseMode <https://processing.org/reference/ellipseMode_.html>`_

Syntax
======

.. code:: python

    ellipse_mode(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - either CENTER, RADIUS, CORNER, or CORNERS


Updated on November 24, 2020 21:22:32pm UTC

