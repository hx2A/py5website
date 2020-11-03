.. title: load_shape()
.. slug: sketch_load_shape
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_shape() documentation
.. type: text

Loads geometry into a variable of type ``Py5Shape``.

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
        global s
        size(100, 100)
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = load_shape("bot.svg")


    def draw():
        shape(s, 10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        size(100, 100, P3D)
        # the file "bot.obj" must be in the data folder
        # of the current sketch to load successfully
        s = load_shape("bot.obj")


    def draw():
        background(204)
        translate(width//2, height//2)
        shape(s, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be loaded. To load correctly, the file must be located in the data directory of the current sketch. In most cases, ``load_shape()`` should be used inside ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a sketch.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the null value may cause a NullPointerException if your code does not check whether the value returned is null.

Syntax
======

.. code:: python

    load_shape(filename: str) -> Py5Shape
    load_shape(filename: str, options: str) -> Py5Shape

Parameters
==========

* **filename**: `str` - name of file to load, can be .svg or .obj
* **options**: `str` - missing variable description


Updated on November 03, 2020 22:19:57pm UTC

