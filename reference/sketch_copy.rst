.. title: copy()
.. slug: copy
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 copy() documentation
.. type: text

Copies a region of pixels from the display window to another area of the display window and copies a region of pixels from an image used as the ``src_img`` parameter into the display window.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_copy_0.png
    :alt: example picture for copy()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("eames.jpg")
    image(img, 0, 0, width, height)
    copy(7, 22, 10, 10, 35, 25, 50, 50)
    stroke(255)
    no_fill()
    # rectangle shows area being copied
    rect(7, 22, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Copies a region of pixels from the display window to another area of the display window and copies a region of pixels from an image used as the ``src_img`` parameter into the display window. If the source and destination regions aren't the same size, it will automatically resize the source pixels to fit the specified target region. No alpha information is used in the process, however if the source image has an alpha channel set, it will be copied as well.

As of release 0149, this function ignores ``image_mode()``.

Underlying Java method: `copy <https://processing.org/reference/copy_.html>`_

Syntax
======

.. code:: python

    copy() -> Py5Image
    copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None
    copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None

Parameters
==========

* **dh**: `int` - destination image height
* **dw**: `int` - destination image width
* **dx**: `int` - X coordinate of the destination's upper left corner
* **dy**: `int` - Y coordinate of the destination's upper left corner
* **sh**: `int` - source image height
* **src**: `Py5Image` - an image variable referring to the source image.
* **sw**: `int` - source image width
* **sx**: `int` - X coordinate of the source's upper left corner
* **sy**: `int` - Y coordinate of the source's upper left corner


Updated on November 24, 2020 21:22:32pm UTC
