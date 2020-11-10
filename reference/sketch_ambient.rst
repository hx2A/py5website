.. title: ambient()
.. slug: ambient
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 ambient() documentation
.. type: text

Sets the ambient reflectance for shapes drawn to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ambient_0.png
    :alt: example picture for ambient()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    directional_light(153, 153, 153, .5, 0, -1)
    ambient_light(153, 102, 0)
    ambient(51, 26, 0)
    translate(70, 50, 0)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the ambient reflectance for shapes drawn to the screen. This is combined with the ambient light component of environment. The color components set through the parameters define the reflectance. For example in the default color mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and half of the green light to reflect. Used in combination with ``emissive()``, ``specular()``, and ``shininess()`` in setting the material properties of shapes.

Underlying Java method: `ambient <https://processing.org/reference/ambient_.html>`_

Syntax
======

.. code:: python

    ambient(gray: float) -> None
    ambient(rgb: int) -> None
    ambient(v1: float, v2: float, v3: float) -> None

Parameters
==========

* **gray**: `float` - number specifying value between white and black
* **rgb**: `int` - any value of the color datatype
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 10, 2020 15:41:45pm UTC

