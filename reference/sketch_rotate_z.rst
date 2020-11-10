.. title: rotate_z()
.. slug: rotate_z
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 rotate_z() documentation
.. type: text

Rotates around the z-axis the amount specified by the ``angle`` parameter.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rotate_z_0.png
    :alt: example picture for rotate_z()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    translate(width//2, height//2)
    rotate_z(PI/3.0)
    rect(-26, -26, 52, 52)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rotate_z_1.png
    :alt: example picture for rotate_z()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    translate(width//2, height//2)
    rotate_z(radians(60))
    rect(-26, -26, 52, 52)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Rotates around the z-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to TWO_PI) or converted from degrees to radians with the ``radians()`` function. Coordinates are always rotated around their relative position to the origin. Positive numbers rotate in a clockwise direction and negative numbers rotate in a counterclockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``rotate_z(PI/2)`` and then ``rotate_z(PI/2)`` is the same as ``rotate_z(PI)``. If ``rotate_z()`` is run within the ``draw()``, the transformation is reset when the loop begins again. This function requires using P3D as a third parameter to ``size()`` as shown in the example above.

Underlying Java method: `rotateZ <https://processing.org/reference/rotateZ_.html>`_

Syntax
======

.. code:: python

    rotate_z(angle: float) -> None

Parameters
==========

* **angle**: `float` - angle of rotation specified in radians


Updated on November 10, 2020 15:41:45pm UTC

