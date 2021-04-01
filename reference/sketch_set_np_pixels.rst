.. title: set_np_pixels()
.. slug: set_np_pixels
.. date: 2021-04-01 18:50:16 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_np_pixels() documentation
.. type: text

Set the entire contents of :doc:`np_pixels` to the contents of another properly sized and typed numpy array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_set_np_pixels_0.png
    :alt: example picture for set_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        array = np.zeros((py5.height, py5.width, 3), dtype=np.uint8)
        array[:60, :, 0] = 200
        array[:, :40, 1] = 100
        array[20:, :, 2] = 250
        py5.set_np_pixels(array, bands='RGB')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set the entire contents of :doc:`np_pixels` to the contents of another properly sized and typed numpy array. The size of ``array``'s first and second dimensions must match the height and width of the Sketch window, respectively. The array's ``dtype`` must be ``np.uint8``.

The ``bands`` parameter is used to interpret the ``array``'s color channel dimension (the array's third dimension). It can be one of ``'L'`` (single-channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha channel, ``array`` is assumed to have no transparency, but recall that the display window's pixels can never be transparent so any transparency in ``array`` will have no effect. If the ``bands`` parameter is ``'L'``, ``array``'s third dimension is optional.

This method makes calls to :doc:`load_np_pixels` and :doc:`update_np_pixels` so there is no need to call either explicitly.

Syntax
======

.. code:: python

    set_np_pixels(array: np.ndarray, bands: str = 'ARGB') -> None

Parameters
==========

* **array**: `np.ndarray` - properly sized numpy array to be copied to np_pixels[]
* **bands**: `str = 'ARGB'` - color channels in the array's third dimension


Updated on April 01, 2021 18:50:16pm UTC

