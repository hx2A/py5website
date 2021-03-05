.. title: point()
.. slug: point
.. date: 2021-03-05 14:12:21 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 point() documentation
.. type: text

Draws a point, a coordinate in space at the dimension of one pixel.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_point_0.png
    :alt: example picture for point()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.no_smooth()


    def setup():
        py5.point(30, 20)
        py5.point(85, 20)
        py5.point(85, 75)
        py5.point(30, 75)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_point_1.png
    :alt: example picture for point()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)
        py5.no_smooth()


    def setup():
        py5.point(30, 20, -50)
        py5.point(85, 20, -50)
        py5.point(85, 75, -50)
        py5.point(30, 75, -50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws a point, a coordinate in space at the dimension of one pixel. The first parameter is the horizontal value for the point, the second value is the vertical value for the point, and the optional third value is the depth value. Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` parameter in combination with :doc:`size` as shown in the above example.

Use :doc:`stroke` to set the color of a ``point()``.

Point appears round with the default ``stroke_cap(ROUND)`` and square with ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no cap).

Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the screen, depending on the graphics settings of the computer. Workarounds include setting the pixel using the :doc:`pixels` or :doc:`np_pixels` arrays or drawing the point using either :doc:`circle` or :doc:`square`.

Underlying Java method: `point <https://processing.org/reference/point_.html>`_

Syntax
======

.. code:: python

    point(x: float, y: float, /) -> None
    point(x: float, y: float, z: float, /) -> None

Parameters
==========

* **x**: `float` - x-coordinate of the point
* **y**: `float` - y-coordinate of the point
* **z**: `float` - z-coordinate of the point


Updated on March 05, 2021 14:12:21pm UTC

