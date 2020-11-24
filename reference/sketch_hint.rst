.. title: hint()
.. slug: hint
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 hint() documentation
.. type: text

This function is used to enable or disable special features that control how graphics are drawn.

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
        size(200, 200, P3D)
        hint(DISABLE_DEPTH_TEST)


    def draw():
        background(204)
        push_matrix()
        translate(width//2, height//2)
        rotate_y(1)
        box(60)
        pop_matrix()
        line(10, 100, 190, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

This function is used to enable or disable special features that control how graphics are drawn. In the course of developing Processing, we had to make hard decisions about tradeoffs between performance and visual quality. We put significant effort into determining what makes most sense for the largest number of users, and then use functions like ``hint()`` to allow people to tune the settings for their particular sketch. Implementing a ``hint()`` is a last resort that's used when a more elegant solution cannot be found. Some options might graduate to standard features instead of hints over time, or be added and removed between (major) releases.


``hints used by the default renderer:``

``ENABLE_STROKE_PURE``
Fixes a problem with shapes that have a stroke and are rendered using small steps (for instance, using ``vertex()`` with points that are close to one another), or are drawn at small sizes.


``hints for use with P2D and P3D:``

``DISABLE_ASYNC_SAVEFRAME``
``save()`` and ``save_frame()`` will not use separate threads for saving and will block until the image is written to the drive. This was the default behavior in 3.0b7 and before. To enable, call hint(ENABLE_ASYNC_SAVEFRAME).

``DISABLE_OPENGL_ERRORS``
Speeds up the P3D renderer setting by not checking for errors while running.

``DISABLE_TEXTURE_MIPMAPS``
Disable generation of texture mipmaps in P2D or P3D. This results in lower quality - but faster - rendering of texture images when they appear smaller than their native resolutions (the mipmaps are scaled-down versions of a texture that make it look better when drawing it at a small size). However, the difference in performance is fairly minor on recent desktop video cards.


``hints for use with P3D only:``

``DISABLE_DEPTH_MASK``
Disables writing into the depth buffer. This means that a shape drawn with this hint can be hidden by another shape drawn later, irrespective of their distances to the camera. Note that this is different from disabling the depth test. The depth test is still applied, as long as the DISABLE_DEPTH_TEST hint is not called, but the depth values of the objects are not recorded. This is useful when drawing a semi-transparent 3D object without depth sorting, in order to avoid visual glitches due the faces of the object being at different distances from the camera, but still having the object properly occluded by the rest of the objects in the scene.

``ENABLE_DEPTH_SORT``
Enable primitive z-sorting of triangles and lines in P3D. This can slow performance considerably, and the algorithm is not yet perfect.

``DISABLE_DEPTH_TEST``
Disable the zbuffer, allowing you to draw on top of everything at will. When depth testing is disabled, items will be drawn to the screen sequentially, like a painting. This hint is most often used to draw in 3D, then draw in 2D on top of it (for instance, to draw GUI controls in 2D on top of a 3D interface). When called, this will also clear the depth buffer. Restore the default with ``hint(ENABLE_DEPTH_TEST)``, but note that with the depth buffer cleared, any 3D drawing that happens later in will ignore existing shapes on the screen.

``DISABLE_OPTIMIZED_STROKE``
Forces the P3D renderer to draw each shape (including its strokes) separately, instead of batching them into larger groups for better performance. One consequence of this is that 2D items drawn with P3D are correctly stacked on the screen, depending on the order in which they were drawn. Otherwise, glitches such as the stroke lines being drawn on top of the interior of all the shapes will occur. However, this hint can make rendering substantially slower, so it is recommended to use it only when drawing a small amount of shapes. For drawing two-dimensional scenes, use the P2D renderer instead, which doesn't need the hint to properly stack shapes and their strokes.

``ENABLE_STROKE_PERSPECTIVE``
Enables stroke geometry (lines and points) to be affected by the perspective, meaning that they will look smaller as they move away from the camera.

Underlying Java method: `hint <https://processing.org/reference/hint_.html>`_

Syntax
======

.. code:: python

    hint(which: int, /) -> None

Parameters
==========

* **which**: `int` - missing variable description


Updated on November 24, 2020 21:22:32pm UTC

