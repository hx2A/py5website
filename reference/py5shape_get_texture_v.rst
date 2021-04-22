.. title: get_texture_v()
.. slug: py5shape_get_texture_v
.. date: 2021-04-22 14:50:01 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_texture_v() documentation
.. type: text

Get the vertical texture mapping coordinate for a particular vertex.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_texture_v_0.png
    :alt: example picture for get_texture_v()

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

        for i in range(s.get_vertex_count()):
            u = s.get_texture_u(i)
            v = s.get_texture_v(i)
            print(f"vertex {i}: u = {u} v = {v}")

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the vertical texture mapping coordinate for a particular vertex. Returned values will always range from 0 to 1, regardless of what the Sketch's :doc:`texture_mode` setting is.

Underlying Java method: PShape.getTextureV

Syntax
======

.. code:: python

    get_texture_v(index: int, /) -> float

Parameters
==========

* **index**: `int` - vertex index


Updated on April 22, 2021 14:50:01pm UTC

