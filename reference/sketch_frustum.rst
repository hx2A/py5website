.. title: frustum()
.. slug: frustum
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 frustum() documentation
.. type: text

Sets a perspective matrix as defined by the parameters.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_frustum_0.png
    :alt: example picture for frustum()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_fill()
    background(204)
    frustum(-10, 0, 0, 10, 10, 200)
    rotate_y(PI/6)
    box(45)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets a perspective matrix as defined by the parameters.

A frustum is a geometric form: a pyramid with its top cut off.  With the viewer's eye at the imaginary top of the pyramid, the six planes of the frustum act as clipping planes when rendering a 3D view.  Thus, any form inside the clipping planes is rendered and visible; anything outside those planes is not visible.

Setting the frustum has the effect of changing the *perspective* with which the scene is rendered.  This can be achieved more simply in many cases by using ``perspective()``.

Note that the near value must be greater than zero (as the point of the frustum "pyramid" cannot converge "behind" the viewer).  Similarly, the far value must be greater than the near value (as the "far" plane of the frustum must be "farther away" from the viewer than the near plane).

Works like glFrustum, except it wipes out the current perspective matrix rather than multiplying itself with it.

Underlying Java method: `frustum <https://processing.org/reference/frustum_.html>`_

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


Updated on November 24, 2020 21:22:32pm UTC

