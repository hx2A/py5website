.. title: Py5Graphics.specular()
.. slug: py5graphics_specular
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.specular() documentation
.. type: text

Sets the specular color of the materials used for shapes drawn to the Py5Graphics drawing surface, which sets the color of highlights.

Description
===========

Sets the specular color of the materials used for shapes drawn to the Py5Graphics drawing surface, which sets the color of highlights. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light). Use in combination with :doc:`py5graphics_emissive`, :doc:`py5graphics_ambient`, and :doc:`py5graphics_shininess` to set the material properties of shapes.

This method is the same as :doc:`specular` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`specular`.

Underlying Java method: PGraphics.specular

Syntax
======

.. code:: python

    specular(gray: float, /) -> None
    specular(rgb: int, /) -> None
    specular(v1: float, v2: float, v3: float, /) -> None

Parameters
==========

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on May 07, 2021 21:23:50pm UTC

