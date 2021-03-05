.. title: arc()
.. slug: arc
.. date: 2021-03-04 19:43:58 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 arc() documentation
.. type: text

Draws an arc to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_arc_0.png
    :alt: example picture for arc()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.arc(50, 55, 50, 50, 0, py5.HALF_PI)
        py5.no_fill()
        py5.arc(50, 55, 60, 60, py5.HALF_PI, py5.PI)
        py5.arc(50, 55, 70, 70, py5.PI, py5.PI+py5.QUARTER_PI)
        py5.arc(50, 55, 80, 80, py5.PI+py5.QUARTER_PI, py5.TWO_PI)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_arc_1.png
    :alt: example picture for arc()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.arc(50, 50, 80, 80, 0, py5.PI+py5.QUARTER_PI, py5.OPEN)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_arc_2.png
    :alt: example picture for arc()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.arc(50, 50, 80, 80, 0, py5.PI+py5.QUARTER_PI, py5.CHORD)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_arc_3.png
    :alt: example picture for arc()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.arc(50, 50, 80, 80, 0, py5.PI+py5.QUARTER_PI, py5.PIE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the arc's ellipse may be changed with the :doc:`ellipse_mode` function. Use the ``start`` and ``stop`` parameters to specify the angles (in radians) at which to draw the arc. The start/stop values must be in clockwise order.

There are three ways to draw an arc; the rendering technique used is defined by the optional seventh parameter. The three options, depicted in the examples, are ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a ``PIE`` fill.

In some cases, the ``arc()`` function isn't accurate enough for smooth drawing. For example, the shape may jitter on screen when rotating slowly. If you're having an issue with how arcs are rendered, you'll need to draw the arc yourself with :doc:`begin_shape` & :doc:`end_shape` or a ``Py5Shape``.

Underlying Java method: `arc <https://processing.org/reference/arc_.html>`_

Syntax
======

.. code:: python

    arc(a: float, b: float, c: float, d: float, start: float, stop: float, /) -> None
    arc(a: float, b: float, c: float, d: float, start: float, stop: float, mode: int, /) -> None

Parameters
==========

* **a**: `float` - x-coordinate of the arc's ellipse
* **b**: `float` - y-coordinate of the arc's ellipse
* **c**: `float` - width of the arc's ellipse by default
* **d**: `float` - height of the arc's ellipse by default
* **mode**: `int` - arc drawing mode
* **start**: `float` - angle to start the arc, specified in radians
* **stop**: `float` - angle to stop the arc, specified in radians


Updated on March 04, 2021 19:43:58pm UTC

