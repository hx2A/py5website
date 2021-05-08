.. title: Py5Graphics.push()
.. slug: py5graphics_push
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.push() documentation
.. type: text

The ``push()`` function saves the current drawing style settings and transformations, while :doc:`py5graphics_pop` restores these settings.

Description
===========

The ``push()`` function saves the current drawing style settings and transformations, while :doc:`py5graphics_pop` restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with ``push()``, it builds on the current style and transform information.

``push()`` stores information related to the current transformation state and style settings controlled by the following functions: :doc:`py5graphics_rotate`, :doc:`py5graphics_translate`, :doc:`py5graphics_scale`, :doc:`py5graphics_fill`, :doc:`py5graphics_stroke`, :doc:`py5graphics_tint`, :doc:`py5graphics_stroke_weight`, :doc:`py5graphics_stroke_cap`, :doc:`py5graphics_stroke_join`, :doc:`py5graphics_image_mode`, :doc:`py5graphics_rect_mode`, :doc:`py5graphics_ellipse_mode`, :doc:`py5graphics_color_mode`, :doc:`py5graphics_text_align`, :doc:`py5graphics_text_font`, :doc:`py5graphics_text_mode`, :doc:`py5graphics_text_size`, :doc:`py5graphics_text_leading`.

The ``push()`` and :doc:`py5graphics_pop` functions can be used in place of :doc:`py5graphics_push_matrix`, :doc:`py5graphics_pop_matrix`, ``push_styles()``, and ``pop_styles()``. The difference is that ``push()`` and :doc:`py5graphics_pop` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

This method is the same as :doc:`push` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`push`.

Underlying Java method: PGraphics.push

Syntax
======

.. code:: python

    push() -> None

Updated on May 04, 2021 20:06:05pm UTC

