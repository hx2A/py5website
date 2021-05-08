.. title: Py5Graphics.stroke_join()
.. slug: py5graphics_stroke_join
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.stroke_join() documentation
.. type: text

Sets the style of the joints which connect line segments.

Description
===========

Sets the style of the joints which connect line segments. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters ``MITER``, ``BEVEL``, and ``ROUND``. The default joint is ``MITER``.

This method is the same as :doc:`stroke_join` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`stroke_join`.

Underlying Java method: PGraphics.strokeJoin

Syntax
======

.. code:: python

    stroke_join(join: int, /) -> None

Parameters
==========

* **join**: `int` - either MITER, BEVEL, ROUND


Updated on May 04, 2021 20:06:05pm UTC

