.. title: normal()
.. slug: sketch_normal
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 normal() documentation
.. type: text

Sets the current normal vector.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_normal_0.png
    :alt: example picture for normal()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_stroke()
    background(0)
    point_light(150, 250, 150, 10, 30, 50)
    begin_shape()
    normal(0, 0, 1)
    vertex(20, 20, -10)
    vertex(80, 20, 10)
    vertex(80, 80, -10)
    vertex(20, 80, 10)
    end_shape(CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the current normal vector. Used for drawing three dimensional shapes and surfaces, ``normal()`` specifies a vector perpendicular to a shape's surface which, in turn, determines how lighting affects it. Processing attempts to automatically assign normals to shapes, but since that's imperfect, this is a better option when you want more control. This function is identical to ``gl_normal3f()`` in OpenGL.

Syntax
======

.. code:: python

    normal(nx: float, ny: float, nz: float) -> None

Parameters
==========

* **nx**: `float` - x direction
* **ny**: `float` - y direction
* **nz**: `float` - z direction


Updated on November 03, 2020 22:19:57pm UTC

