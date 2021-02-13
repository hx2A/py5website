.. title: Py5Image
.. slug: py5image
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Image documentation
.. type: text

Datatype for storing images.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_0.png
    :alt: example picture for Py5Image

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global photo
        photo = py5.load_image("laDefense.jpg")


    def draw():
        py5.image(photo, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Datatype for storing images. Processing can display ``.gif``, ``.jpg``, ``.tga``, and ``.png`` images. Images may be displayed in 2D and 3D space. Before an image is used, it must be loaded with the ``load_image()`` function. The ``Py5Image`` class contains fields for the ``width`` and ``height`` of the image, as well as an array called ``pixels[]`` that contains the values for every pixel in the image. The methods described below allow easy access to the image's pixels and alpha channel and simplify the process of compositing.

Before using the ``pixels[]`` array, be sure to use the ``load_pixels()`` method on the image to make sure that the pixel data is properly loaded.

To create a new image, use the ``create_image()`` function. Do not use the syntax ``new Py5Image()``.

Underlying Java class: `PImage <https://processing.org/reference/PImage.html>`_

This class provides the following methods and fields:

.. include:: include/py5image_include.rst

Updated on February 13, 2021 18:02:35pm UTC

