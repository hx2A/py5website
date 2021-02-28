.. title: texture_wrap()
.. slug: texture_wrap
.. date: 2021-02-28 03:31:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 texture_wrap() documentation
.. type: text

Defines if textures repeat or draw once within a texture map.

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
        py5.size(300, 300, py5.P2D)


    def setup():
        global img
        img = py5.load_image("berlin-1.jpg")
        py5.texture_mode(py5.NORMAL)


    def draw():
        py5.background(0)
        py5.translate(py5.width//2, py5.height//2)
        py5.rotate(py5.remap(py5.mouse_x, 0, py5.width, -py5.PI, py5.PI))
        if py5.is_mouse_pressed:
            py5.texture_wrap(py5.REPEAT)
        else:
            py5.texture_wrap(py5.CLAMP)

        py5.begin_shape()
        py5.texture(img)
        py5.vertex(-100, -100, 0, 0)
        py5.vertex(100, -100, 2, 0)
        py5.vertex(100, 100, 2, 2)
        py5.vertex(-100, 100, 0, 2)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Defines if textures repeat or draw once within a texture map. The two parameters are ``CLAMP`` (the default behavior) and ``REPEAT``. This function only works with the P2D and P3D renderers.

Underlying Java method: `textureWrap <https://processing.org/reference/textureWrap_.html>`_

Syntax
======

.. code:: python

    texture_wrap(wrap: int, /) -> None

Parameters
==========

* **wrap**: `int` - Either CLAMP (default) or REPEAT


Updated on February 28, 2021 03:31:12am UTC

