.. title: reset_matrix()
.. slug: reset_matrix
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 reset_matrix() documentation
.. type: text

Replaces the current matrix with the identity matrix.

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

    size(100, 100, P3D)
    no_fill()
    box(80)
    print_matrix()
    # prints:
    # 01.0000  00.0000  00.0000 -50.0000
    # 00.0000  01.0000  00.0000 -50.0000
    # 00.0000  00.0000  01.0000 -86.6025
    # 00.0000  00.0000  00.0000  01.0000

    reset_matrix()
    box(80)
    print_matrix()
    # prints:
    # 1.0000  0.0000  0.0000  0.0000
    # 0.0000  1.0000  0.0000  0.0000
    # 0.0000  0.0000  1.0000  0.0000
    # 0.0000  0.0000  0.0000  1.0000

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Replaces the current matrix with the identity matrix. The equivalent function in OpenGL is ``gl_load_identity()``.

Underlying Java method: `resetMatrix <https://processing.org/reference/resetMatrix_.html>`_

Syntax
======

.. code:: python

    reset_matrix() -> None

Updated on November 10, 2020 15:41:45pm UTC

