.. title: Py5Shape.get_tint()
.. slug: py5shape_get_tint
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_tint() documentation
.. type: text

Get the texture tint color assigned to one vertex in a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_tint_0.png
    :alt: example picture for get_tint()

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
        s.tint(0, 0, 255)
        s.vertex(20, 20, 0, 0)
        s.vertex(20, 80, 0, 100)
        s.no_tint()
        s.vertex(80, 80, 100, 100)
        s.vertex(80, 20, 100, 0)
        s.end_shape(py5.CLOSE)

        py5.shape(s)

        for i in range(s.get_vertex_count()):
            tint = s.get_tint(i)
            r, g, b = py5.red(tint), py5.green(tint), py5.blue(tint)
            print(f"vertex {i}: r = {r} g = {g} b = {b}")

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the texture tint color assigned to one vertex in a ``Py5Shape`` object. If the vertex has no assigned tint, the returned color value will be white.

Underlying Java method: PShape.getTint

Syntax
======

.. code:: python

    get_tint(index: int, /) -> int

Parameters
==========

* **index**: `int` - vertex index


Updated on May 01, 2021 20:51:42pm UTC

