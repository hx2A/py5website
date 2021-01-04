.. title: vertex()
.. slug: vertex
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 vertex() documentation
.. type: text

All shapes are constructed by connecting a series of vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertex_0.png
    :alt: example picture for vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    begin_shape(POINTS)
    vertex(30, 20)
    vertex(85, 20)
    vertex(85, 75)
    vertex(30, 75)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertex_1.png
    :alt: example picture for vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # drawing vertices in 3D requires P3D
    # as a parameter to size()
    size(100, 100, P3D)
    begin_shape(POINTS)
    vertex(30, 20, -50)
    vertex(85, 20, -50)
    vertex(85, 75, -50)
    vertex(30, 75, -50)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertex_2.png
    :alt: example picture for vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    img = load_image("laDefense.jpg")
    no_stroke()
    begin_shape()
    texture(img)
    # "laDefense.jpg" is 100x100 pixels in size so
    # the values 0 and 100 are used for the
    # parameters "u" and "v" to map it directly
    # to the vertex points
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

All shapes are constructed by connecting a series of vertices. ``vertex()`` is used to specify the vertex coordinates for points, lines, triangles, quads, and polygons. It is used exclusively within the ``begin_shape()`` and ``end_shape()`` functions.

Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in combination with size, as shown in the above example.

This function is also used to map a texture onto geometry. The ``texture()`` function declares the texture to apply to the geometry and the ``u`` and ``v`` coordinates set define the mapping of this texture to the form. By default, the coordinates used for ``u`` and ``v`` are specified in relation to the image's size in pixels, but this relation can be changed with ``texture_mode()``.

Underlying Java method: `vertex <https://processing.org/reference/vertex_.html>`_

Syntax
======

.. code:: python

    vertex(v: NDArray[(Any,), Float], /) -> None
    vertex(x: float, y: float, /) -> None
    vertex(x: float, y: float, u: float, v: float, /) -> None
    vertex(x: float, y: float, z: float, /) -> None
    vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

Parameters
==========

* **u**: `float` - horizontal coordinate for the texture mapping
* **v**: `NDArray[(Any,), Float]` - vertical coordinate for the texture mapping
* **v**: `float` - vertical coordinate for the texture mapping
* **x**: `float` - x-coordinate of the vertex
* **y**: `float` - y-coordinate of the vertex
* **z**: `float` - z-coordinate of the vertex


Updated on November 24, 2020 21:22:32pm UTC
