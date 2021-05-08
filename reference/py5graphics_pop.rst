.. title: Py5Graphics.pop()
.. slug: py5graphics_pop
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.pop() documentation
.. type: text

The ``pop()`` function restores the previous drawing style settings and transformations after :doc:`py5graphics_push` has changed them.

Description
===========

The ``pop()`` function restores the previous drawing style settings and transformations after :doc:`py5graphics_push` has changed them. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with :doc:`py5graphics_push`, it builds on the current style and transform information.

:doc:`py5graphics_push` stores information related to the current transformation state and style settings controlled by the following functions: :doc:`py5graphics_rotate`, :doc:`py5graphics_translate`, :doc:`py5graphics_scale`, :doc:`py5graphics_fill`, :doc:`py5graphics_stroke`, :doc:`py5graphics_tint`, :doc:`py5graphics_stroke_weight`, :doc:`py5graphics_stroke_cap`, :doc:`py5graphics_stroke_join`, :doc:`py5graphics_image_mode`, :doc:`py5graphics_rect_mode`, :doc:`py5graphics_ellipse_mode`, :doc:`py5graphics_color_mode`, :doc:`py5graphics_text_align`, :doc:`py5graphics_text_font`, :doc:`py5graphics_text_mode`, :doc:`py5graphics_text_size`, and :doc:`py5graphics_text_leading`.

The :doc:`py5graphics_push` and ``pop()`` functions can be used in place of :doc:`py5graphics_push_matrix`, :doc:`py5graphics_pop_matrix`, ``push_styles()``, and ``pop_styles()``. The difference is that :doc:`py5graphics_push` and ``pop()`` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

This method is the same as :doc:`pop` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`pop`.

Underlying Java method: PGraphics.pop

Syntax
======

.. code:: python

    pop() -> None

Updated on May 04, 2021 20:06:05pm UTC

