.. title: Py5Shape.get_emissive()
.. slug: py5shape_get_emissive
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_emissive() documentation
.. type: text

Get the emissive color setting for one of a ``Py5Shape`` object's vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_emissive_0.png
    :alt: example picture for get_emissive()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.directional_light(200, 200, 200, .5, 0, -1)
        py5.emissive(0, 50, 100)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 30)

        py5.shape(s, 50, 50)
        emissive = s.get_emissive(0)
        print(py5.red(emissive), py5.green(emissive), py5.blue(emissive))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the emissive color setting for one of a ``Py5Shape`` object's vertices. Use :doc:`py5shape_set_emissive` to change the setting.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getEmissive

Syntax
======

.. code:: python

    get_emissive(index: int, /) -> int

Parameters
==========

* **index**: `int` - vertex index


Updated on May 01, 2021 20:51:42pm UTC

