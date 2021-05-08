.. title: Py5Graphics.load_shape()
.. slug: py5graphics_load_shape
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.load_shape() documentation
.. type: text

Loads geometry into a variable of type ``Py5Shape``.

Description
===========

Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be loaded. To load correctly, the file must be located in the data directory of the current Sketch. In most cases, ``load_shape()`` should be used inside ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a Sketch.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the ``None`` value may cause errors if your code does not check whether the value returned is ``None``.

This method is the same as :doc:`load_shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`load_shape`.

Underlying Java method: PGraphics.loadShape

Syntax
======

.. code:: python

    load_shape(filename: str, /) -> Py5Shape
    load_shape(filename: str, options: str, /) -> Py5Shape

Parameters
==========

* **filename**: `str` - name of file to load, can be .svg or .obj
* **options**: `str` - unused parameter


Updated on May 04, 2021 20:06:05pm UTC

