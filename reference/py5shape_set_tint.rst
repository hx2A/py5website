.. title: set_tint()
.. slug: py5shape_set_tint
.. date: 2021-04-22 15:56:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_tint() documentation
.. type: text

Apply a color tint to a shape's texture map.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_tint_0.png
    :alt: example picture for set_tint()

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

        s.set_tint(0, py5.color(0, 0, 255))
        s.set_tint(2, py5.color(255, 0, 0))
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P2D)


    def setup():
        global s
        img = py5.load_image("tower.jpg")
        s = py5.create_shape()
        s.begin_shape()
        s.texture(img)
        s.tint(0, 0, 255)
        s.vertex(20, 20, 0, 0)
        s.vertex(20, 80, 0, 100)
        s.vertex(80, 80, 100, 100)
        s.vertex(80, 20, 100, 0)
        s.end_shape(py5.CLOSE)


    def draw():
        if py5.frame_count == 50:
            s.set_tint(False)
        if py5.frame_count == 100:
            s.set_tint(py5.color(255, 0, 0))

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Apply a color tint to a shape's texture map. This can be done for either the entire shape or one vertex.

This method differs from :doc:`py5shape_tint` in that it is only to be used outside the :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` methods. This method only works with the ``P2D`` and ``P3D`` renderers.

Calling this method with the boolean parameter ``False`` will delete the assigned tint. A later call with the boolean parameter ``True`` will not restore it; you must reassign the tint color, as shown in the second example.

Underlying Java method: PShape.setTint

Syntax
======

.. code:: python

    set_tint(fill: int, /) -> None
    set_tint(index: int, tint: int, /) -> None
    set_tint(tint: bool, /) -> None

Parameters
==========

* **fill**: `int` - color value in hexadecimal notation
* **index**: `int` - vertex index
* **tint**: `bool` - allow tint
* **tint**: `int` - color value in hexadecimal notation


Updated on April 22, 2021 15:56:35pm UTC

