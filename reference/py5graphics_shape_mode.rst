.. title: Py5Graphics.shape_mode()
.. slug: py5graphics_shape_mode
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.shape_mode() documentation
.. type: text

Modifies the location from which shapes draw.

Description
===========

Modifies the location from which shapes draw. The default mode is ``shape_mode(CORNER)``, which specifies the location to be the upper left corner of the shape and uses the third and fourth parameters of :doc:`py5graphics_shape` to specify the width and height. The syntax ``shape_mode(CORNERS)`` uses the first and second parameters of :doc:`py5graphics_shape` to set the location of one corner and uses the third and fourth parameters to set the opposite corner. The syntax ``shape_mode(CENTER)`` draws the shape from its center point and uses the third and forth parameters of :doc:`py5graphics_shape` to specify the width and height. The parameter must be written in ALL CAPS because Python is a case sensitive language.

This method is the same as :doc:`shape_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`shape_mode`.

Underlying Java method: PGraphics.shapeMode

Syntax
======

.. code:: python

    shape_mode(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - either CORNER, CORNERS, CENTER


Updated on May 04, 2021 20:06:05pm UTC

