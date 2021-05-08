.. title: Py5Graphics.bezier_detail()
.. slug: py5graphics_bezier_detail
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.bezier_detail() documentation
.. type: text

Sets the resolution at which Beziers display.

Description
===========

Sets the resolution at which Beziers display. The default value is 20. This function is only useful when using the ``P3D`` renderer; the default ``P2D`` renderer does not use this information.

This method is the same as :doc:`bezier_detail` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`bezier_detail`.

Underlying Java method: PGraphics.bezierDetail

Syntax
======

.. code:: python

    bezier_detail(detail: int, /) -> None

Parameters
==========

* **detail**: `int` - resolution of the curves


Updated on May 04, 2021 20:06:05pm UTC

