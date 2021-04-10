.. title: load_image()
.. slug: load_image
.. date: 2021-04-10 15:07:49 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_image() documentation
.. type: text

Load an image into a variable of type ``Py5Image``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_image_0.png
    :alt: example picture for load_image()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.background(0)
        img = py5.load_image('apples.jpg')
        py5.image(img, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Load an image into a variable of type ``Py5Image``. Four types of images (GIF, JPG, TGA, PNG) can be loaded. To load images in other formats, consider using :doc:`convert_image`.

The ``image_path`` parameter can be a file or a URL. When loading a file, the path can be in the data directory, relative to the current working directory (:doc:`sketch_path`), or an absolute path. When loading from a URL, the ``image_path`` parameter must start with ``http://`` or ``https://``. If the image cannot be loaded, a Python ``RuntimeError`` will be thrown.

In most cases, load all images in ``setup()`` to preload them at the start of the program. Loading images inside ``draw()`` will reduce the speed of a program. In those situations, consider using :doc:`request_image` instead.

The ``dst`` parameter allows users to store the loaded image into an existing Py5Image object instead of creating a new object. The size of the existing Py5Image object must match the size of the loaded image. Most users will not find the ``dst`` parameter helpful. This feature is needed internally for performance reasons.

Syntax
======

.. code:: python

    load_image(image_path: Union[str, Path], dst: Py5Image = None) -> Py5Image

Parameters
==========

* **dst**: `Py5Image = None` - missing variable description
* **image_path**: `Union[str, Path]` - url or file path for image file


Updated on April 10, 2021 15:07:49pm UTC

