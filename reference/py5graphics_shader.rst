.. title: Py5Graphics.shader()
.. slug: py5graphics_shader
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.shader() documentation
.. type: text

Applies the shader specified by the parameters.

Description
===========

Applies the shader specified by the parameters. It's compatible with the ``P2D`` and ``P3D`` renderers, but not with the default renderer.

This method is the same as :doc:`shader` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`shader`.

Underlying Java method: PGraphics.shader

Syntax
======

.. code:: python

    shader(shader: Py5Shader, /) -> None
    shader(shader: Py5Shader, kind: int, /) -> None

Parameters
==========

* **kind**: `int` - type of shader, either POINTS, LINES, or TRIANGLES
* **shader**: `Py5Shader` - name of shader file


Updated on May 04, 2021 20:06:05pm UTC

