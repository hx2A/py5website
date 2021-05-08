.. title: Py5Graphics.stroke_cap()
.. slug: py5graphics_stroke_cap
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.stroke_cap() documentation
.. type: text

Sets the style for rendering line endings.

Description
===========

Sets the style for rendering line endings. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: ``SQUARE``, ``PROJECT``, and ``ROUND``. The default cap is ``ROUND``.

To make :doc:`py5graphics_point` appear square, use ``stroke_cap(PROJECT)``. Using ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.

This method is the same as :doc:`stroke_cap` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`stroke_cap`.

Underlying Java method: PGraphics.strokeCap

Syntax
======

.. code:: python

    stroke_cap(cap: int, /) -> None

Parameters
==========

* **cap**: `int` - either SQUARE, PROJECT, or ROUND


Updated on May 04, 2021 20:06:05pm UTC

