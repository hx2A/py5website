.. title: Py5Shape.get_shininess()
.. slug: py5shape_get_shininess
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_shininess() documentation
.. type: text

Get the shininess setting for one of a ``Py5Shape`` object's vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_shininess_0.png
    :alt: example picture for get_shininess()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.ambient_light(102, 102, 102)
        py5.light_specular(204, 204, 204)
        py5.directional_light(150, 150, 150, .5, 0, -1)
        py5.shininess(5)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 30)

        py5.shape(s, 50, 50)
        py5.println(s.get_shininess(0))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the shininess setting for one of a ``Py5Shape`` object's vertices. Use :doc:`py5shape_set_shininess` to change the setting.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getShininess

Syntax
======

.. code:: python

    get_shininess(index: int, /) -> float

Parameters
==========

* **index**: `int` - vertex index


Updated on July 06, 2021 22:46:12pm UTC

