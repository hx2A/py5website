.. title: Py5Shader
.. slug: py5shader
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shader documentation
.. type: text

This class encapsulates a GLSL shader program, including a vertex and a fragment shader.

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
        global blur
        py5.size(640, 360, py5.P2D)
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

This class encapsulates a GLSL shader program, including a vertex and a fragment shader. It's compatible with the P2D and P3D renderers, but not with the default renderer. Use the ``load_shader()`` function to load your shader code. [Note: It's strongly encouraged to use ``load_shader()`` to create a PShader object, rather than calling the PShader constructor manually.]

Underlying Java class: `PShader <https://processing.org/reference/PShader.html>`_

This class provides the following methods and fields:

.. include:: include/py5shader_include.rst

Updated on February 13, 2021 18:02:35pm UTC

