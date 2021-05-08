.. title: Py5Graphics.text_width()
.. slug: py5graphics_text_width
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.text_width() documentation
.. type: text

Calculates and returns the width of any character or text string.

Description
===========

Calculates and returns the width of any character or text string.

This method is the same as :doc:`text_width` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`text_width`.

Underlying Java method: PGraphics.textWidth

Syntax
======

.. code:: python

    text_width(c: chr, /) -> float
    text_width(chars: List[chr], start: int, length: int, /) -> float
    text_width(str: str, /) -> float

Parameters
==========

* **c**: `chr` - the character to measure
* **chars**: `List[chr]` - the character to measure
* **length**: `int` - number of characters to measure
* **start**: `int` - first character to measure
* **str**: `str` - the String of characters to measure


Updated on May 04, 2021 20:06:05pm UTC

