.. title: create_image()
.. slug: create_image
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_image() documentation
.. type: text

Creates a new PImage (the datatype for storing images).

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_create_image_0.png
    :alt: example picture for create_image()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = create_image(66, 66, RGB)
    img.load_pixels()
    for i in range(0, len(img.pixels)):
        img.pixels[i] = color(0, 90, 102)

    img.update_pixels()
    image(img, 17, 17)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_create_image_1.png
    :alt: example picture for create_image()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = create_image(66, 66, ARGB)
    img.load_pixels()
    for i in range(0, len(img.pixels)):
        img.pixels[i] = color(0, 90, 102, i % img.width * 2)

    img.update_pixels()
    image(img, 17, 17)
    image(img, 34, 34)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Creates a new PImage (the datatype for storing images). This provides a fresh buffer of pixels to play with. Set the size of the buffer with the ``width`` and ``height`` parameters. The ``format`` parameter defines how the pixels are stored. See the PImage reference for more information.
 
Be sure to include all three parameters, specifying only the width and height (but no format) will produce a strange error.
 
Advanced users please note that ``create_image()`` should be used instead of the syntax ``new Py5Image()``.

Underlying Java method: `createImage <https://processing.org/reference/createImage_.html>`_

Syntax
======

.. code:: python

    create_image(w: int, h: int, format: int, /) -> Py5Image

Parameters
==========

* **format**: `int` - Either RGB, ARGB, ALPHA (grayscale alpha channel)
* **h**: `int` - height in pixels
* **w**: `int` - width in pixels


Updated on November 24, 2020 21:22:32pm UTC
