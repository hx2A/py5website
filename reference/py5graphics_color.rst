.. title: Py5Graphics.color()
.. slug: py5graphics_color
.. date: 2021-05-04 20:26:15 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.color() documentation
.. type: text

Creates colors for storing in variables of the ``color`` datatype (a 32 bit integer).

Description
===========

Creates colors for storing in variables of the ``color`` datatype (a 32 bit integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending on the current :doc:`py5graphics_color_mode`. The default mode is ``RGB`` values from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color (see the first example).

Note that if only one value is provided to ``color()``, it will be interpreted as a grayscale value. Add a second value, and it will be used for alpha transparency. When three values are specified, they are interpreted as either ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

Note that when using hexadecimal notation, it is not necessary to use ``color()``, as in: ``c = 0x006699``

This method is the same as :doc:`color` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`color`.

Underlying Java method: PGraphics.color

Syntax
======

.. code:: python

    color(c: int, /) -> int
    color(c: int, alpha: float, /) -> int
    color(c: int, alpha: int, /) -> int
    color(gray: float, /) -> int
    color(gray: float, alpha: float, /) -> int
    color(v1: float, v2: float, v3: float, /) -> int
    color(v1: float, v2: float, v3: float, a: float, /) -> int
    color(v1: int, v2: int, v3: int, /) -> int
    color(v1: int, v2: int, v3: int, a: int, /) -> int

Parameters
==========

* **a**: `float` - alpha value relative to current color range
* **a**: `int` - alpha value relative to current color range
* **alpha**: `float` - alpha value relative to current color range
* **alpha**: `int` - alpha value relative to current color range
* **c**: `int` - color value
* **gray**: `float` - gray value relative to current color range
* **v1**: `float` - red or hue values relative to the current color range
* **v1**: `int` - red or hue values relative to the current color range
* **v2**: `float` - green or saturation values relative to the current color range
* **v2**: `int` - green or saturation values relative to the current color range
* **v3**: `float` - blue or brightness values relative to the current color range
* **v3**: `int` - blue or brightness values relative to the current color range


Updated on May 04, 2021 20:26:15pm UTC

