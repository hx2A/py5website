.. title: texture_wrap()
.. slug: sketch_texture_wrap
.. date: 2020-11-03 22:19:57 UTC+00:00
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

    def setup():
        global img
        size(300, 300, P2D)
        img = load_image("berlin-1.jpg")
        texture_mode(NORMAL)


    def draw():
        background(0)
        translate(width//2, height//2)
        rotate(map(mouse_x, 0, width, -PI, PI))
        if is_mouse_pressed():
            texture_wrap(REPEAT)
        else:
            texture_wrap(CLAMP)

        begin_shape()
        texture(img)
        vertex(-100, -100, 0, 0)
        vertex(100, -100, 2, 0)
        vertex(100, 100, 2, 2)
        vertex(-100, 100, 0, 2)
        end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Defines if textures repeat or draw once within a texture map. The two parameters are CLAMP (the default behavior) and REPEAT. This function only works with the P2D and P3D renderers.

Syntax
======

.. code:: python

    texture_wrap(wrap: int) -> None

Parameters
==========

* **wrap**: `int` - Either CLAMP (default) or REPEAT


Updated on November 03, 2020 22:19:57pm UTC

