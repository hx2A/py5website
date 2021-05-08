.. title: Py5Graphics.alpha()
.. slug: py5graphics_alpha
.. date: 2021-05-05 16:59:55 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.alpha() documentation
.. type: text

Extracts the alpha value from a color, scaled to match current :doc:`py5graphics_color_mode`.

Description
===========

Extracts the alpha value from a color, scaled to match current :doc:`py5graphics_color_mode`.

The ``alpha()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``alpha()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``alpha(c)`` and ``c >> 24 & 0xFF`` both extract the alpha value from a color variable ``c`` but the later is faster.

This method is the same as :doc:`alpha` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`alpha`.

Underlying Java method: PGraphics.alpha

Syntax
======

.. code:: python

    alpha(rgb: int, /) -> float

Parameters
==========

* **rgb**: `int` - any value of the color datatype


Updated on May 05, 2021 16:59:55pm UTC

