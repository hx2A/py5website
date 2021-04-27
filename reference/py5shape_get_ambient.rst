.. title: get_ambient()
.. slug: py5shape_get_ambient
.. date: 2021-04-27 15:50:18 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_ambient() documentation
.. type: text

Get the ambient reflectance setting for one of a ``Py5Shape`` object's vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_ambient_0.png
    :alt: example picture for get_ambient()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.directional_light(153, 153, 153, .5, 0, -1)
        py5.ambient(255, 255, 0)
        py5.ambient_light(50, 50, 50)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 30)

        py5.shape(s, 50, 50)
        ambient = s.get_ambient(0)
        print(py5.red(ambient), py5.green(ambient), py5.blue(ambient))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the ambient reflectance setting for one of a ``Py5Shape`` object's vertices. This setting is combined with the ambient light component of the environment. Use :doc:`py5shape_set_ambient` to change the setting.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.getAmbient

Syntax
======

.. code:: python

    get_ambient(index: int, /) -> int

Parameters
==========

* **index**: `int` - vertex index


Updated on April 27, 2021 15:50:18pm UTC

