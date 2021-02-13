.. title: set_vertex()
.. slug: py5shape_set_vertex
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_vertex() documentation
.. type: text

The ``set_vertex()`` method defines the coordinates of the vertex point located at the position defined by the ``index`` parameter.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(0, 0)
        s.vertex(60, 0)
        s.vertex(60, 60)
        s.vertex(0, 60)
        s.end_shape(py5.CLOSE)


    def draw():
        py5.translate(20, 20)
        for i in range(0, s.get_vertex_count()):
            v = s.get_vertex(i)
            v.x += py5.random(-1, 1)
            v.y += py5.random(-1, 1)
            s.set_vertex(i, v)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``set_vertex()`` method defines the coordinates of the vertex point located at the position defined by the ``index`` parameter. This method works when shapes are created as shown in the example above, but won't work properly when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.

Underlying Java method: `PShape.setVertex <https://processing.org/reference/PShape_setVertex_.html>`_

Syntax
======

.. code:: python

    set_vertex(index: int, vec: NDArray[(Any,), Float], /) -> None
    set_vertex(index: int, x: float, y: float, /) -> None
    set_vertex(index: int, x: float, y: float, z: float, /) -> None

Parameters
==========

* **index**: `int` - the location of the vertex
* **vec**: `NDArray[(Any,), Float]` - the PVector to define the x, y, z coordinates
* **x**: `float` - the x value for the vertex
* **y**: `float` - the y value for the vertex
* **z**: `float` - the z value for the vertex


Updated on February 13, 2021 18:02:35pm UTC

