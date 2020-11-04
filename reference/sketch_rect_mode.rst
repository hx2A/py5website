.. title: rect_mode()
.. slug: sketch_rect_mode
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 rect_mode() documentation
.. type: text

Modifies the location from which rectangles are drawn by changing the way in which parameters given to ``rect()`` are intepreted.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_mode_0.png
    :alt: example picture for rect_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    rect_mode(CORNER)  # default rect_mode is CORNER
    fill(255)  # set fill to white
    rect(25, 25, 50, 50)  # draw white rect using CORNER mode

    rect_mode(CORNERS)  # set rect_mode to CORNERS
    fill(100)  # set fill to gray
    rect(25, 25, 50, 50)  # draw gray rect using CORNERS mode

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rect_mode_1.png
    :alt: example picture for rect_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    rect_mode(RADIUS)  # set rect_mode to RADIUS
    fill(255)  # set fill to white
    rect(50, 50, 30, 30)  # draw white rect using RADIUS mode

    rect_mode(CENTER)  # set rect_mode to CENTER
    fill(100)  # set fill to gray
    rect(50, 50, 30, 30)  # draw gray rect using CENTER mode

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Modifies the location from which rectangles are drawn by changing the way in which parameters given to ``rect()`` are intepreted.

The default mode is ``rect_mode(CORNER)``, which interprets the first two parameters of ``rect()`` as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

``rect_mode(CORNERS)`` interprets the first two parameters of ``rect()`` as the location of one corner, and the third and fourth parameters as the location of the opposite corner.

``rect_mode(CENTER)`` interprets the first two parameters of ``rect()`` as the shape's center point, while the third and fourth parameters are its width and height.

``rect_mode(RADIUS)`` also uses the first two parameters of ``rect()`` as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

The parameter must be written in ALL CAPS because Processing is a case-sensitive language.

Underlying Java method: `rectMode <https://processing.org/reference/rectMode_.html>`_

Syntax
======

.. code:: python

    rect_mode(mode: int) -> None

Parameters
==========

* **mode**: `int` - either CORNER, CORNERS, CENTER, or RADIUS


Updated on November 04, 2020 20:45:44pm UTC

