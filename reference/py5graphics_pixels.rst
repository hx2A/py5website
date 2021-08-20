.. title: Py5Graphics.pixels[]
.. slug: py5graphics_pixels
.. date: 2021-08-20 15:31:10 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.pixels[] documentation
.. type: text

The ``pixels[]`` array contains the values for all the pixels in the Py5Graphics drawing surface.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_pixels_0.png
    :alt: example picture for pixels[]

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        g = py5.create_graphics(60, 60)
        g.begin_draw()
        g.background(255, 0, 0)
        g.rect(10, 10, 40, 40)
        g.load_pixels()
        yellow = "#FF0"
        for i in range(len(g.pixels) // 2):
            g.pixels[i] = yellow
        g.update_pixels()
        g.end_draw()

        py5.background(240)
        py5.image(g, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``pixels[]`` array contains the values for all the pixels in the Py5Graphics drawing surface. These values are of the color datatype. This array is defined by the size of the Py5Graphics drawing surface. For example, if the drawing surface is 100 x 100 pixels, there will be 10,000 values and if the drawing surface is 200 x 300 pixels, there will be 60,000 values. When the pixel density is set to higher than 1 with the :doc:`py5graphics_pixel_density` function, these values will change. See the reference for :doc:`py5graphics_pixel_width` or :doc:`py5graphics_pixel_height` for more information. 

Before accessing this array, the data must loaded with the :doc:`py5graphics_load_pixels` function. Failure to do so may result in a Java ``NullPointerException``. Subsequent changes to the Py5Graphics drawing surface will not be reflected in ``pixels`` until :doc:`py5graphics_load_pixels` is called again. After ``pixels`` has been modified, the :doc:`py5graphics_update_pixels` function must be run to update the content of the Py5Graphics drawing surface.

This field is the same as :doc:`pixels` but linked to a ``Py5Graphics`` object.

Underlying Java field: PGraphics.pixels


Updated on August 20, 2021 15:31:10pm UTC

