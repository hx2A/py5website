.. title: Py5Graphics.emissive()
.. slug: py5graphics_emissive
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.emissive() documentation
.. type: text

Sets the emissive color of the material used for drawing shapes drawn to the screen.

Description
===========

Sets the emissive color of the material used for drawing shapes drawn to the screen. Use in combination with :doc:`py5graphics_ambient`, :doc:`py5graphics_specular`, and :doc:`py5graphics_shininess` to set the material properties of shapes.

This method is the same as :doc:`emissive` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`emissive`.

Underlying Java method: PGraphics.emissive

Syntax
======

.. code:: python

    emissive(gray: float, /) -> None
    emissive(rgb: int, /) -> None
    emissive(v1: float, v2: float, v3: float, /) -> None

Parameters
==========

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on May 04, 2021 20:06:05pm UTC

