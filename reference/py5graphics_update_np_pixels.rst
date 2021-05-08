.. title: Py5Graphics.update_np_pixels()
.. slug: py5graphics_update_np_pixels
.. date: 2021-05-08 14:00:38 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.update_np_pixels() documentation
.. type: text

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_np_pixels` array.

Description
===========

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_np_pixels` array. Use in conjunction with :doc:`py5graphics_load_np_pixels`. If you're only reading pixels from the array, there's no need to call ``update_np_pixels()`` — updating is only necessary to apply changes.

The ``update_np_pixels()`` method is similar to :doc:`py5graphics_update_pixels` in that ``update_np_pixels()`` must be called after modifying :doc:`py5graphics_np_pixels` just as :doc:`py5graphics_update_pixels` must be called after modifying :doc:`py5graphics_pixels`.

This method is the same as :doc:`update_np_pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`update_np_pixels`.

Syntax
======

.. code:: python

    update_np_pixels() -> None

Updated on May 08, 2021 14:00:38pm UTC

