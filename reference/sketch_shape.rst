.. title: shape()
.. slug: shape
.. date: 2021-02-28 03:13:08 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 shape() documentation
.. type: text

Draws shapes to the display window.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_shape_0.png
    :alt: example picture for shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        s = py5.load_shape("bot.svg")


    def draw():
        py5.shape(s, 10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws shapes to the display window. Shapes must be in the sketch's "data" directory to load correctly. Py5 currently works with SVG, OBJ, and custom-created shapes. The ``shape`` parameter specifies the shape to display and the coordinate parameters define the location of the shape from its upper-left corner. The shape is displayed at its original size unless the ``c`` and ``d`` parameters specify a different size. The ``shape_mode()`` function can be used to change the way these parameters are interpreted.

Underlying Java method: `shape <https://processing.org/reference/shape_.html>`_

Syntax
======

.. code:: python

    shape(shape: Py5Shape, /) -> None
    shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None
    shape(shape: Py5Shape, x: float, y: float, /) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the shape
* **b**: `float` - y-coordinate of the shape
* **c**: `float` - width to display the shape
* **d**: `float` - height to display the shape
* **shape**: `Py5Shape` - the shape to display
* **x**: `float` - x-coordinate of the shape
* **y**: `float` - y-coordinate of the shape


Updated on February 28, 2021 03:13:08am UTC

