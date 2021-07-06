.. title: Py5Shape.get_texture_u()
.. slug: py5shape_get_texture_u
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_texture_u() documentation
.. type: text

Get the horizontal texture mapping coordinate for a particular vertex.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_texture_u_0.png
    :alt: example picture for get_texture_u()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
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

        for i in range(s.get_vertex_count()):
            u = s.get_texture_u(i)
            v = s.get_texture_v(i)
            py5.println(f"vertex {i}: u = {u} v = {v}")

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the horizontal texture mapping coordinate for a particular vertex. Returned values will always range from 0 to 1, regardless of what the Sketch's :doc:`texture_mode` setting is.

Underlying Java method: PShape.getTextureU

Syntax
======

.. code:: python

    get_texture_u(index: int, /) -> float

Parameters
==========

* **index**: `int` - vertex index


Updated on July 06, 2021 22:46:12pm UTC

