.. title: Py5Graphics.shear_x()
.. slug: py5graphics_shear_x
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.shear_x() documentation
.. type: text

Shears a shape around the x-axis the amount specified by the ``angle`` parameter.

Description
===========

Shears a shape around the x-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from ``0`` to ``TWO_PI``) or converted to radians with the :doc:`radians` function. Objects are always sheared around their relative position to the origin and positive numbers shear objects in a clockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``shear_x(PI/2)`` and then ``shear_x(PI/2)`` is the same as ``shear_x(PI)``.
 
Technically, ``shear_x()`` multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the :doc:`py5graphics_push_matrix` and :doc:`py5graphics_pop_matrix` functions.

This method is the same as :doc:`shear_x` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`shear_x`.

Underlying Java method: PGraphics.shearX

Syntax
======

.. code:: python

    shear_x(angle: float, /) -> None

Parameters
==========

* **angle**: `float` - angle of shear specified in radians


Updated on May 07, 2021 21:23:50pm UTC

