.. title: shape_mode()
.. slug: shape_mode
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 shape_mode() documentation
.. type: text

Modifies the location from which shapes draw.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_shape_mode_0.png
    :alt: example picture for shape_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global bot
        size(100, 100)
        bot = load_shape("bot.svg")


    def draw():
        shape_mode(CENTER)
        shape(bot, 35, 35, 50, 50)
        shape_mode(CORNER)
        shape(bot, 35, 35, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Modifies the location from which shapes draw. The default mode is ``shape_mode(CORNER)``, which specifies the location to be the upper left corner of the shape and uses the third and fourth parameters of ``shape()`` to specify the width and height. The syntax ``shape_mode(CORNERS)`` uses the first and second parameters of ``shape()`` to set the location of one corner and uses the third and fourth parameters to set the opposite corner. The syntax ``shape_mode(CENTER)`` draws the shape from its center point and uses the third and forth parameters of ``shape()`` to specify the width and height. The parameter must be written in "ALL CAPS" because Processing is a case sensitive language.

Underlying Java method: `shapeMode <https://processing.org/reference/shapeMode_.html>`_

Syntax
======

.. code:: python

    shape_mode(mode: int) -> None

Parameters
==========

* **mode**: `int` - either CORNER, CORNERS, CENTER


Updated on January 01, 1970 00:00:00am UTC

