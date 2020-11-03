.. title: PShader
.. slug: py5shader_set
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 PShader documentation
.. type: text

Sets the uniform variables inside the shader to modify the effect while the program is running.

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
        global tex
        global deform
        size(640, 360, P2D)
        tex = load_image("tex1.jpg")
        deform = load_shader("deform.glsl")
        deform.set("resolution", float(width), float(height))


    def draw():
        deform.set("time", millis() / 1000.0)
        deform.set("mouse", float(mouse_x), float(mouse_y))
        shader(deform)
        image(tex, 0, 0, width, height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the uniform variables inside the shader to modify the effect while the program is running.


Updated on November 03, 2020 22:19:57pm UTC

