.. title: pixels[]
.. slug: sketch_pixels
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pixels[] documentation
.. type: text

The ``pixels[]`` array contains the values for all the pixels in the display window.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pixels_0.png
    :alt: example picture for pixels[]

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    pink = color(255, 102, 204)
    load_pixels()
    for i in range(0, (width*height//2)-width//2):
        pixels[i] = pink

    update_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``pixels[]`` array contains the values for all the pixels in the display window. These values are of the color datatype. This array is defined by the size of the display window. For example, if the window is 100 x 100 pixels, there will be 10,000 values and if the window is 200 x 300 pixels, there will be 60,000 values. When the pixel density is set to higher than 1 with the ``pixel_density()`` function, these values will change. See the reference for ``pixel_width`` or ``pixel_height`` for more information. 

Before accessing this array, the data must loaded with the ``load_pixels()`` function. Failure to do so may result in a NullPointerException. Subsequent changes to the display window will not be reflected in ``pixels`` until ``load_pixels()`` is called again. After ``pixels`` has been modified, the ``update_pixels()`` function must be run to update the content of the display window.


Updated on November 03, 2020 22:19:57pm UTC

