.. title: Py5Graphics.load_np_pixels()
.. slug: py5graphics_load_np_pixels
.. date: 2021-05-08 14:06:36 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.load_np_pixels() documentation
.. type: text

Loads the pixel data of the current Py5Graphics drawing surface into the :doc:`py5graphics_np_pixels` array.

Description
===========

Loads the pixel data of the current Py5Graphics drawing surface into the :doc:`py5graphics_np_pixels` array. This method must always be called before reading from or writing to :doc:`py5graphics_np_pixels`. Subsequent changes to the Py5Graphics drawing surface will not be reflected in :doc:`py5graphics_np_pixels` until ``load_np_pixels()`` is called again.

The ``load_np_pixels()`` method is similar to :doc:`py5graphics_load_pixels` in that ``load_np_pixels()`` must be called before reading from or writing to :doc:`py5graphics_np_pixels` just as :doc:`py5graphics_load_pixels` must be called before reading from or writing to :doc:`py5graphics_pixels`.

Note that ``load_np_pixels()`` will as a side effect call :doc:`py5graphics_load_pixels`, so if your code needs to read :doc:`py5graphics_np_pixels` and :doc:`py5graphics_pixels` simultaneously, there is no need for a separate call to :doc:`py5graphics_load_pixels`. However, be aware that modifying both :doc:`py5graphics_np_pixels` and :doc:`py5graphics_pixels` simultaneously will likely result in the updates to :doc:`py5graphics_pixels` being discarded.

This method is the same as :doc:`load_np_pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`load_np_pixels`.

Syntax
======

.. code:: python

    load_np_pixels() -> None

Updated on May 08, 2021 14:06:36pm UTC

