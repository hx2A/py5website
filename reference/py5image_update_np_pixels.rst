.. title: Py5Image.update_np_pixels()
.. slug: py5image_update_np_pixels
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Image.update_np_pixels() documentation
.. type: text

Updates the image with the data in the :doc:`py5image_np_pixels` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_update_np_pixels_0.png
    :alt: example picture for update_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        my_image = py5.load_image("apples.jpg")
        my_image.load_np_pixels()
        my_image.np_pixels[:50, :, :] = my_image.np_pixels[50:100, :, :]
        my_image.update_np_pixels()
        py5.image(my_image, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Updates the image with the data in the :doc:`py5image_np_pixels` array. Use in conjunction with :doc:`py5image_load_np_pixels`. If you're only reading pixels from the array, there's no need to call ``update_np_pixels()`` — updating is only necessary to apply changes.

The ``update_np_pixels()`` method is similar to :doc:`py5image_update_pixels` in that ``update_np_pixels()`` must be called after modifying :doc:`py5image_np_pixels` just as :doc:`py5image_update_pixels` must be called after modifying :doc:`py5image_pixels`.

Syntax
======

.. code:: python

    update_np_pixels() -> None

Updated on May 01, 2021 20:51:42pm UTC

