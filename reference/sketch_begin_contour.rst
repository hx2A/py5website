.. title: begin_contour()
.. slug: begin_contour
.. date: 2021-04-25 23:58:30 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_contour() documentation
.. type: text

Use the ``begin_contour()`` and :doc:`end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'.

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

    def setup():
        py5.translate(50, 50)
        py5.stroke(255, 0, 0)
        py5.begin_shape()
        # exterior part of shape, clockwise winding
        py5.vertex(-40, -40)
        py5.vertex(40, -40)
        py5.vertex(40, 40)
        py5.vertex(-40, 40)
        # interior part of shape, counter-clockwise winding
        py5.begin_contour()
        py5.vertex(-20, -20)
        py5.vertex(-20, 20)
        py5.vertex(20, 20)
        py5.vertex(20, -20)
        py5.end_contour()
        py5.end_shape(py5.CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Use the ``begin_contour()`` and :doc:`end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'. The ``begin_contour()`` method begins recording vertices for the shape and :doc:`end_contour` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a :doc:`begin_shape` & :doc:`end_shape` pair and transformations such as :doc:`translate`, :doc:`rotate`, and :doc:`scale` do not work within a ``begin_contour()`` & :doc:`end_contour` pair. It is also not possible to use other shapes, such as :doc:`ellipse` or :doc:`rect` within.

Underlying Java method: `beginContour <https://processing.org/reference/beginContour_.html>`_

Syntax
======

.. code:: python

    begin_contour() -> None

Updated on April 25, 2021 23:58:30pm UTC

