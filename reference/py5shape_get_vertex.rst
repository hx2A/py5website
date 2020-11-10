.. title: get_vertex()
.. slug: py5shape_get_vertex
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_vertex() documentation
.. type: text

The ``get_vertex()`` method returns a PVector with the coordinates of the vertex point located at the position defined by the ``index`` parameter.

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
        size(100, 100)
        s = create_shape()
        s.begin_shape()
        s.vertex(0, 0)
        s.vertex(60, 0)
        s.vertex(60, 60)
        s.vertex(0, 60)
        s.end_shape(CLOSE)


    def draw():
        translate(20, 20)
        for i in range(0, s.get_vertex_count()):
            v = s.get_vertex(i)
            v.x += random(-1, 1)
            v.y += random(-1, 1)
            s.set_vertex(i, v)

        shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``get_vertex()`` method returns a PVector with the coordinates of the vertex point located at the position defined by the ``index`` parameter. This method works when shapes are created as shown in the example above, but won't work properly when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.

Underlying Java method: `PShape.getVertex <https://processing.org/reference/PShape_getVertex_.html>`_

Syntax
======

.. code:: python

    get_vertex(index: int) -> NDArray[(Any,), Float]
    get_vertex(index: int, vec: NDArray[(Any,), Float]) -> NDArray[(Any,), Float]

Parameters
==========

* **index**: `int` - the location of the vertex
* **vec**: `NDArray[(Any,), Float]` - PVector to assign the data to


Updated on November 10, 2020 15:41:45pm UTC

