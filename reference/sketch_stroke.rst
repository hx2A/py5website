.. title: stroke()
.. slug: sketch_stroke
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 stroke() documentation
.. type: text

Sets the color used to draw lines and borders around shapes.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_0.png
    :alt: example picture for stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    stroke(153)
    rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_1.png
    :alt: example picture for stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    stroke(204, 102, 0)
    rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the color used to draw lines and borders around shapes. This color is either specified in terms of the RGB or HSB color depending on the current ``c``olor_mode()``.`` The default color space is RGB, with each value in the range from 0 to 255. 
 
When using hexadecimal notation to specify a color, use "``#``" or "``0x``" before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses six digits to specify a color (just as colors are typically specified in HTML and CSS). When using the hexadecimal notation starting with "``0x``", the hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components. 
 
The value for the gray parameter must be less than or equal to the current maximum value as specified by ``color_mode()``. The default maximum value is 255.
 
When drawing in 2D with the default renderer, you may need ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of performance). See the ``hint()`` documentation for more details.

Syntax
======

.. code:: python

    stroke(gray: float) -> None
    stroke(gray: float, alpha: float) -> None
    stroke(rgb: int) -> None
    stroke(rgb: int, alpha: float) -> None
    stroke(v1: float, v2: float, v3: float) -> None
    stroke(v1: float, v2: float, v3: float, alpha: float) -> None

Parameters
==========

* **alpha**: `float` - opacity of the stroke
* **gray**: `float` - specifies a value between white and black
* **rgb**: `int` - color value in hexadecimal notation
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 03, 2020 22:19:57pm UTC

