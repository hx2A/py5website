.. title: Py5Graphics.begin_camera()
.. slug: py5graphics_begin_camera
.. date: 2021-05-05 16:59:55 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.begin_camera() documentation
.. type: text

The ``begin_camera()`` and :doc:`py5graphics_end_camera` functions enable advanced customization of the camera space.

Description
===========

The ``begin_camera()`` and :doc:`py5graphics_end_camera` functions enable advanced customization of the camera space. The functions are useful if you want to more control over camera movement, however for most users, the :doc:`py5graphics_camera` function will be sufficient. The camera functions will replace any transformations (such as :doc:`py5graphics_rotate` or :doc:`py5graphics_translate`) that occur before them, but they will not automatically replace the camera transform itself. For this reason, camera functions should be placed right after the call to :doc:`py5graphics_begin_draw` (so that transformations happen afterwards), and the :doc:`py5graphics_camera` function can be used after ``begin_camera()`` if you want to reset the camera before applying transformations.

This function sets the matrix mode to the camera matrix so calls such as :doc:`py5graphics_translate`, :doc:`py5graphics_rotate`, :doc:`py5graphics_apply_matrix` and :doc:`py5graphics_reset_matrix` affect the camera. ``begin_camera()`` should always be used with a following :doc:`py5graphics_end_camera` and pairs of ``begin_camera()`` and :doc:`py5graphics_end_camera` cannot be nested.

This method is the same as :doc:`begin_camera` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`begin_camera`.

Underlying Java method: PGraphics.beginCamera

Syntax
======

.. code:: python

    begin_camera() -> None

Updated on May 05, 2021 16:59:55pm UTC

