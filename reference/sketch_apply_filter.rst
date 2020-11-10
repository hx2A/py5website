.. title: apply_filter()
.. slug: apply_filter
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 apply_filter() documentation
.. type: text

Filters the display window using a preset filter or with a custom shader.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_0.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(THRESHOLD)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_1.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(GRAY)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_2.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(INVERT)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_3.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(POSTERIZE, 4)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_4.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(BLUR, 6)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_5.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(ERODE)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_6.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("apples.jpg")
    image(img, 0, 0)
    apply_filter(DILATE)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_apply_filter_7.png
    :alt: example picture for apply_filter()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global blur
        global img
        size(100, 100, P2D)
        blur = load_shader("blur.glsl")
        img = load_image("apples.jpg")
        image(img, 0, 0)


    def draw():
        apply_filter(blur)  # blurs more each time through draw()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Filters the display window using a preset filter or with a custom shader. Using a shader with ``apply_filter()`` is much faster than without. Shaders require the P2D or P3D renderer in ``size()``.

The presets options are:

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
Executes a Guassian blur with the level parameter specifying the extent of the blurring. If no parameter is used, the blur is equivalent to Guassian blur of radius 1. Larger values increase the blur.

ERODE
Reduces the light areas. No parameter is used.

DILATE
Increases the light areas. No parameter is used.

Underlying Java method: `filter <https://processing.org/reference/filter_.html>`_

Syntax
======

.. code:: python

    apply_filter(kind: int) -> None
    apply_filter(kind: int, param: float) -> None
    apply_filter(shader: Py5Shader) -> None

Parameters
==========

* **kind**: `int` - Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE
* **param**: `float` - unique for each, see above
* **shader**: `Py5Shader` - the fragment shader to apply


Updated on November 10, 2020 15:41:45pm UTC

