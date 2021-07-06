.. title: Py5Image.save()
.. slug: py5image_save
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Image.save() documentation
.. type: text

Save the Py5Image object to an image file.

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

    def setup():
        for _ in range(10):
            py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
        img = py5.get(10, 10, 80, 80)
        img.save('/tmp/cropped_random_squares.jpg')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Save the Py5Image object to an image file. This method uses the Python library Pillow to write the image, so it can save images in any format that that library supports.

Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This defaults to ``True``. Some image formats such as JPG do not support alpha channels, and Pillow will throw an error if you try to save an image with the alpha channel in that format.

The ``use_thread`` parameter will save the image in a separate Python thread. This improves performance by returning before the image has actually been written to the file.

Syntax
======

.. code:: python

    save(filename: Union[str, Path], *, format: str = None, drop_alpha: bool = True, use_thread: bool = False, **params) -> None

Parameters
==========

* **drop_alpha**: `bool = True` - remove the alpha channel when saving the image
* **filename**: `Union[str, Path]` - output filename
* **format**: `str = None` - image format, if not determined from filename extension
* **params**: - keyword arguments to pass to the PIL.Image save method
* **use_thread**: `bool = False` - write file in separate thread


Updated on July 06, 2021 22:46:12pm UTC

