.. title: create_image()
.. slug: create_image
.. date: 2021-08-20 15:31:10 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_image() documentation
.. type: text

Creates a new Py5Image (the datatype for storing images).

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

    def setup():
        img = py5.create_image(66, 66, py5.RGB)
        img.load_pixels()
        for i in range(0, len(img.pixels)):
            img.pixels[i] = "#005A66"
    
        img.update_pixels()
        py5.image(img, 17, 17)

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

    def setup():
        img = py5.create_image(66, 66, py5.ARGB)
        img.load_pixels()
        for i in range(0, len(img.pixels)):
            img.pixels[i] = py5.color(0, 90, 102, i%img.width*2)
    
        img.update_pixels()
        py5.image(img, 17, 17)
        py5.image(img, 34, 34)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Creates a new Py5Image (the datatype for storing images). This provides a fresh buffer of pixels to play with. Set the size of the buffer with the ``w`` and ``h`` parameters. The ``format`` parameter defines how the pixels are stored. See the :doc:`py5image` reference for more information.
 
Be sure to include all three parameters, specifying only the width and height (but no format) will produce a strange error.
 
Advanced users please note that ``create_image()`` should be used instead of the syntax ``Py5Image()``.

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


Updated on August 20, 2021 15:31:10pm UTC

