.. title: set_matrix()
.. slug: set_matrix
.. date: 2021-04-11 15:29:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_matrix() documentation
.. type: text

Set the current matrix to the one specified through the parameter ``source``.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_set_matrix_0.png
    :alt: example picture for set_matrix()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.no_fill()
        matrix = np.array([[0.866025, 0, 0.5, 0],
                           [0, 1, 0, 0],
                           [-0.5, 0, 0.866025, -86.6025],
                           [0, 0, 0, 1]], dtype=np.float64)
        py5.set_matrix(matrix)
        py5.stroke(153)
        py5.box(50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set the current matrix to the one specified through the parameter ``source``. Inside the Processing code it will call :doc:`reset_matrix` followed by :doc:`apply_matrix`. This will be very slow because :doc:`apply_matrix` will try to calculate the inverse of the transform, so avoid it whenever possible.

Underlying Java method: setMatrix

Syntax
======

.. code:: python

    set_matrix(source: NDArray[(2, 3), Float], /) -> None
    set_matrix(source: NDArray[(4, 4), Float], /) -> None

Parameters
==========

* **source**: `NDArray[(2, 3), Float]` - transformation matrix data
* **source**: `NDArray[(4, 4), Float]` - transformation matrix data


Updated on April 11, 2021 15:29:44pm UTC

