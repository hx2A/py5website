.. title: Py5Graphics.no_lights()
.. slug: py5graphics_no_lights
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.no_lights() documentation
.. type: text

Disable all lighting.

Description
===========

Disable all lighting. Lighting is turned off by default and enabled with the :doc:`py5graphics_lights` function. This function can be used to disable lighting so that 2D geometry (which does not require lighting) can be drawn after a set of lighted 3D geometry.

This method is the same as :doc:`no_lights` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`no_lights`.

Underlying Java method: PGraphics.noLights

Syntax
======

.. code:: python

    no_lights() -> None

Updated on May 04, 2021 20:06:05pm UTC

