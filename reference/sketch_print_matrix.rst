.. title: print_matrix()
.. slug: print_matrix
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 print_matrix() documentation
.. type: text

Prints the current matrix to standard output.

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
        py5.size(100, 100, py5.P3D)
        py5.print_matrix()
        # prints:
        # 01.0000  00.0000  00.0000 -50.0000
        # 00.0000  01.0000  00.0000 -50.0000
        # 00.0000  00.0000  01.0000 -86.6025
        # 00.0000  00.0000  00.0000  01.0000

        py5.reset_matrix()
        py5.print_matrix()
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

Prints the current matrix to standard output.

Underlying Java method: `printMatrix <https://processing.org/reference/printMatrix_.html>`_

Syntax
======

.. code:: python

    print_matrix() -> None

Updated on June 28, 2021 15:16:14pm UTC

