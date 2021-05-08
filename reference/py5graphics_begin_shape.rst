.. title: Py5Graphics.begin_shape()
.. slug: py5graphics_begin_shape
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.begin_shape() documentation
.. type: text

Using the ``begin_shape()`` and :doc:`py5graphics_end_shape` functions allow creating more complex forms.

Description
===========

Using the ``begin_shape()`` and :doc:`py5graphics_end_shape` functions allow creating more complex forms. ``begin_shape()`` begins recording vertices for a shape and :doc:`py5graphics_end_shape` stops recording. The value of the ``kind`` parameter tells it which types of shapes to create from the provided vertices. With no mode specified, the shape can be any irregular polygon. The parameters available for ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``, ``TRIANGLE_FAN``, ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After calling the ``begin_shape()`` function, a series of :doc:`py5graphics_vertex` commands must follow. To stop drawing the shape, call :doc:`py5graphics_end_shape`. The :doc:`py5graphics_vertex` function with two parameters specifies a position in 2D and the :doc:`py5graphics_vertex` function with three parameters specifies a position in 3D. Each shape will be outlined with the current stroke color and filled with the fill color. 

Transformations such as :doc:`py5graphics_translate`, :doc:`py5graphics_rotate`, and :doc:`py5graphics_scale` do not work within ``begin_shape()``. It is also not possible to use other shapes, such as :doc:`py5graphics_ellipse` or :doc:`py5graphics_rect` within ``begin_shape()``. 

The ``P2D`` and ``P3D`` renderers allow :doc:`py5graphics_stroke` and :doc:`py5graphics_fill` to be altered on a per-vertex basis, but the default renderer does not. Settings such as :doc:`py5graphics_stroke_weight`, :doc:`py5graphics_stroke_cap`, and :doc:`py5graphics_stroke_join` cannot be changed while inside a ``begin_shape()`` & :doc:`py5graphics_end_shape` block with any renderer.

This method is the same as :doc:`begin_shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`begin_shape`.

Underlying Java method: PGraphics.beginShape

Syntax
======

.. code:: python

    begin_shape() -> None
    begin_shape(kind: int, /) -> None

Parameters
==========

* **kind**: `int` - Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP


Updated on May 04, 2021 20:06:05pm UTC

