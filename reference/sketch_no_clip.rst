.. title: no_clip()
.. slug: no_clip
.. date: 1970-01-01 00:00:00 UTC+00:00
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

Updated on January 01, 1970 00:00:00am UTC

