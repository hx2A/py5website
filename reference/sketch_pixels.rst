.. title: pixels[]
.. slug: pixels
.. date: 2021-08-20 15:31:10 UTC+00:00
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

    def setup():
        pink = "#F6C"
        py5.load_pixels()
        for i in range(0, (py5.width*py5.height//2) - py5.width//2):
            py5.pixels[i] = pink
    
        py5.update_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``pixels[]`` array contains the values for all the pixels in the display window. These values are of the color datatype. This array is defined by the size of the display window. For example, if the window is 100 x 100 pixels, there will be 10,000 values and if the window is 200 x 300 pixels, there will be 60,000 values. When the pixel density is set to higher than 1 with the :doc:`pixel_density` function, these values will change. See the reference for :doc:`pixel_width` or :doc:`pixel_height` for more information. 

Before accessing this array, the data must loaded with the :doc:`load_pixels` function. Failure to do so may result in a Java ``NullPointerException``. Subsequent changes to the display window will not be reflected in ``pixels`` until :doc:`load_pixels` is called again. After ``pixels`` has been modified, the :doc:`update_pixels` function must be run to update the content of the display window.

Underlying Java field: `pixels <https://processing.org/reference/pixels.html>`_


Updated on August 20, 2021 15:31:10pm UTC

