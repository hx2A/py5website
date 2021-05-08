.. title: Py5Graphics.light_specular()
.. slug: py5graphics_light_specular
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.light_specular() documentation
.. type: text

Sets the specular color for lights.

Description
===========

Sets the specular color for lights. Like :doc:`py5graphics_fill`, it affects only the elements which are created after it in the code. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light) and is used for creating highlights. The specular quality of a light interacts with the specular material qualities set through the :doc:`py5graphics_specular` and :doc:`py5graphics_shininess` functions.

This method is the same as :doc:`light_specular` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`light_specular`.

Underlying Java method: PGraphics.lightSpecular

Syntax
======

.. code:: python

    light_specular(v1: float, v2: float, v3: float, /) -> None

Parameters
==========

* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on May 04, 2021 20:06:05pm UTC

