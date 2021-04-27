.. title: set_shininess()
.. slug: py5shape_set_shininess
.. date: 2021-04-27 15:50:18 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_shininess() documentation
.. type: text

Sets the amount of gloss a ``Py5Shape`` object's surface has.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_shininess_0.png
    :alt: example picture for set_shininess()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.ambient_light(102, 102, 102)
        py5.light_specular(204, 204, 204)
        py5.directional_light(150, 150, 150, .5, 0, -1)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 20)

        s.set_shininess(0.2)
        py5.shape(s, 50, 25)
        s.set_shininess(5)
        py5.shape(s, 50, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the amount of gloss a ``Py5Shape`` object's surface has. This is part of the material properties of a ``Py5Shape`` object.

The ``shine`` parameter can be applied to the entire ``Py5Shape`` object or to a single vertex.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.setShininess

Syntax
======

.. code:: python

    set_shininess(index: int, shine: float, /) -> None
    set_shininess(shine: float, /) -> None

Parameters
==========

* **index**: `int` - vertex index
* **shine**: `float` - degree of shininess


Updated on April 27, 2021 15:50:18pm UTC

