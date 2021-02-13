.. title: convert_image()
.. slug: convert_image
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 convert_image() documentation
.. type: text

Convert non-py5 image objects into Py5Image objects.

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

    from PIL import Image


    def setup():
        pil_image = Image.open('py5_logo.jpg')
        py5_image = py5.convert_image(pil_image)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Convert non-py5 image objects into Py5Image objects. This facilitates py5 compatability with other commonly used Python libraries.

This method is comparable to :doc:`load_image`, except instead of reading image files from disk, it reads image data from other Python objects.

Passed image object types must be known to py5's builtin image conversion tools. New object types and functions to effect conversions can be registered with :doc:`register_image_conversion`.

The caller can optionally pass an existing Py5Image object to put the converted image into. This can have performance benefits in code that would otherwise continuously create new Py5Image objects. The converted image width and height must match that of the recycled Py5Image object.

Syntax
======

.. code:: python

    convert_image(obj: Any, dst: Py5Image = None) -> Py5Image

Parameters
==========

* **dst**: `Py5Image = None` - existing Py5Image object to put the converted image into
* **obj**: `Any` - object to convert into a Py5Image object


Updated on February 13, 2021 18:02:35pm UTC

