.. title: print_matrix()
.. slug: print_matrix
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 print_matrix() documentation
.. type: text

Prints the current matrix to the Console (the text window at the bottom of Processing).

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
    print_matrix()
    # prints:
    # 01.0000  00.0000  00.0000 -50.0000
    # 00.0000  01.0000  00.0000 -50.0000
    # 00.0000  00.0000  01.0000 -86.6025
    # 00.0000  00.0000  00.0000  01.0000

    reset_matrix()
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

Prints the current matrix to the Console (the text window at the bottom of Processing).

Underlying Java method: `printMatrix <https://processing.org/reference/printMatrix_.html>`_

Syntax
======

.. code:: python

    print_matrix() -> None

Updated on January 01, 1970 00:00:00am UTC

