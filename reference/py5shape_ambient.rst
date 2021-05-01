.. title: Py5Shape.ambient()
.. slug: py5shape_ambient
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.ambient() documentation
.. type: text

Sets a ``Py5Shape`` object's ambient reflectance.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_ambient_0.png
    :alt: example picture for ambient()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def create_strip(use_ambient):
        s = py5.create_shape()
        s.begin_shape(py5.TRIANGLE_STRIP)
        if use_ambient:
            s.ambient(255, 0, 0)
        s.vertex(10, 40, -25)
        s.vertex(20, 0, -10)
        s.vertex(30, 40, 0)
        s.vertex(40, 0, 5)
        s.vertex(50, 40, 0)
        s.vertex(60, 0, -10)
        s.vertex(70, 40, -25)
        s.end_shape()
        return s


    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.directional_light(153, 153, 153, .5, 0, -1)
        py5.ambient_light(50, 50, 50)
        py5.shape(create_strip(False), 0, 5)
        py5.shape(create_strip(True), 0, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a ``Py5Shape`` object's ambient reflectance. This is combined with the ambient light component of the environment. The color components set through the parameters define the reflectance. For example in the default color mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect and half of the green light to reflect. Use in combination with :doc:`py5shape_emissive`, :doc:`py5shape_specular`, and :doc:`py5shape_shininess` to set the material properties of a ``Py5Shape`` object.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair. The ambient color setting will be applied to vertices added after the call to this method.

Underlying Java method: PShape.ambient

Syntax
======

.. code:: python

    ambient(gray: float, /) -> None
    ambient(rgb: int, /) -> None
    ambient(x: float, y: float, z: float, /) -> None

Parameters
==========

* **gray**: `float` - number specifying value between white and black
* **rgb**: `int` - any value of the color datatype
* **x**: `float` - red or hue value (depending on current color mode)
* **y**: `float` - green or saturation value (depending on current color mode)
* **z**: `float` - blue or brightness value (depending on current color mode)


Updated on May 01, 2021 20:51:42pm UTC

