.. title: Py5Shape.set_ambient()
.. slug: py5shape_set_ambient
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.set_ambient() documentation
.. type: text

Sets a ``Py5Shape`` object's ambient reflectance.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_ambient_0.png
    :alt: example picture for set_ambient()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.directional_light(153, 153, 153, .5, 0, -1)
        py5.ambient_light(50, 50, 50)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 20)

        s.set_ambient(py5.color(255, 0, 0))
        py5.shape(s, 50, 25)
        s.set_ambient(py5.color(255, 255, 0))
        py5.shape(s, 50, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a ``Py5Shape`` object's ambient reflectance. This is combined with the ambient light component of the environment. The color components set through the parameters define the reflectance. For example in the default color mode, calling ``set_ambient(255, 127, 0)``, would cause all the red light to reflect and half of the green light to reflect. Use in combination with :doc:`py5shape_set_emissive`, :doc:`py5shape_set_specular`, and :doc:`py5shape_set_shininess` to set the material properties of a ``Py5Shape`` object.

The ``ambient`` parameter can be applied to the entire ``Py5Shape`` object or to a single vertex.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Java method: PShape.setAmbient

Syntax
======

.. code:: python

    set_ambient(ambient: int, /) -> None
    set_ambient(index: int, ambient: int, /) -> None

Parameters
==========

* **ambient**: `int` - any color value
* **index**: `int` - vertex index


Updated on May 01, 2021 20:51:42pm UTC

