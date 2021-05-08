.. title: Py5Graphics.point_light()
.. slug: py5graphics_point_light
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.point_light() documentation
.. type: text

Adds a point light.

Description
===========

Adds a point light. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The ``x``, ``y``, and ``z`` parameters set the position of the light.

This method is the same as :doc:`point_light` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`point_light`.

Underlying Java method: PGraphics.pointLight

Syntax
======

.. code:: python

    point_light(v1: float, v2: float, v3: float, x: float, y: float, z: float, /) -> None

Parameters
==========

* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)
* **x**: `float` - x-coordinate of the light
* **y**: `float` - y-coordinate of the light
* **z**: `float` - z-coordinate of the light


Updated on May 06, 2021 16:39:27pm UTC

