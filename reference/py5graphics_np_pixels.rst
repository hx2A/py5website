.. title: Py5Graphics.np_pixels[]
.. slug: py5graphics_np_pixels
.. date: 2021-05-08 14:06:36 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.np_pixels[] documentation
.. type: text

The ``np_pixels[]`` array contains the values for all the pixels in the Py5Graphics drawing surface.

Description
===========

The ``np_pixels[]`` array contains the values for all the pixels in the Py5Graphics drawing surface. Unlike the one dimensional array :doc:`py5graphics_pixels`, the ``np_pixels[]`` array organizes the color data in a 3 dimensional numpy array. The size of the array's dimensions are defined by the size of the Py5Graphics drawing surface. The first dimension is the height, the second is the width, and the third represents the color channels. The color channels are ordered alpha, red, green, blue (ARGB). Every value in ``np_pixels[]`` is an integer between 0 and 255.

This numpy array is very similar to the image arrays used by other popular Python image libraries, but note that some of them like opencv will by default order the color channels as RGBA.

When the pixel density is set to higher than 1 with the :doc:`py5graphics_pixel_density` function, the size of ``np_pixels[]``'s height and width dimensions will change. See the reference for :doc:`py5graphics_pixel_width` or :doc:`py5graphics_pixel_height` for more information. Nothing about ``np_pixels[]`` will change as a result of calls to :doc:`py5graphics_color_mode`. 

Much like the :doc:`py5graphics_pixels` array, there are load and update methods that must be called before and after making changes to the data in ``np_pixels[]``. Before accessing ``np_pixels[]``, the data must be loaded with the :doc:`py5graphics_load_np_pixels` method. If this is not done, ``np_pixels`` will be equal to ``None`` and your code will likely result in Python exceptions. After ``np_pixels[]`` has been modified, the :doc:`py5graphics_update_np_pixels` method must be called to update the content of the Py5Graphics drawing surface.

To set the entire contents of ``np_pixels[]`` to the contents of another properly sized numpy array, consider using :doc:`py5graphics_set_np_pixels`.

This field is the same as :doc:`np_pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`np_pixels`.


Updated on May 08, 2021 14:06:36pm UTC

