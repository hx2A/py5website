.. title: Py5Graphics.pixel_density
.. slug: py5graphics_pixel_density
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.pixel_density documentation
.. type: text

Get the pixel density of the Py5Graphics drawing surface.

Description
===========

Get the pixel density of the Py5Graphics drawing surface. By default this is 1 but it can be changed by calling :doc:`pixel_density` in ``settings()``.

When the pixel density has been set to more than 1, it changes all of the pixel operations including the way :doc:`py5graphics_get`, :doc:`py5graphics_blend`, :doc:`py5graphics_copy`, :doc:`py5graphics_update_pixels`, and :doc:`py5graphics_update_np_pixels` all work. See the reference for :doc:`py5graphics_pixel_width` and :doc:`py5graphics_pixel_height` for more information.

Underlying Java field: PGraphics.pixelDensity


Updated on May 06, 2021 16:39:27pm UTC

