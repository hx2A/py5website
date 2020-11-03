.. title: end_camera()
.. slug: sketch_end_camera
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_camera() documentation
.. type: text

The ``begin_camera()`` and ``end_camera()`` functions enable advanced customization of the camera space.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_end_camera_0.png
    :alt: example picture for end_camera()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_fill()

    begin_camera()
    camera()
    rotate_x(-PI/6)
    end_camera()

    translate(50, 50, 0)
    rotate_y(PI/3)
    box(45)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``begin_camera()`` and ``end_camera()`` functions enable advanced customization of the camera space. Please see the reference for ``begin_camera()`` for a description of how the functions are used.

Syntax
======

.. code:: python

    end_camera() -> None

Updated on November 03, 2020 22:19:57pm UTC

