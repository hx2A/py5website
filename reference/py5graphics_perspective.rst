.. title: Py5Graphics.perspective()
.. slug: py5graphics_perspective
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.perspective() documentation
.. type: text

Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones.

Description
===========

Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones. The parameters define a viewing volume with the shape of truncated pyramid. Objects near to the front of the volume appear their actual size, while farther objects appear smaller. This projection simulates the perspective of the world more accurately than orthographic projection. The version of perspective without parameters sets the default perspective and the version with four parameters allows the programmer to set the area precisely. The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0, cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.

This method is the same as :doc:`perspective` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`perspective`.

Underlying Java method: PGraphics.perspective

Syntax
======

.. code:: python

    perspective() -> None
    perspective(fovy: float, aspect: float, z_near: float, z_far: float, /) -> None

Parameters
==========

* **aspect**: `float` - ratio of width to height
* **fovy**: `float` - field-of-view angle (in radians) for vertical direction
* **z_far**: `float` - z-position of farthest clipping plane
* **z_near**: `float` - z-position of nearest clipping plane


Updated on May 04, 2021 20:06:05pm UTC

