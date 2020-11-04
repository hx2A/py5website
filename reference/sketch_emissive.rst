.. title: emissive()
.. slug: sketch_emissive
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 emissive() documentation
.. type: text

Sets the emissive color of the material used for drawing shapes drawn to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_emissive_0.png
    :alt: example picture for emissive()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    background(0)
    directional_light(204, 204, 204, .5, 0, -1)
    emissive(0, 26, 51)
    translate(70, 50, 0)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the emissive color of the material used for drawing shapes drawn to the screen. Used in combination with ``ambient()``, ``specular()``, and ``shininess()`` in setting the material properties of shapes.

Underlying Java method: `emissive <https://processing.org/reference/emissive_.html>`_

Syntax
======

.. code:: python

    emissive(gray: float) -> None
    emissive(rgb: int) -> None
    emissive(v1: float, v2: float, v3: float) -> None

Parameters
==========

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 04, 2020 20:45:44pm UTC

