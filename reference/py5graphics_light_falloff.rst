.. title: Py5Graphics.light_falloff()
.. slug: py5graphics_light_falloff
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.light_falloff() documentation
.. type: text

Sets the falloff rates for point lights, spot lights, and ambient lights.

Description
===========

Sets the falloff rates for point lights, spot lights, and ambient lights. Like :doc:`py5graphics_fill`, it affects only the elements which are created after it in the code. The default value is ``light_falloff(1.0, 0.0, 0.0)``, and the parameters are used to calculate the falloff with the equation ``falloff = 1 / (CONSTANT + d * ``LINEAR`` + (d*d) * QUADRATIC)``, where ``d`` is the distance from light position to vertex position.

Thinking about an ambient light with a falloff can be tricky. If you want a region of your scene to be lit ambiently with one color and another region to be lit ambiently with another color, you could use an ambient light with location and falloff. You can think of it as a point light that doesn't care which direction a surface is facing.

This method is the same as :doc:`light_falloff` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`light_falloff`.

Underlying Java method: PGraphics.lightFalloff

Syntax
======

.. code:: python

    light_falloff(constant: float, linear: float, quadratic: float, /) -> None

Parameters
==========

* **constant**: `float` - constant value or determining falloff
* **linear**: `float` - linear value for determining falloff
* **quadratic**: `float` - quadratic value for determining falloff


Updated on May 04, 2021 20:06:05pm UTC

