.. title: Py5Graphics.save()
.. slug: py5graphics_save
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.save() documentation
.. type: text

Save image data to a file.

Description
===========

Save image data to a file. This method uses the Python library Pillow to write the image, so it can save images in any format that that library supports.

Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This defaults to ``True``. Some image formats such as JPG do not support alpha channels, and Pillow will throw an error if you try to save an image with the alpha channel in that format.

The ``use_thread`` parameter will save the image in a separate Python thread. This improves performance by returning before the image has actually been written to the file.

This method is the same as :doc:`save` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`save`.

Syntax
======

.. code:: python

    save(filename: Union[str, Path], *, format: str = None, drop_alpha: bool = True, use_thread: bool = True, **params) -> None

Parameters
==========

* **drop_alpha**: `bool = True` - remove the alpha channel when saving the image
* **filename**: `Union[str, Path]` - output filename
* **format**: `str = None` - image format, if not determined from filename extension
* **params**: - keyword arguments to pass to the PIL.Image save method
* **use_thread**: `bool = True` - write file in separate thread


Updated on May 04, 2021 20:06:05pm UTC

