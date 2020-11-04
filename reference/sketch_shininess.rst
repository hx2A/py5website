.. title: shininess()
.. slug: sketch_shininess
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 shininess() documentation
.. type: text

Sets the amount of gloss in the surface of shapes.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_shininess_0.png
    :alt: example picture for shininess()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    background(0)
    fill(0, 51, 102)
    ambient_light(102, 102, 102)
    light_specular(204, 204, 204)
    directional_light(102, 102, 102, 0, 0, -1)
    specular(255, 255, 255)
    translate(30, 50, 0)
    shininess(1.0)
    sphere(20)  # left sphere
    translate(40, 0, 0)
    shininess(5.0)
    sphere(20)  # right sphere

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the amount of gloss in the surface of shapes. Used in combination with ``ambient()``, ``specular()``, and ``emissive()`` in setting the material properties of shapes.

Underlying Java method: `shininess <https://processing.org/reference/shininess_.html>`_

Syntax
======

.. code:: python

    shininess(shine: float) -> None

Parameters
==========

* **shine**: `float` - degree of shininess


Updated on November 04, 2020 20:45:44pm UTC

