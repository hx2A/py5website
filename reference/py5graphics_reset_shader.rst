.. title: Py5Graphics.reset_shader()
.. slug: py5graphics_reset_shader
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.reset_shader() documentation
.. type: text

Restores the default shaders.

Description
===========

Restores the default shaders. Code that runs after ``reset_shader()`` will not be affected by previously defined shaders.

This method is the same as :doc:`reset_shader` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`reset_shader`.

Underlying Java method: PGraphics.resetShader

Syntax
======

.. code:: python

    reset_shader() -> None
    reset_shader(kind: int, /) -> None

Parameters
==========

* **kind**: `int` - type of shader, either POINTS, LINES, or TRIANGLES


Updated on May 04, 2021 20:06:05pm UTC

