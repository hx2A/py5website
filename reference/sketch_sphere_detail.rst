.. title: sphere_detail()
.. slug: sphere_detail
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 sphere_detail() documentation
.. type: text

Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(100, 100, P3D)


    def draw():
        background(200)
        stroke(255, 50)
        translate(50, 50, 0)
        rotate_x(mouse_y * 0.05)
        rotate_y(mouse_x * 0.05)
        fill(mouse_x * 2, 0, 160)
        sphere_detail(mouse_x / 4)
        sphere(40)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh. The default resolution is 30, which creates a fairly detailed sphere definition with vertices every 360/30 = 12 degrees. If you're going to render a great number of spheres per frame, it is advised to reduce the level of detail using this function. The setting stays active until ``sphere_detail()`` is called again with a new parameter and so should *not* be called prior to every ``sphere()`` statement, unless you wish to render spheres with different settings, e.g. using less detail for smaller spheres or ones further away from the camera. To control the detail of the horizontal and vertical resolution independently, use the version of the functions with two parameters.

Underlying Java method: `sphereDetail <https://processing.org/reference/sphereDetail_.html>`_

Syntax
======

.. code:: python

    sphere_detail(res: int) -> None
    sphere_detail(ures: int, vres: int) -> None

Parameters
==========

* **res**: `int` - number of segments (minimum 3) used per full circle revolution
* **ures**: `int` - number of segments used longitudinally per full circle revolutoin
* **vres**: `int` - number of segments used latitudinally from top to bottom


Updated on January 01, 1970 00:00:00am UTC

