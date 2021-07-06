.. title: specular()
.. slug: specular
.. date: 2021-06-28 15:16:14 UTC+00:00
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

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.no_stroke()
        py5.background(0)
        py5.fill(0, 51, 102)
        py5.light_specular(255, 255, 255)
        py5.directional_light(204, 204, 204, 0, 0, -1)
        py5.translate(20, 50, 0)
        py5.specular(255, 255, 255)
        py5.sphere(30)
        py5.translate(60, 0, 0)
        py5.specular(204, 102, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light). Use in combination with :doc:`emissive`, :doc:`ambient`, and :doc:`shininess` to set the material properties of shapes.

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


Updated on June 28, 2021 15:16:14pm UTC

