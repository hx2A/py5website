.. title: print_projection()
.. slug: sketch_print_projection
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 print_projection() documentation
.. type: text

Prints the current projection matrix to the Console (the text window at the bottom of Processing).

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
    print_projection()

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

Prints the current projection matrix to the Console (the text window at the bottom of Processing).

Underlying Java method: `printProjection <https://processing.org/reference/printProjection_.html>`_

Syntax
======

.. code:: python

    print_projection() -> None

Updated on November 04, 2020 20:45:44pm UTC

