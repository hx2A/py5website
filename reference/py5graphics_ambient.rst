.. title: Py5Graphics.ambient()
.. slug: py5graphics_ambient
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.ambient() documentation
.. type: text

Sets the ambient reflectance for shapes drawn to the screen.

Description
===========

Sets the ambient reflectance for shapes drawn to the screen. This is combined with the ambient light component of the environment. The color components set through the parameters define the reflectance. For example in the default color mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect and half of the green light to reflect. Use in combination with :doc:`py5graphics_emissive`, :doc:`py5graphics_specular`, and :doc:`py5graphics_shininess` to set the material properties of shapes.

This method is the same as :doc:`ambient` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`ambient`.

Underlying Java method: PGraphics.ambient

Syntax
======

.. code:: python

    ambient(gray: float, /) -> None
    ambient(rgb: int, /) -> None
    ambient(v1: float, v2: float, v3: float, /) -> None

Parameters
==========

* **gray**: `float` - number specifying value between white and black
* **rgb**: `int` - any value of the color datatype
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on May 04, 2021 20:06:05pm UTC

