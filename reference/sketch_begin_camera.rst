.. title: begin_camera()
.. slug: begin_camera
.. date: 2021-02-25 16:17:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_camera() documentation
.. type: text

The ``begin_camera()`` and ``end_camera()`` functions enable advanced customization of the camera space.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_camera_0.png
    :alt: example picture for begin_camera()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.no_fill()
    
        py5.begin_camera()
        py5.camera()
        py5.rotate_x(-py5.PI/6)
        py5.end_camera()
    
        py5.translate(50, 50, 0)
        py5.rotate_y(py5.PI/3)
        py5.box(45)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``begin_camera()`` and ``end_camera()`` functions enable advanced customization of the camera space. The functions are useful if you want to more control over camera movement, however for most users, the ``camera()`` function will be sufficient. The camera functions will replace any transformations (such as ``rotate()`` or ``translate()``) that occur before them in ``draw()``, but they will not automatically replace the camera transform itself. For this reason, camera functions should be placed at the beginning of ``draw()`` (so that transformations happen afterwards), and the ``camera()`` function can be used after ``begin_camera()`` if you want to reset the camera before applying transformations.

This function sets the matrix mode to the camera matrix so calls such as ``translate()``, ``rotate()``, ``apply_matrix()`` and ``reset_matrix()`` affect the camera. ``begin_camera()`` should always be used with a following ``end_camera()`` and pairs of ``begin_camera()`` and ``end_camera()`` cannot be nested.

Underlying Java method: `beginCamera <https://processing.org/reference/beginCamera_.html>`_

Syntax
======

.. code:: python

    begin_camera() -> None

Updated on February 25, 2021 16:17:14pm UTC

