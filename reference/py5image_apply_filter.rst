.. title: apply_filter()
.. slug: py5image_apply_filter
.. date: 2020-11-24 21:52:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 apply_filter() documentation
.. type: text

Apply an image filter.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_0.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        size(100, 100)
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img1.apply_filter(THRESHOLD, 0.3)
        img2.apply_filter(THRESHOLD, 0.7)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_1.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img2.apply_filter(GRAY)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_2.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img2.apply_filter(INVERT)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_3.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img2.apply_filter(POSTERIZE, 4)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_4.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img2.apply_filter(BLUR, 6)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_5.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img2.apply_filter(ERODE)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_apply_filter_6.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img1
        global img2
        img1 = load_image("apples.jpg")
        img2 = load_image("apples.jpg")
        img2.apply_filter(DILATE)


    def draw():
        image(img1, 0, 0)
        image(img2, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Apply an image filter.

Filters the image as defined by one of the following modes:

THRESHOLD
Converts the image to black and white pixels depending if they are above or below the threshold defined by the level parameter. The parameter must be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.

GRAY
Converts any colors in the image to grayscale equivalents. No parameter is used.

OPAQUE
Sets the alpha channel to entirely opaque. No parameter is used.

INVERT
Sets each pixel to its inverse value. No parameter is used.

POSTERIZE
Limits each channel of the image to the number of colors specified as the parameter. The parameter can be set to values between 2 and 255, but results are most noticeable in the lower ranges.

BLUR
Executes a Gaussian blur with the level parameter specifying the extent of the blurring. If no parameter is used, the blur is equivalent to Gaussian blur of radius 1. Larger values increase the blur.

ERODE
Reduces the light areas. No parameter is used.

DILATE
Increases the light areas. No parameter is used.

Underlying Java method: `PImage.filter <https://processing.org/reference/PImage_filter_.html>`_

Syntax
======

.. code:: python

    apply_filter(kind: int, /) -> None
    apply_filter(kind: int, param: float, /) -> None

Parameters
==========

* **kind**: `int` - Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE
* **param**: `float` - unique for each, see above


Updated on November 24, 2020 21:52:12pm UTC

