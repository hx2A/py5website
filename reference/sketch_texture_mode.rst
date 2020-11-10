.. title: texture_mode()
.. slug: texture_mode
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 texture_mode() documentation
.. type: text

Sets the coordinate space for texture mapping.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_texture_mode_0.png
    :alt: example picture for texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_stroke()
    img = load_image("laDefense.jpg")
    texture_mode(IMAGE)
    begin_shape()
    texture(img)
    vertex(10, 20, 0, 0)
    vertex(80, 5, 100, 0)
    vertex(95, 90, 100, 100)
    vertex(40, 95, 0, 100)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_texture_mode_1.png
    :alt: example picture for texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_stroke()
    img = load_image("laDefense.jpg")
    texture_mode(NORMAL)
    begin_shape()
    texture(img)
    vertex(10, 20, 0, 0)
    vertex(80, 5, 1, 0)
    vertex(95, 90, 1, 1)
    vertex(40, 95, 0, 1)
    end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the coordinate space for texture mapping. The default mode is ``IMAGE``, which refers to the actual coordinates of the image. ``NORMAL`` refers to a normalized space of values ranging from 0 to 1. This function only works with the P2D and P3D renderers.

With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the entire size of a quad would require the points (0,0) (100, 0) (100,200) (0,200). The same mapping in ``NORMAL`` is (0,0) (1,0) (1,1) (0,1).

Underlying Java method: `textureMode <https://processing.org/reference/textureMode_.html>`_

Syntax
======

.. code:: python

    texture_mode(mode: int) -> None

Parameters
==========

* **mode**: `int` - either IMAGE or NORMAL


Updated on November 10, 2020 15:41:45pm UTC

