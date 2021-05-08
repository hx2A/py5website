.. title: Py5Graphics.load_shader()
.. slug: py5graphics_load_shader
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.load_shader() documentation
.. type: text

Loads a shader into a ``Py5Shader`` object.

Description
===========

Loads a shader into a ``Py5Shader`` object. The shader file must be loaded in the Sketch's "data" directory to load correctly. Shaders are compatible with the ``P2D`` and ``P3D`` renderers, but not with the default renderer.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the ``None`` value may cause an error if your code does not check whether the value returned is ``None``.

This method is the same as :doc:`load_shader` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`load_shader`.

Underlying Java method: PGraphics.loadShader

Syntax
======

.. code:: python

    load_shader(frag_filename: str, /) -> Py5Shader
    load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader

Parameters
==========

* **frag_filename**: `str` - name of fragment shader file
* **vert_filename**: `str` - name of vertex shader file


Updated on May 04, 2021 20:06:05pm UTC

