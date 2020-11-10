.. title: color()
.. slug: color
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 color() documentation
.. type: text

Creates colors for storing in variables of the ``color`` datatype.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_color_0.png
    :alt: example picture for color()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    c = color(255, 204, 0)  # define color 'c'
    fill(c)  # use color variable 'c' as fill color
    no_stroke()  # don't draw a stroke around shapes
    rect(30, 20, 55, 55)  # draw rectangle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_color_1.png
    :alt: example picture for color()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    c = color(255, 204, 0)  # define color 'c'
    fill(c)  # use color variable 'c' as fill color
    no_stroke()  # don't draw a stroke around shapes
    ellipse(25, 25, 80, 80)  # draw left circle

    # using only one value with color()
    # generates a grayscale value.
    c = color(65)  # update 'c' with grayscale value
    fill(c)  # use updated 'c' as fill color
    ellipse(75, 75, 80, 80)  # draw right circle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_color_2.png
    :alt: example picture for color()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    color c  # declare color 'c'
    no_stroke()  # don't draw a stroke around shapes

    # if no color_mode is specified, then the
    # default of RGB with scale of 0-255 is used.
    c = color(50, 55, 100)  # create a color for 'c'
    fill(c)  # use color variable 'c' as fill color
    rect(0, 10, 45, 80)  # draw left rect

    color_mode(HSB, 100)  # use HSB with scale of 0-100
    c = color(50, 55, 100)  # update 'c' with new color
    fill(c)  # use updated 'c' as fill color
    rect(55, 10, 45, 80)  # draw right rect

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Creates colors for storing in variables of the ``color`` datatype. The parameters are interpreted as RGB or HSB values depending on the current ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color (see the first example above).

Note that if only one value is provided to ``color()``, it will be interpreted as a grayscale value. Add a second value, and it will be used for alpha transparency. When three values are specified, they are interpreted as either RGB or HSB values. Adding a fourth value applies alpha transparency.

Note that when using hexadecimal notation, it is not necessary to use ``color()``, as in: ``c = 0x006699``

More about how colors are stored can be found in the reference for the color datatype.

Underlying Java method: `color <https://processing.org/reference/color_.html>`_

Syntax
======

.. code:: python

    color(fgray: float) -> int
    color(fgray: float, falpha: float) -> int
    color(gray: int) -> int
    color(gray: int, alpha: int) -> int
    color(v1: float, v2: float, v3: float) -> int
    color(v1: float, v2: float, v3: float, alpha: float) -> int
    color(v1: int, v2: int, v3: int) -> int
    color(v1: int, v2: int, v3: int, alpha: int) -> int

Parameters
==========

* **alpha**: `float` - relative to current color range
* **alpha**: `int` - relative to current color range
* **falpha**: `float` - missing variable description
* **fgray**: `float` - number specifying value between white and black
* **gray**: `int` - number specifying value between white and black
* **v1**: `float` - red or hue values relative to the current color range
* **v1**: `int` - red or hue values relative to the current color range
* **v2**: `float` - green or saturation values relative to the current color range
* **v2**: `int` - green or saturation values relative to the current color range
* **v3**: `float` - blue or brightness values relative to the current color range
* **v3**: `int` - blue or brightness values relative to the current color range


Updated on November 10, 2020 15:41:45pm UTC

