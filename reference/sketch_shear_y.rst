.. title: shear_y()
.. slug: sketch_shear_y
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 shear_y() documentation
.. type: text

Shears a shape around the y-axis the amount specified by the ``angle`` parameter.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_shear_y_0.png
    :alt: example picture for shear_y()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100)
    translate(width/4, height/4)
    shear_y(PI/4.0)
    rect(0, 0, 30, 30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Shears a shape around the y-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to PI*2) or converted to radians with the ``radians()`` function. Objects are always sheared around their relative position to the origin and positive numbers shear objects in a clockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``shear_y(PI/2)`` and then ``shear_y(PI/2)`` is the same as ``shear_y(PI)``. If ``shear_y()`` is called within the ``draw()``, the transformation is reset when the loop begins again.
 
Technically, ``shear_y()`` multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the ``push_matrix()`` and ``pop_matrix()`` functions.

Underlying Java method: `shearY <https://processing.org/reference/shearY_.html>`_

Syntax
======

.. code:: python

    shear_y(angle: float) -> None

Parameters
==========

* **angle**: `float` - angle of shear specified in radians


Updated on November 04, 2020 20:45:44pm UTC

