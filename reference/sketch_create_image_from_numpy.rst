.. title: create_image_from_numpy()
.. slug: create_image_from_numpy
.. date: 2021-04-12 18:01:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_image_from_numpy() documentation
.. type: text

Convert a numpy array into a Py5Image object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_create_image_from_numpy_0.png
    :alt: example picture for create_image_from_numpy()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        r = np.linspace(0, 255, num=py5.width).reshape(1, -1)
        g = np.linspace(0, 255, num=py5.height).reshape(-1, 1)
        b = 255
        rgb = np.dstack(np.broadcast_arrays(r, g, b)).astype(np.uint8)
        img = py5.create_image_from_numpy(rgb, 'RGB')
        py5.image(img, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Convert a numpy array into a Py5Image object. The numpy array must have 3 dimensions and the array's ``dtype`` must be ``np.uint8``. The size of ``array``'s first and second dimensions will be the image's height and width, respectively. The third dimension is for the array's color channels.

The ``bands`` parameter is used to interpret the ``array``'s color channel dimension (the array's third dimension). It can be one of ``'L'`` (single-channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha channel, ``array`` is assumed to have no transparency. If the ``bands`` parameter is ``'L'``, ``array``'s third dimension is optional.

The caller can optionally pass an existing Py5Image object to put the image data into using the ``dst`` parameter. This can have performance benefits in code that would otherwise continuously create new Py5Image objects. The array's width and height must match that of the recycled Py5Image object.

Syntax
======

.. code:: python

    create_image_from_numpy(array: np.array, bands: str = 'ARGB', *, dst: Py5Image = None) -> Py5Image

Parameters
==========

* **array**: `np.array` - numpy image array
* **bands**: `str = 'ARGB'` - color channels in array
* **dst**: `Py5Image = None` - existing Py5Image object to put the image data into


Updated on April 12, 2021 18:01:27pm UTC

