.. title: reset_shader()
.. slug: reset_shader
.. date: 2020-11-24 21:22:32 UTC+00:00
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

    def setup():
        global edges
        global img
        size(640, 360, P2D)
        img = load_image("leaves.jpg")
        edges = load_shader("edges.glsl")


    def draw():
        shader(edges)
        image(img, 0, 0)
        reset_shader()
        image(img, width//2, 0)

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


Updated on November 24, 2020 21:22:32pm UTC

