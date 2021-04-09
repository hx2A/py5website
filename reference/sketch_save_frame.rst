.. title: save_frame()
.. slug: save_frame
.. date: 2021-04-09 20:37:07 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 save_frame() documentation
.. type: text

Save the current frame as an image.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def draw():
        for _ in range(10):
            py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
        py5.save_frame('/tmp/random_squares_####.jpg')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Save the current frame as an image. This method uses the Python library Pillow to write the image, so it can save images in any format that that library supports.

Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This defaults to ``True``. Some image formats such as JPG do not support alpha channels, and Pillow will throw an error if you try to save an image with the alpha channel in that format.

The ``use_thread`` parameter will save the image in a separate Python thread. This improves performance by returning before the image has actually been written to the file.

This method is the same as :doc:`save` except it will replace a sequence of ``#`` symbols in the ``filename`` parameter with the frame number. This is useful when saving an image sequence for a running animation. The first frame number will be 1.

Syntax
======

.. code:: python

    save_frame(filename: Union[str, Path], format: str = None, drop_alpha: bool = True, use_thread: bool = True, params) -> None

Parameters
==========

* **drop_alpha**: `bool = True` - remove the alpha channel when saving the image
* **filename**: `Union[str, Path]` - output filename
* **format**: `str = None` - image format, if not determined from filename extension
* **params**: - keyword arguments to pass to the PIL.Image save method
* **use_thread**: `bool = True` - write file in separate thread


Updated on April 09, 2021 20:37:07pm UTC

