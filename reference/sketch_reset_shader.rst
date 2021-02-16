.. title: reset_shader()
.. slug: reset_shader
.. date: 2021-02-16 16:54:21 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 reset_shader() documentation
.. type: text

Restores the default shaders.

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

    def settings():
        py5.size(640, 360, py5.P2D)


    def setup():
        global edges
        global img
        img = py5.load_image("leaves.jpg")
        edges = py5.load_shader("edges.glsl")


    def draw():
        py5.shader(edges)
        py5.image(img, 0, 0)
        py5.reset_shader()
        py5.image(img, py5.width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Restores the default shaders. Code that runs after ``reset_shader()`` will not be affected by previously defined shaders.

Underlying Java method: `resetShader <https://processing.org/reference/resetShader_.html>`_

Syntax
======

.. code:: python

    reset_shader() -> None
    reset_shader(kind: int, /) -> None

Parameters
==========

* **kind**: `int` - type of shader, either POINTS, LINES, or TRIANGLES


Updated on February 16, 2021 16:54:21pm UTC

