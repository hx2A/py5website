.. title: color_mode()
.. slug: color_mode
.. date: 2021-03-05 15:24:25 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 color_mode() documentation
.. type: text

Changes the way py5 interprets color data.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_color_mode_0.png
    :alt: example picture for color_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.color_mode(py5.RGB, 100)
        for i in range(0, 100):
            for j in range(0, 100):
                py5.stroke(i, j, 0)
                py5.point(i, j)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_color_mode_1.png
    :alt: example picture for color_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.color_mode(py5.HSB, 100)
        for i in range(0, 100):
            for j in range(0, 100):
                py5.stroke(i, j, 100)
                py5.point(i, j)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_color_mode_2.png
    :alt: example picture for color_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.color_mode(py5.HSB, 360, 100, 100)
        # use the global keyword so the draw method
        # has access to the bg variable
        global bg
        bg = py5.color(180, 50, 50)


    def draw():
        py5.background(bg)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Changes the way py5 interprets color data. By default, the parameters for :doc:`fill`, :doc:`stroke`, :doc:`background`, and :doc:`color` are defined by values between 0 and 255 using the ``RGB`` color model. The ``color_mode()`` function is used to change the numerical range used for specifying colors and to switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified between 0 and 1. The limits for defining colors are altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

After changing the range of values for colors with code like ``color_mode(HSB, 360, 100, 100)``, those ranges remain in use until they are explicitly changed again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the range for G and B will be 0 to 100. To avoid this, be explicit about the ranges when changing the color mode. For instance, instead of ``color_mode(RGB)``, write ``color_mode(RGB, 255, 255, 255)``.

Underlying Java method: `colorMode <https://processing.org/reference/colorMode_.html>`_

Syntax
======

.. code:: python

    color_mode(mode: int, /) -> None
    color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None
    color_mode(mode: int, max1: float, max2: float, max3: float, max_a: float, /) -> None
    color_mode(mode: int, max: float, /) -> None

Parameters
==========

* **max1**: `float` - range for the red or hue depending on the current color mode
* **max2**: `float` - range for the green or saturation depending on the current color mode
* **max3**: `float` - range for the blue or brightness depending on the current color mode
* **max**: `float` - range for all color elements
* **max_a**: `float` - range for the alpha
* **mode**: `int` - Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness


Updated on March 05, 2021 15:24:25pm UTC

