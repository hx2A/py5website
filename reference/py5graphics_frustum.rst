.. title: Py5Graphics.frustum()
.. slug: py5graphics_frustum
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.frustum() documentation
.. type: text

Sets a perspective matrix as defined by the parameters.

Description
===========

Sets a perspective matrix as defined by the parameters.

A frustum is a geometric form: a pyramid with its top cut off.  With the viewer's eye at the imaginary top of the pyramid, the six planes of the frustum act as clipping planes when rendering a 3D view.  Thus, any form inside the clipping planes is rendered and visible; anything outside those planes is not visible.

Setting the frustum has the effect of changing the *perspective* with which the scene is rendered.  This can be achieved more simply in many cases by using :doc:`py5graphics_perspective`.

Note that the near value must be greater than zero (as the point of the frustum "pyramid" cannot converge "behind" the viewer).  Similarly, the far value must be greater than the near value (as the "far" plane of the frustum must be "farther away" from the viewer than the near plane).

Works like glFrustum, except it wipes out the current perspective matrix rather than multiplying itself with it.

This method is the same as :doc:`frustum` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`frustum`.

Underlying Java method: PGraphics.frustum

Syntax
======

.. code:: python

    frustum(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

Parameters
==========

* **bottom**: `float` - bottom coordinate of the clipping plane
* **far**: `float` - far component of the clipping plane; must be greater than the near value
* **left**: `float` - left coordinate of the clipping plane
* **near**: `float` - near component of the clipping plane; must be greater than zero
* **right**: `float` - right coordinate of the clipping plane
* **top**: `float` - top coordinate of the clipping plane


Updated on May 04, 2021 20:06:05pm UTC

