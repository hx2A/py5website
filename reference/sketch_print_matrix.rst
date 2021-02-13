.. title: print_matrix()
.. slug: print_matrix
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
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

Prints the current matrix to the Console (the text window at the bottom of Processing).

Underlying Java method: `printMatrix <https://processing.org/reference/printMatrix_.html>`_

Syntax
======

.. code:: python

    print_matrix() -> None

Updated on February 13, 2021 18:02:35pm UTC

