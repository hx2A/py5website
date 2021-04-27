.. title: shininess()
.. slug: shininess
.. date: 2021-04-27 15:39:47 UTC+00:00
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

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.no_stroke()
        py5.background(0)
        py5.fill(0, 51, 102)
        py5.ambient_light(102, 102, 102)
        py5.light_specular(204, 204, 204)
        py5.directional_light(102, 102, 102, 0, 0, -1)
        py5.specular(255, 255, 255)
        py5.translate(30, 50, 0)
        py5.shininess(1.0)
        py5.sphere(20)  # left sphere
        py5.translate(40, 0, 0)
        py5.shininess(5.0)
        py5.sphere(20)  # right sphere

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the amount of gloss in the surface of shapes. Use in combination with :doc:`ambient`, :doc:`specular`, and :doc:`emissive` to set the material properties of shapes.

Underlying Java method: `shininess <https://processing.org/reference/shininess_.html>`_

Syntax
======

.. code:: python

    shininess(shine: float, /) -> None

Parameters
==========

* **shine**: `float` - degree of shininess


Updated on April 27, 2021 15:39:47pm UTC

