.. title: Py5Graphics.green()
.. slug: py5graphics_green
.. date: 2021-05-05 16:59:55 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.green() documentation
.. type: text

Extracts the green value from a color, scaled to match current :doc:`py5graphics_color_mode`.

Description
===========

Extracts the green value from a color, scaled to match current :doc:`py5graphics_color_mode`.

The ``green()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``green()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``green(c)`` and ``c >> 8 & 0xFF`` both extract the green value from a color variable ``c`` but the later is faster.

This method is the same as :doc:`green` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`green`.

Underlying Java method: PGraphics.green

Syntax
======

.. code:: python

    green(rgb: int, /) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on May 05, 2021 16:59:55pm UTC

