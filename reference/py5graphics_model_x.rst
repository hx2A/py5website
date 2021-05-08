.. title: Py5Graphics.model_x()
.. slug: py5graphics_model_x
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.model_x() documentation
.. type: text

Returns the three-dimensional X, Y, Z position in model space.

Description
===========

Returns the three-dimensional X, Y, Z position in model space. This returns the X value for a given coordinate based on the current set of transformations (scale, rotate, translate, etc.) The X value can be used to place an object in space relative to the location of the original point once the transformations are no longer in use. 

To see an example for how this can be used, see :doc:`model_x`. In that example, the ``model_x()``, :doc:`model_y`, and :doc:`model_z` methods (which are analogous to the ``model_x()``, :doc:`py5graphics_model_y`, and :doc:`py5graphics_model_z` methods) record the location of a box in space after being placed using a series of translate and rotate commands. After :doc:`pop_matrix` is called, those transformations no longer apply, but the (x, y, z) coordinate returned by the model functions is used to place another box in the same location.

This method is the same as :doc:`model_x` but linked to a ``Py5Graphics`` object.

Underlying Java method: PGraphics.modelX

Syntax
======

.. code:: python

    model_x(x: float, y: float, z: float, /) -> float

Parameters
==========

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on May 06, 2021 16:39:27pm UTC

