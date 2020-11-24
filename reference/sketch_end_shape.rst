.. title: end_shape()
.. slug: end_shape
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_shape() documentation
.. type: text

The ``end_shape()`` function is the companion to ``begin_shape()`` and may only be called after ``begin_shape()``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_end_shape_0.png
    :alt: example picture for end_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_fill()

    begin_shape()
    vertex(20, 20)
    vertex(45, 20)
    vertex(45, 80)
    end_shape(CLOSE)

    begin_shape()
    vertex(50, 20)
    vertex(75, 20)
    vertex(75, 80)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``end_shape()`` function is the companion to ``begin_shape()`` and may only be called after ``begin_shape()``. When ``end_shape()`` is called, all of image data defined since the previous call to ``begin_shape()`` is written into the image buffer. The constant CLOSE as the value for the MODE parameter to close the shape (to connect the beginning and the end).

Underlying Java method: `endShape <https://processing.org/reference/endShape_.html>`_

Syntax
======

.. code:: python

    end_shape() -> None
    end_shape(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - use CLOSE to close the shape


Updated on November 24, 2020 21:22:32pm UTC

