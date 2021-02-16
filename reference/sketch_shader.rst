.. title: shader()
.. slug: shader
.. date: 2021-02-16 16:54:21 UTC+00:00
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

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Applies the shader specified by the parameters. It's compatible with the P2D and P3D renderers, but not with the default renderer.

Underlying Java method: `shader <https://processing.org/reference/shader_.html>`_

Syntax
======

.. code:: python

    shader(shader: Py5Shader, /) -> None
    shader(shader: Py5Shader, kind: int, /) -> None

Parameters
==========

* **kind**: `int` - type of shader, either POINTS, LINES, or TRIANGLES
* **shader**: `Py5Shader` - name of shader file


Updated on February 16, 2021 16:54:21pm UTC

