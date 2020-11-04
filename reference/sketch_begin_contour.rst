.. title: begin_contour()
.. slug: sketch_begin_contour
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_contour() documentation
.. type: text

Use the ``begin_contour()`` and ``end_contour()`` function to create negative shapes within shapes such as the center of the letter 'O'.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_contour_0.png
    :alt: example picture for begin_contour()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100)
    translate(50, 50)
    stroke(255, 0, 0)
    begin_shape()
    # exterior part of shape, clockwise winding
    vertex(-40, -40)
    vertex(40, -40)
    vertex(40, 40)
    vertex(-40, 40)
    # interior part of shape, counter-clockwise winding
    begin_contour()
    vertex(-20, -20)
    vertex(-20, 20)
    vertex(20, 20)
    vertex(20, -20)
    end_contour()
    end_shape(CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Use the ``begin_contour()`` and ``end_contour()`` function to create negative shapes within shapes such as the center of the letter 'O'. ``begin_contour()`` begins recording vertices for the shape and ``end_contour()`` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These functions can only be used within a ``begin_shape()``/``end_shape()`` pair and transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not work within a ``begin_contour()``/``end_contour()`` pair. It is also not possible to use other shapes, such as ``ellipse()`` or ``rect()`` within.

Underlying Java method: `beginContour <https://processing.org/reference/beginContour_.html>`_

Syntax
======

.. code:: python

    begin_contour() -> None

Updated on November 04, 2020 20:45:44pm UTC

