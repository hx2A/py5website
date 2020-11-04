.. title: image()
.. slug: sketch_image
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 image() documentation
.. type: text

The ``image()`` function draws an image to the display window.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_image_0.png
    :alt: example picture for image()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img
        # images must be in the "data" directory to load correctly
        img = load_image("laDefense.jpg")


    def draw():
        image(img, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_image_1.png
    :alt: example picture for image()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img
        # images must be in the "data" directory to load correctly
        img = load_image("laDefense.jpg")


    def draw():
        image(img, 0, 0)
        image(img, 0, 0, width//2, height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``image()`` function draws an image to the display window. Images must be in the sketch's "data" directory to load correctly. Select "Add file..." from the "Sketch" menu to add the image to the data directory, or just drag the image file onto the sketch window. Processing currently works with GIF, JPEG, and PNG images. 

The ``img`` parameter specifies the image to display and by default the ``a`` and ``b`` parameters define the location of its upper-left corner. The image is displayed at its original size unless the ``c`` and ``d`` parameters specify a different size. The ``image_mode()`` function can be used to change the way these parameters draw the image.

The color of an image may be modified with the ``tint()`` function. This function will maintain transparency for GIF and PNG images.

Underlying Java method: `image <https://processing.org/reference/image_.html>`_

Syntax
======

.. code:: python

    image(img: Py5Image, a: float, b: float) -> None
    image(img: Py5Image, a: float, b: float, c: float, d: float) -> None
    image(img: Py5Image, a: float, b: float, c: float, d: float, u1: int, v1: int, u2: int, v2: int) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the image by default
* **b**: `float` - y-coordinate of the image by default
* **c**: `float` - width to display the image by default
* **d**: `float` - height to display the image by default
* **img**: `Py5Image` - the image to display
* **u1**: `int` - missing variable description
* **u2**: `int` - missing variable description
* **v1**: `int` - missing variable description
* **v2**: `int` - missing variable description


Updated on November 04, 2020 20:45:44pm UTC

