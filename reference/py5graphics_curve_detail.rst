.. title: Py5Graphics.curve_detail()
.. slug: py5graphics_curve_detail
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.curve_detail() documentation
.. type: text

Sets the resolution at which curves display.

Description
===========

Sets the resolution at which curves display. The default value is 20. This function is only useful when using the ``P3D`` renderer as the default ``P2D`` renderer does not use this information.

This method is the same as :doc:`curve_detail` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`curve_detail`.

Underlying Java method: PGraphics.curveDetail

Syntax
======

.. code:: python

    curve_detail(detail: int, /) -> None

Parameters
==========

* **detail**: `int` - resolution of the curves


Updated on May 04, 2021 20:06:05pm UTC

