.. title: no_clip()
.. slug: sketch_no_clip
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_clip() documentation
.. type: text

Disables the clipping previously started by the ``clip()`` function.

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
        size(200, 200)
        image_mode(CENTER)


    def draw():
        background(204)
        if is_mouse_pressed():
            clip(mouse_x, mouse_y, 100, 100)
        else:
            no_clip()

        line(0, 0, width, height)
        line(0, height, width, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Disables the clipping previously started by the ``clip()`` function.

Underlying Java method: `noClip <https://processing.org/reference/noClip_.html>`_

Syntax
======

.. code:: python

    no_clip() -> None

Updated on November 04, 2020 20:45:44pm UTC

