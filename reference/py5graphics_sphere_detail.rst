.. title: Py5Graphics.sphere_detail()
.. slug: py5graphics_sphere_detail
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.sphere_detail() documentation
.. type: text

Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh.

Description
===========

Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh. The default resolution is 30, which creates a fairly detailed sphere definition with vertices every ``360/30 = 12`` degrees. If you're going to render a great number of spheres per frame, it is advised to reduce the level of detail using this function. The setting stays active until ``sphere_detail()`` is called again with a new parameter and so should *not* be called prior to every :doc:`py5graphics_sphere` statement, unless you wish to render spheres with different settings, e.g. using less detail for smaller spheres or ones further away from the camera. To control the detail of the horizontal and vertical resolution independently, use the version of the functions with two parameters.

This method is the same as :doc:`sphere_detail` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sphere_detail`.

Underlying Java method: PGraphics.sphereDetail

Syntax
======

.. code:: python

    sphere_detail(res: int, /) -> None
    sphere_detail(ures: int, vres: int, /) -> None

Parameters
==========

* **res**: `int` - number of segments (minimum 3) used per full circle revolution
* **ures**: `int` - number of segments used longitudinally per full circle revolutoin
* **vres**: `int` - number of segments used latitudinally from top to bottom


Updated on May 04, 2021 20:06:05pm UTC

