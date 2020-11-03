.. title: reset_matrix()
.. slug: sketch_reset_matrix
.. date: 2020-11-03 22:19:57 UTC+00:00
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

Syntax
======

.. code:: python

    reset_matrix() -> None

Updated on November 03, 2020 22:19:57pm UTC

