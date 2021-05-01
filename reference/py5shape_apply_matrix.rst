.. title: Py5Shape.apply_matrix()
.. slug: py5shape_apply_matrix
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.apply_matrix() documentation
.. type: text

Apply a transformation matrix to a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        s = py5.create_shape(py5.RECT, -40, -40, 80, 80)


    def draw():
        py5.background(255)
        if py5.is_mouse_pressed:
            s.apply_matrix(0.99, 0, 0, 0, 0.99, 0)
        else:
            s.reset_matrix()
        py5.shape(s, py5.width / 2, py5.height / 2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Apply a transformation matrix to a ``Py5Shape`` object. This can be used to scale, rotate, and translate a shape with one call.

Making productive use of this method requires some knowledge of 2D or 3D transformation matrices, and perhaps some knowledge of Processing's source code.

Transformations are cummulative and therefore will be applied on top of existing transformations. Use :doc:`py5shape_reset_matrix` to set the transformation matrix to the identity matrix.

Underlying Java method: PShape.applyMatrix

Syntax
======

.. code:: python

    apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
    apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
    apply_matrix(source: NDArray[(2, 3), Float], /) -> None
    apply_matrix(source: NDArray[(4, 4), Float], /) -> None

Parameters
==========

* **n00**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n01**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n02**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n03**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n10**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n11**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n12**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n13**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n20**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n21**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n22**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n23**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n30**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n31**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n32**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n33**: `float` - numbers which define the 4x4 matrix to be multiplied
* **source**: `NDArray[(2, 3), Float]` - 2D transformation matrix
* **source**: `NDArray[(4, 4), Float]` - 3D transformation matrix


Updated on May 01, 2021 20:51:42pm UTC

