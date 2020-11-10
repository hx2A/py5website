.. title: light_specular()
.. slug: light_specular
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 light_specular() documentation
.. type: text

Sets the specular color for lights.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_light_specular_0.png
    :alt: example picture for light_specular()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    directional_light(102, 102, 102, 0, 0, -1)
    light_specular(204, 204, 204)
    directional_light(102, 102, 102, 0, 1, -1)
    light_specular(102, 102, 102)
    translate(20, 50, 0)
    specular(51, 51, 51)
    sphere(30)
    translate(60, 0, 0)
    specular(102, 102, 102)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the specular color for lights. Like ``fill()``, it affects only the elements which are created after it in the code. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light) and is used for creating highlights. The specular quality of a light interacts with the specular material qualities set through the ``specular()`` and ``shininess()`` functions.

Underlying Java method: `lightSpecular <https://processing.org/reference/lightSpecular_.html>`_

Syntax
======

.. code:: python

    light_specular(v1: float, v2: float, v3: float) -> None

Parameters
==========

* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on January 01, 1970 00:00:00am UTC

