.. title: Py5Graphics.scale()
.. slug: py5graphics_scale
.. date: 2021-05-07 21:23:50 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.scale() documentation
.. type: text

Increases or decreases the size of a shape by expanding and contracting vertices.

Description
===========

Increases or decreases the size of a shape by expanding and contracting vertices. Objects always scale from their relative origin to the coordinate system. Scale values are specified as decimal percentages. For example, the function call ``scale(2.0)`` increases the dimension of a shape by 200%.

Transformations apply to everything that happens after and subsequent calls to the function multiply the effect. For example, calling ``scale(2.0)`` and then ``scale(1.5)`` is the same as ``scale(3.0)``. Using this function with the ``z`` parameter requires using ``P3D`` as the renderer. This function can be further controlled with :doc:`py5graphics_push_matrix` and :doc:`py5graphics_pop_matrix`.

This method is the same as :doc:`scale` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`scale`.

Underlying Java method: PGraphics.scale

Syntax
======

.. code:: python

    scale(s: float, /) -> None
    scale(x: float, y: float, /) -> None
    scale(x: float, y: float, z: float, /) -> None

Parameters
==========

* **s**: `float` - percentage to scale the object
* **x**: `float` - percentage to scale the object in the x-axis
* **y**: `float` - percentage to scale the object in the y-axis
* **z**: `float` - percentage to scale the object in the z-axis


Updated on May 07, 2021 21:23:50pm UTC

