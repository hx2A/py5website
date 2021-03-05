.. title: print_camera()
.. slug: print_camera
.. date: 2021-03-05 15:24:25 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 print_camera() documentation
.. type: text

Prints the current camera matrix to standard output.

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
        py5.print_camera()
    
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

Prints the current camera matrix to standard output.

Underlying Java method: `printCamera <https://processing.org/reference/printCamera_.html>`_

Syntax
======

.. code:: python

    print_camera() -> None

Updated on March 05, 2021 15:24:25pm UTC

