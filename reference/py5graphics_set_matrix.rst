.. title: Py5Graphics.set_matrix()
.. slug: py5graphics_set_matrix
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.set_matrix() documentation
.. type: text

Set the current matrix to the one specified through the parameter ``source``.

Description
===========

Set the current matrix to the one specified through the parameter ``source``. Inside the Processing code it will call :doc:`py5graphics_reset_matrix` followed by :doc:`py5graphics_apply_matrix`. This will be very slow because :doc:`py5graphics_apply_matrix` will try to calculate the inverse of the transform, so avoid it whenever possible.

This method is the same as :doc:`set_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`set_matrix`.

Underlying Java method: PGraphics.setMatrix

Syntax
======

.. code:: python

    set_matrix(source: NDArray[(2, 3), Float], /) -> None
    set_matrix(source: NDArray[(4, 4), Float], /) -> None

Parameters
==========

* **source**: `NDArray[(2, 3), Float]` - transformation matrix data
* **source**: `NDArray[(4, 4), Float]` - transformation matrix data


Updated on May 04, 2021 20:06:05pm UTC

