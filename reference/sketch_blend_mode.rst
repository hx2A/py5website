.. title: blend_mode()
.. slug: blend_mode
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 blend_mode() documentation
.. type: text

Blends the pixels in the display window according to a defined mode.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100)
    background(0)
    blend_mode(ADD)
    stroke(102)
    stroke_weight(30)
    line(25, 25, 75, 75)
    line(75, 25, 25, 75)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P2D)
    blend_mode(MULTIPLY)
    stroke(51)
    stroke_weight(30)
    line(25, 25, 75, 75)
    line(75, 25, 25, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Blends the pixels in the display window according to a defined mode. There is a choice of the following modes to blend the source pixels (A) with the ones of pixels already in the display window (B). Each pixel's final color is the result of applying one of the blend modes with each channel of (A) and (B) independently. The red channel is compared with red, green with green, and blue with blue.

BLEND - linear interpolation of colors: C = A*factor + B. This is the default.

ADD - additive blending with white clip: C = min(A*factor + B, 255)

SUBTRACT - subtractive blending with black clip: C = max(B - A*factor, 0)

DARKEST - only the darkest color succeeds: C = min(A*factor, B)

LIGHTEST - only the lightest color succeeds: C = max(A*factor, B)

DIFFERENCE - subtract colors from underlying image.

EXCLUSION - similar to DIFFERENCE, but less extreme.

MULTIPLY - multiply the colors, result will always be darker.

SCREEN - opposite multiply, uses inverse values of the colors.

REPLACE - the pixels entirely replace the others and don't utilize alpha (transparency) values

We recommend using ``blend_mode()`` and not the previous ``blend()`` function. However, unlike ``blend()``, the ``blend_mode()`` function does not support the following: HARD_LIGHT, SOFT_LIGHT, OVERLAY, DODGE, BURN. On older hardware, the LIGHTEST, DARKEST, and DIFFERENCE modes might not be available as well.

Underlying Java method: `blendMode <https://processing.org/reference/blendMode_.html>`_

Syntax
======

.. code:: python

    blend_mode(mode: int) -> None

Parameters
==========

* **mode**: `int` - the blending mode to use


Updated on January 01, 1970 00:00:00am UTC

