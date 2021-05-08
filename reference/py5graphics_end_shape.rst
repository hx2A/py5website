.. title: Py5Graphics.end_shape()
.. slug: py5graphics_end_shape
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.end_shape() documentation
.. type: text

The ``end_shape()`` function is the companion to :doc:`py5graphics_begin_shape` and may only be called after :doc:`py5graphics_begin_shape`.

Description
===========

The ``end_shape()`` function is the companion to :doc:`py5graphics_begin_shape` and may only be called after :doc:`py5graphics_begin_shape`. When ``end_shape()`` is called, all of image data defined since the previous call to :doc:`py5graphics_begin_shape` is written into the image buffer. The constant ``CLOSE`` as the value for the ``MODE`` parameter to close the shape (to connect the beginning and the end).

This method is the same as :doc:`end_shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`end_shape`.

Underlying Java method: PGraphics.endShape

Syntax
======

.. code:: python

    end_shape() -> None
    end_shape(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - use CLOSE to close the shape


Updated on May 04, 2021 20:06:05pm UTC

