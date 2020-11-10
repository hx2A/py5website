.. title: Py5Shape
.. slug: py5shape
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape documentation
.. type: text

Datatype for storing shapes.

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
        global square  # the Py5Shape object
        size(100, 100)
        # creating the Py5Shape as a square. the corner
        # is 0,0 so that the center is at 40,40
        square = create_shape(RECT, 0, 0, 80, 80)


    def draw():
        shape(square, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Datatype for storing shapes. Before a shape is used, it must be loaded with the ``load_shape()`` or created with the ``create_shape()``. The ``shape()`` function is used to draw the shape to the display window. Processing can currently load and display SVG (Scalable Vector Graphics) and OBJ shapes. OBJ files can only be opened using the ``P3D`` renderer. The ``load_shape()`` function supports SVG files created with Inkscape and Adobe Illustrator. It is not a full SVG implementation, but offers some straightforward support for handling vector data.

The ``Py5Shape`` object contains a group of methods that can operate on the shape data. Some of the methods are listed below, but the full list used for creating and modifying shapes is available here in the Processing Javadoc.

To create a new shape, use the ``create_shape()`` function. Do not use the syntax ``new Py5Shape()``.

Underlying Java class: `PShape <https://processing.org/reference/PShape.html>`_

This class provides the following methods and fields:

.. include:: include/py5shape_include.rst

Updated on January 01, 1970 00:00:00am UTC

