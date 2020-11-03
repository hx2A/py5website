.. title: texture()
.. slug: sketch_texture
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 texture() documentation
.. type: text

Sets a texture to be applied to vertex points.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_texture_0.png
    :alt: example picture for texture()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_stroke()
    img = load_image("laDefense.jpg")
    begin_shape()
    texture(img)
    vertex(10, 20, 0, 0)
    vertex(80, 5, 100, 0)
    vertex(95, 90, 100, 100)
    vertex(40, 95, 0, 100)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a texture to be applied to vertex points. The ``texture()`` function must be called between ``begin_shape()`` and ``end_shape()`` and before any calls to ``vertex()``. This function only works with the P2D and P3D renderers.

When textures are in use, the fill color is ignored. Instead, use ``tint()`` to specify the color of the texture as it is applied to the shape.

Syntax
======

.. code:: python

    texture(image: Py5Image) -> None

Parameters
==========

* **image**: `Py5Image` - reference to a PImage object


Updated on November 03, 2020 22:19:57pm UTC

