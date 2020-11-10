.. title: get()
.. slug: get
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get() documentation
.. type: text

Reads the color of any pixel or grabs a section of an image.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_get_0.png
    :alt: example picture for get()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    my_image = load_image("apples.jpg")
    image(my_image, 0, 0)
    c = get()
    image(c, width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_get_1.png
    :alt: example picture for get()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    my_image = load_image("apples.jpg")
    image(my_image, 0, 0)
    c = get(25, 25)
    fill(c)
    no_stroke()
    rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Reads the color of any pixel or grabs a section of an image. If no parameters are specified, the entire image is returned. Use the ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the display window by specifying additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and ``y`` parameters define the coordinates for the upper-left corner of the image, regardless of the current ``image_mode()``.

If the pixel requested is outside of the image window, black is returned. The numbers returned are scaled according to the current color ranges, but only RGB values are returned by this function. For example, even though you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in RGB format.

If a width and a height are specified, ``get(x, y, w, h)`` returns a PImage corresponding to the part of the original PImage where the top left pixel is at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast as grabbing the data directly from ``pixels[]``. The equivalent statement to ``get(x, y)`` using ``pixels[]`` is ``pixels[y*width+x]``. See the reference for pixels[] for more information.

Underlying Java method: `get <https://processing.org/reference/get_.html>`_

Syntax
======

.. code:: python

    get() -> Py5Image
    get(x: int, y: int) -> int
    get(x: int, y: int, w: int, h: int) -> Py5Image

Parameters
==========

* **h**: `int` - height of pixel rectangle to get
* **w**: `int` - width of pixel rectangle to get
* **x**: `int` - x-coordinate of the pixel
* **y**: `int` - y-coordinate of the pixel


Updated on January 01, 1970 00:00:00am UTC

