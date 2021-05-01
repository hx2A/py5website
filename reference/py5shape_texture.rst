.. title: Py5Shape.texture()
.. slug: py5shape_texture
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.texture() documentation
.. type: text

Sets a texture to be applied to a ``Py5Shape`` object's vertex points.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_texture_0.png
    :alt: example picture for texture()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P2D)


    def setup():
        img = py5.load_image("tower.jpg")
        s = py5.create_shape()
        s.begin_shape()
        s.texture(img)
        s.vertex(20, 20, 0, 0)
        s.vertex(20, 80, 0, 100)
        s.vertex(80, 80, 100, 100)
        s.vertex(80, 20, 100, 0)
        s.end_shape(py5.CLOSE)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a texture to be applied to a ``Py5Shape`` object's vertex points. The ``texture()`` function must be called between :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` and before any calls to :doc:`py5shape_vertex`. This method only works with the ``P2D`` and ``P3D`` renderers.

When textures are in use, the fill color is ignored. Instead, use :doc:`py5shape_tint` to specify the color of the texture as it is applied to the shape.

Underlying Java method: PShape.texture

Syntax
======

.. code:: python

    texture(tex: Py5Image, /) -> None

Parameters
==========

* **tex**: `Py5Image` - reference to a Py5Image object


Updated on May 01, 2021 20:51:42pm UTC

