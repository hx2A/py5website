.. title: width
.. slug: py5image_width
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 width documentation
.. type: text

The width of the image in units of pixels.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_width_0.png
    :alt: example picture for width

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        tiles = py5.load_image("tiles.jpg")
        py5.image(tiles, 20, 10)
        py5.rect(55, 10, tiles.width, tiles.height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The width of the image in units of pixels.

Underlying Java field: `PImage.width <https://processing.org/reference/PImage_width.html>`_


Updated on February 13, 2021 18:02:35pm UTC

