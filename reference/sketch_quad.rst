.. title: quad()
.. slug: quad
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 quad() documentation
.. type: text

A quad is a quadrilateral, a four sided polygon.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quad_0.png
    :alt: example picture for quad()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    quad(38, 31, 86, 20, 69, 63, 30, 76)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

Underlying Java method: `quad <https://processing.org/reference/quad_.html>`_

Syntax
======

.. code:: python

    quad(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None

Parameters
==========

* **x1**: `float` - x-coordinate of the first corner
* **x2**: `float` - x-coordinate of the second corner
* **x3**: `float` - x-coordinate of the third corner
* **x4**: `float` - x-coordinate of the fourth corner
* **y1**: `float` - y-coordinate of the first corner
* **y2**: `float` - y-coordinate of the second corner
* **y3**: `float` - y-coordinate of the third corner
* **y4**: `float` - y-coordinate of the fourth corner


Updated on November 10, 2020 15:41:45pm UTC

