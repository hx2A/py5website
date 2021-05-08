.. title: Py5Graphics.box()
.. slug: py5graphics_box
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.box() documentation
.. type: text

A box is an extruded rectangle.

Description
===========

A box is an extruded rectangle. A box with equal dimensions on all sides is a cube.

This method is the same as :doc:`box` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`box`.

Underlying Java method: PGraphics.box

Syntax
======

.. code:: python

    box(size: float, /) -> None
    box(w: float, h: float, d: float, /) -> None

Parameters
==========

* **d**: `float` - dimension of the box in the z-dimension
* **h**: `float` - dimension of the box in the y-dimension
* **size**: `float` - dimension of the box in all dimensions (creates a cube)
* **w**: `float` - dimension of the box in the x-dimension


Updated on May 04, 2021 20:06:05pm UTC

