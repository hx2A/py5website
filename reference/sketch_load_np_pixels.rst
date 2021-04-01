.. title: load_np_pixels()
.. slug: load_np_pixels
.. date: 2021-04-01 15:50:23 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_np_pixels() documentation
.. type: text

Loads the pixel data of the current display window into the :doc:`np_pixels` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_np_pixels_0.png
    :alt: example picture for load_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        my_image = py5.load_image("apples.jpg")
        py5.image(my_image, 0, 0)
    
        py5.load_np_pixels()
        py5.np_pixels[50:100, :, :] = py5.np_pixels[:50, :, :]
        py5.update_np_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Loads the pixel data of the current display window into the :doc:`np_pixels` array. This method must always be called before reading from or writing to :doc:`np_pixels`. Subsequent changes to the display window will not be reflected in :doc:`np_pixels` until ``load_np_pixels()`` is called again.

The ``load_np_pixels()`` method is similar to :doc:`load_pixels` in that ``load_np_pixels()`` must be called before reading from or writing to :doc:`np_pixels` just as :doc:`load_pixels` must be called before reading from or writing to :doc:`pixels`.

Note that ``load_np_pixels()`` will as a side effect call :doc:`load_pixels`, so if your code needs to read :doc:`np_pixels` and :doc:`pixels` simultaneously, there is no need for a separate call to :doc:`load_pixels`. However, be aware that modifying both :doc:`np_pixels` and :doc:`pixels` simultaneously will likely result in the updates to :doc:`pixels` being discarded.

Syntax
======

.. code:: python

    load_np_pixels() -> None

Updated on April 01, 2021 15:50:23pm UTC

