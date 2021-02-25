.. title: load_shader()
.. slug: load_shader
.. date: 2021-02-25 16:27:06 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_shader() documentation
.. type: text

Loads a shader into the Py5Shader object.

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
        global blur
        # shaders files must be in the "data" folder to load correctly
        blur = py5.load_shader("blur.glsl")
        py5.stroke(0, 102, 153)
        py5.rect_mode(py5.CENTER)


    def draw():
        py5.apply_filter(blur)
        py5.rect(py5.mouse_x-75, py5.mouse_y, 150, 150)
        py5.ellipse(py5.mouse_x+75, py5.mouse_y, 150, 150)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Loads a shader into the Py5Shader object. The shader file must be loaded in the sketch's "data" folder/directory to load correctly. Shaders are compatible with the P2D and P3D renderers, but not with the default renderer.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the null value may cause a NullPointerException if your code does not check whether the value returned is null.

Underlying Java method: `loadShader <https://processing.org/reference/loadShader_.html>`_

Syntax
======

.. code:: python

    load_shader(frag_filename: str, /) -> Py5Shader
    load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader

Parameters
==========

* **frag_filename**: `str` - name of fragment shader file
* **vert_filename**: `str` - name of vertex shader file


Updated on February 25, 2021 16:27:06pm UTC

