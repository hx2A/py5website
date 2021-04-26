.. title: emissive()
.. slug: py5shape_emissive
.. date: 2021-04-26 16:21:41 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 emissive() documentation
.. type: text

Sets the emissive color of a ``Py5Shape`` object's material.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_emissive_0.png
    :alt: example picture for emissive()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def create_strip(use_emissive):
        s = py5.create_shape()
        s.begin_shape(py5.TRIANGLE_STRIP)
        if use_emissive:
            s.emissive(0, 50, 100)
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
        py5.directional_light(200, 200, 200, .5, 0, -1)
        py5.shape(create_strip(False), 0, 5)
        py5.shape(create_strip(True), 0, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the emissive color of a ``Py5Shape`` object's material. Used in combination with :doc:`py5shape_ambient`, :doc:`py5shape_specular`, and :doc:`py5shape_shininess` in setting the material properties of a ``Py5Shape`` object.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair. The emissive color setting will be applied to vertices added after the call to this method.

Underlying Java method: PShape.emissive

Syntax
======

.. code:: python

    emissive(gray: float, /) -> None
    emissive(rgb: int, /) -> None
    emissive(x: float, y: float, z: float, /) -> None

Parameters
==========

* **gray**: `float` - value between black and white, by default 0 to 255
* **rgb**: `int` - color to set
* **x**: `float` - red or hue value (depending on current color mode)
* **y**: `float` - green or saturation value (depending on current color mode)
* **z**: `float` - blue or brightness value (depending on current color mode)


Updated on April 26, 2021 16:21:41pm UTC

