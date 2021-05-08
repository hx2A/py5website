.. title: Py5Graphics.pixels[]
.. slug: py5graphics_pixels
.. date: 2021-05-08 14:06:36 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.pixels[] documentation
.. type: text

The ``pixels[]`` array contains the values for all the pixels in the Py5Graphics drawing surface.

Description
===========

The ``pixels[]`` array contains the values for all the pixels in the Py5Graphics drawing surface. These values are of the color datatype. This array is defined by the size of the Py5Graphics drawing surface. For example, if the drawing surface is 100 x 100 pixels, there will be 10,000 values and if the drawing surface is 200 x 300 pixels, there will be 60,000 values. When the pixel density is set to higher than 1 with the :doc:`py5graphics_pixel_density` function, these values will change. See the reference for :doc:`py5graphics_pixel_width` or :doc:`py5graphics_pixel_height` for more information. 

Before accessing this array, the data must loaded with the :doc:`py5graphics_load_pixels` function. Failure to do so may result in a Java ``NullPointerException``. Subsequent changes to the Py5Graphics drawing surface will not be reflected in ``pixels`` until :doc:`py5graphics_load_pixels` is called again. After ``pixels`` has been modified, the :doc:`py5graphics_update_pixels` function must be run to update the content of the Py5Graphics drawing surface.

This field is the same as :doc:`pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`pixels`.

Underlying Java field: PGraphics.pixels


Updated on May 08, 2021 14:06:36pm UTC

