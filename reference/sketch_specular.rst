.. title: specular()
.. slug: specular
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 specular() documentation
.. type: text

Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_specular_0.png
    :alt: example picture for specular()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    background(0)
    fill(0, 51, 102)
    light_specular(255, 255, 255)
    directional_light(204, 204, 204, 0, 0, -1)
    translate(20, 50, 0)
    specular(255, 255, 255)
    sphere(30)
    translate(60, 0, 0)
    specular(204, 102, 0)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light). Used in combination with ``emissive()``, ``ambient()``, and ``shininess()`` in setting the material properties of shapes.

Underlying Java method: `specular <https://processing.org/reference/specular_.html>`_

Syntax
======

.. code:: python

    specular(gray: float, /) -> None
    specular(rgb: int, /) -> None
    specular(v1: float, v2: float, v3: float, /) -> None

Parameters
==========

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 24, 2020 21:22:32pm UTC

