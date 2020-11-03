.. title: shader()
.. slug: sketch_shader
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 shader() documentation
.. type: text

Applies the shader specified by the parameters.

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

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Applies the shader specified by the parameters. It's compatible with the P2D and P3D renderers, but not with the default renderer.

Syntax
======

.. code:: python

    shader(shader: Py5Shader) -> None
    shader(shader: Py5Shader, kind: int) -> None

Parameters
==========

* **kind**: `int` - type of shader, either POINTS, LINES, or TRIANGLES
* **shader**: `Py5Shader` - name of shader file


Updated on November 03, 2020 22:19:57pm UTC

