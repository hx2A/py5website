.. title: Py5Graphics.lights()
.. slug: py5graphics_lights
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.lights() documentation
.. type: text

Sets the default ambient light, directional light, falloff, and specular values.

Description
===========

Sets the default ambient light, directional light, falloff, and specular values. The defaults are ``ambientLight(128, 128, 128)`` and ``directionalLight(128, 128, 128, 0, 0, -1)``, ``lightFalloff(1, 0, 0)``, and ``lightSpecular(0, 0, 0)``.

This method is the same as :doc:`lights` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`lights`.

Underlying Java method: PGraphics.lights

Syntax
======

.. code:: python

    lights() -> None

Updated on May 06, 2021 16:39:27pm UTC

