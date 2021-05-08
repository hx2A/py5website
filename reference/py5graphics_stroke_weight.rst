.. title: Py5Graphics.stroke_weight()
.. slug: py5graphics_stroke_weight
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.stroke_weight() documentation
.. type: text

Sets the width of the stroke used for lines, points, and the border around shapes.

Description
===========

Sets the width of the stroke used for lines, points, and the border around shapes. All widths are set in units of pixels.

Using :doc:`py5graphics_point` with ``strokeWeight(1)`` or smaller may draw nothing to the Py5Graphics drawing surface, depending on the graphics settings of the computer. Workarounds include setting the pixel using the :doc:`py5graphics_pixels` or :doc:`py5graphics_np_pixels` arrays or drawing the point using either :doc:`py5graphics_circle` or :doc:`py5graphics_square`.

This method is the same as :doc:`stroke_weight` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`stroke_weight`.

Underlying Java method: PGraphics.strokeWeight

Syntax
======

.. code:: python

    stroke_weight(weight: float, /) -> None

Parameters
==========

* **weight**: `float` - the weight (in pixels) of the stroke


Updated on May 07, 2021 21:23:50pm UTC

