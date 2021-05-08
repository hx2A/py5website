.. title: Py5Graphics.set_np_pixels()
.. slug: py5graphics_set_np_pixels
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.set_np_pixels() documentation
.. type: text

Set the entire contents of :doc:`py5graphics_np_pixels` to the contents of another properly sized and typed numpy array.

Description
===========

Set the entire contents of :doc:`py5graphics_np_pixels` to the contents of another properly sized and typed numpy array. The size of ``array``'s first and second dimensions must match the height and width of the Py5Graphics drawing surface, respectively. The array's ``dtype`` must be ``np.uint8``.

The ``bands`` parameter is used to interpret the ``array``'s color channel dimension (the array's third dimension). It can be one of ``'L'`` (single-channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha channel, ``array`` is assumed to have no transparency. Unlike the main drawing window, a Py5Graphics drawing surface's pixels can be transparent so using the alpha channel will work properly. If the ``bands`` parameter is ``'L'``, ``array``'s third dimension is optional.

This method makes calls to :doc:`py5graphics_load_np_pixels` and :doc:`py5graphics_update_np_pixels` so there is no need to call either explicitly.

This method is the same as :doc:`set_np_pixels` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`set_np_pixels`.

Syntax
======

.. code:: python

    set_np_pixels(array: np.ndarray, bands: str = 'ARGB') -> None

Parameters
==========

* **array**: `np.ndarray` - properly sized numpy array to be copied to np_pixels[]
* **bands**: `str = 'ARGB'` - color channels in the array's third dimension


Updated on May 07, 2021 21:23:50pm UTC

