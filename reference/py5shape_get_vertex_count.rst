.. title: Py5Shape.get_vertex_count()
.. slug: py5shape_get_vertex_count
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_vertex_count() documentation
.. type: text

The ``get_vertex_count()`` method returns the number of vertices that make up a ``Py5Shape``.

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
            v[0] += py5.random(-1, 1)
            v[1] += py5.random(-1, 1)
            s.set_vertex(i, v)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``get_vertex_count()`` method returns the number of vertices that make up a ``Py5Shape``. In the example, the value 4 is returned by the ``get_vertex_count()`` method because 4 vertices are defined in ``setup()``.

Underlying Java method: `PShape.getVertexCount <https://processing.org/reference/PShape_getVertexCount_.html>`_

Syntax
======

.. code:: python

    get_vertex_count() -> int

Updated on May 01, 2021 20:51:42pm UTC

