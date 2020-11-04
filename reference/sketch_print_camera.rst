.. title: print_camera()
.. slug: sketch_print_camera
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 print_camera() documentation
.. type: text

Prints the current camera matrix to the Console (the text window at the bottom of Processing).

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
    print_camera()

    # the program above prints this data:
    # 01.0000  00.0000  00.0000 -50.0000
    # 00.0000  01.0000  00.0000 -50.0000
    # 00.0000  00.0000  01.0000 -86.6025
    # 00.0000  00.0000  00.0000  01.0000

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Prints the current camera matrix to the Console (the text window at the bottom of Processing).

Underlying Java method: `printCamera <https://processing.org/reference/printCamera_.html>`_

Syntax
======

.. code:: python

    print_camera() -> None

Updated on November 04, 2020 20:45:44pm UTC

