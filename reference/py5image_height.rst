.. title: height
.. slug: py5image_height
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 height documentation
.. type: text

The height of the image in units of pixels.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_height_0.png
    :alt: example picture for height

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

The height of the image in units of pixels.

Underlying Java field: `PImage.height <https://processing.org/reference/PImage_height.html>`_


Updated on February 13, 2021 18:02:35pm UTC

