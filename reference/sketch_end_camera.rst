.. title: end_camera()
.. slug: end_camera
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_camera() documentation
.. type: text

The :doc:`begin_camera` and ``end_camera()`` methods enable advanced customization of the camera space.

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

    def setup():
        py5.size(100, 100, py5.P3D)
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

The :doc:`begin_camera` and ``end_camera()`` methods enable advanced customization of the camera space. Please see the reference for :doc:`begin_camera` for a description of how the methods are used.

Underlying Java method: `endCamera <https://processing.org/reference/endCamera_.html>`_

Syntax
======

.. code:: python

    end_camera() -> None

Updated on June 28, 2021 15:16:14pm UTC

