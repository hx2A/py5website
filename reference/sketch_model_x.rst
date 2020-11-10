.. title: model_x()
.. slug: model_x
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 model_x() documentation
.. type: text

Returns the three-dimensional X, Y, Z position in model space.

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
        size(500, 500, P3D)
        no_fill()


    def draw():
        background(0)

        push_matrix()
        # start at the middle of the screen
        translate(width//2, height//2, -200)
        # some random rotation to make things interesting
        rotate_y(1.0)  # yrot)
        rotate_z(2.0)  # zrot)
        # rotate in X a little more each frame
        rotate_x(frame_count / 100.0)
        # offset from_ center
        translate(0, 150, 0)

        # draw a white box outline at (0, 0, 0)
        stroke(255)
        box(50)

        # the box was drawn at (0, 0, 0), store that location
        x = model_x(0, 0, 0)
        y = model_y(0, 0, 0)
        z = model_z(0, 0, 0)
        # clear out all the transformations
        pop_matrix()

        # draw another box at the same (x, y, z) coordinate as the other
        push_matrix()
        translate(x, y, z)
        stroke(255, 0, 0)
        box(50)
        pop_matrix()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns the three-dimensional X, Y, Z position in model space. This returns the X value for a given coordinate based on the current set of transformations (scale, rotate, translate, etc.) The X value can be used to place an object in space relative to the location of the original point once the transformations are no longer in use. 
 
In the example, the ``model_x()``, ``model_y()``, and ``model_z()`` functions record the location of a box in space after being placed using a series of translate and rotate commands. After ``pop_matrix()`` is called, those transformations no longer apply, but the (x, y, z) coordinate returned by the model functions is used to place another box in the same location.

Underlying Java method: `modelX <https://processing.org/reference/modelX_.html>`_

Syntax
======

.. code:: python

    model_x(x: float, y: float, z: float) -> float

Parameters
==========

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on November 10, 2020 15:41:45pm UTC

