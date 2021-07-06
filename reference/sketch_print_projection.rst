.. title: print_projection()
.. slug: print_projection
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 print_projection() documentation
.. type: text

Prints the current projection matrix to standard output.

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
        py5.print_projection()

        # the program above prints this data:
        # 01.7321  00.0000  00.0000  00.0000
        # 00.0000 -01.7321  00.0000  00.0000
        # 00.0000  00.0000 -01.0202 -17.4955
        # 00.0000  00.0000 -01.0000  00.0000

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Prints the current projection matrix to standard output.

Underlying Java method: `printProjection <https://processing.org/reference/printProjection_.html>`_

Syntax
======

.. code:: python

    print_projection() -> None

Updated on June 28, 2021 15:16:14pm UTC

