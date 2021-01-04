.. title: tint()
.. slug: tint
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 tint() documentation
.. type: text

Sets the fill value for displaying images.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tint_0.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("laDefense.jpg")
    image(img, 0, 0)
    tint(0, 153, 204)  # tint blue
    image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tint_1.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("laDefense.jpg")
    image(img, 0, 0)
    tint(0, 153, 204, 126)  # tint blue and set transparency
    image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tint_2.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("laDefense.jpg")
    image(img, 0, 0)
    tint(255, 126)  # apply transparency without changing color
    image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the fill value for displaying images. Images can be tinted to specified colors or made transparent by including an alpha value. 

To apply transparency to an image without affecting its color, use white as the tint color and specify an alpha value. For instance, ``tint(255, 128)`` will make an image 50% transparent (assuming the default alpha range of 0-255, which can be changed with ``color_mode()``).

When using hexadecimal notation to specify a color, use "``#``" or "``0x``" before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses six digits to specify a color (just as colors are typically specified in HTML and CSS). When using the hexadecimal notation starting with "``0x``", the hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components. 

The value for the gray parameter must be less than or equal to the current maximum value as specified by ``color_mode()``. The default maximum value is 255.

The ``tint()`` function is also used to control the coloring of textures in 3D.

Underlying Java method: `tint <https://processing.org/reference/tint_.html>`_

Syntax
======

.. code:: python

    tint(gray: float, /) -> None
    tint(gray: float, alpha: float, /) -> None
    tint(rgb: int, /) -> None
    tint(rgb: int, alpha: float, /) -> None
    tint(v1: float, v2: float, v3: float, /) -> None
    tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

Parameters
==========

* **alpha**: `float` - opacity of the image
* **gray**: `float` - specifies a value between white and black
* **rgb**: `int` - color value in hexadecimal notation
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 24, 2020 21:22:32pm UTC
