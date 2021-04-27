.. title: set_emissive()
.. slug: py5shape_set_emissive
.. date: 2021-04-27 15:39:47 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_emissive() documentation
.. type: text

Sets a ``Py5Shape`` object's emissive color.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_emissive_0.png
    :alt: example picture for set_emissive()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.directional_light(200, 200, 200, .5, 0, -1)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 20)

        s.set_emissive(py5.color(0, 50, 100))
        py5.shape(s, 50, 25)
        s.set_emissive(py5.color(100, 50, 0))
        py5.shape(s, 50, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a ``Py5Shape`` object's emissive color. This is part of the material properties of a ``Py5Shape`` object.

The ``emissive`` parameter can be applied to the entire ``Py5Shape`` object or to a single vertex.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.setEmissive

Syntax
======

.. code:: python

    set_emissive(emissive: int, /) -> None
    set_emissive(index: int, emissive: int, /) -> None

Parameters
==========

* **emissive**: `int` - any color value
* **index**: `int` - vertex index


Updated on April 27, 2021 15:39:47pm UTC

