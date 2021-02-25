.. title: rotate_x()
.. slug: rotate_x
.. date: 2021-02-25 18:50:59 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 rotate_x() documentation
.. type: text

Rotates around the x-axis the amount specified by the ``angle`` parameter.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rotate_x_0.png
    :alt: example picture for rotate_x()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.translate(py5.width//2, py5.height//2)
        py5.rotate_x(py5.PI/3.0)
        py5.rect(-26, -26, 52, 52)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rotate_x_1.png
    :alt: example picture for rotate_x()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.translate(py5.width//2, py5.height//2)
        py5.rotate_x(py5.radians(60))
        py5.rect(-26, -26, 52, 52)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Rotates around the x-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to TWO_PI) or converted from degrees to radians with the ``radians()`` function. Coordinates are always rotated around their relative position to the origin. Positive numbers rotate in a clockwise direction and negative numbers rotate in a counterclockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``rotate_x(PI/2)`` and then ``rotate_x(PI/2)`` is the same as ``rotate_x(PI)``. If ``rotate_x()`` is run within the ``draw()``, the transformation is reset when the loop begins again. This function requires using P3D as a third parameter to ``size()`` as shown in the example.

Underlying Java method: `rotateX <https://processing.org/reference/rotateX_.html>`_

Syntax
======

.. code:: python

    rotate_x(angle: float, /) -> None

Parameters
==========

* **angle**: `float` - angle of rotation specified in radians


Updated on February 25, 2021 18:50:59pm UTC

