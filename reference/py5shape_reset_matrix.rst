.. title: reset_matrix()
.. slug: py5shape_reset_matrix
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 reset_matrix() documentation
.. type: text

Replaces the current matrix of a shape with the identity matrix.

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
        s = py5.load_shape("ohio.svg")
        s.rotate(py5.PI/6)


    def draw():
        py5.background(204)
        py5.shape(s)


    def mouse_pressed():
        # removes all transformations applied to shape
        # loads the identity matrix
        s.reset_matrix()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Replaces the current matrix of a shape with the identity matrix. The equivalent function in OpenGL is ``gl_load_identity()``.

Underlying Java method: `PShape.resetMatrix <https://processing.org/reference/PShape_resetMatrix_.html>`_

Syntax
======

.. code:: python

    reset_matrix() -> None

Updated on February 13, 2021 18:02:35pm UTC

