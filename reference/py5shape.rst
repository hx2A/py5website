.. title: Py5Shape
.. slug: py5shape
.. date: 2021-03-05 15:24:25 UTC+00:00
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
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = py5.load_shape("bot.svg")


    def draw():
        py5.shape(s, 10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s  # the Py5Shape object
        # creating the Py5Shape as a square. the corner
        # is 0,0 so that the center is at 40,40
        s = py5.create_shape(py5.RECT, 0, 0, 80, 80)


    def draw():
        py5.shape(s, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Datatype for storing shapes. Before a shape is used, it must be loaded with the :doc:`load_shape` or created with the :doc:`create_shape`. The :doc:`shape` function is used to draw the shape to the display window. Py5 can currently load and display SVG (Scalable Vector Graphics) and OBJ shapes. OBJ files can only be opened using the ``P3D`` renderer. The :doc:`load_shape` function supports SVG files created with Inkscape and Adobe Illustrator. It is not a full SVG implementation, but offers some straightforward support for handling vector data. A more complete SVG implementation can be provided by :doc:`convert_image` if Cairo is installed. See installation instructions for additional detail.

The ``Py5Shape`` object contains a group of methods that can operate on the shape data.

To create a new shape, use the :doc:`create_shape` function. Do not use the syntax ``Py5Shape()``.

Underlying Java class: `PShape <https://processing.org/reference/PShape.html>`_

This class provides the following methods and fields:

.. include:: include/py5shape_include.rst

Updated on March 05, 2021 15:24:25pm UTC

