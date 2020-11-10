.. title: perspective()
.. slug: perspective
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 perspective() documentation
.. type: text

Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_perspective_0.png
    :alt: example picture for perspective()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # re-creates the default perspective
    size(100, 100, P3D)
    no_fill()
    fov = PI/3.0
    camera_z = (height//2.0) / tan(fov/2.0)
    perspective(fov, float(width)/float(height),
                camera_z/10.0, camera_z*10.0)
    translate(50, 50, 0)
    rotate_x(-PI/6)
    rotate_y(PI/3)
    box(45)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones. The parameters define a viewing volume with the shape of truncated pyramid. Objects near to the front of the volume appear their actual size, while farther objects appear smaller. This projection simulates the perspective of the world more accurately than orthographic projection. The version of perspective without parameters sets the default perspective and the version with four parameters allows the programmer to set the area precisely. The default values are: perspective(PI/3.0, width/height, cameraZ/10.0, cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));

Underlying Java method: `perspective <https://processing.org/reference/perspective_.html>`_

Syntax
======

.. code:: python

    perspective() -> None
    perspective(fovy: float, aspect: float, z_near: float, z_far: float) -> None

Parameters
==========

* **aspect**: `float` - ratio of width to height
* **fovy**: `float` - field-of-view angle (in radians) for vertical direction
* **z_far**: `float` - z-position of farthest clipping plane
* **z_near**: `float` - z-position of nearest clipping plane


Updated on January 01, 1970 00:00:00am UTC

