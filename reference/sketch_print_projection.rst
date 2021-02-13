.. title: print_projection()
.. slug: print_projection
.. date: 2021-02-13 18:02:35 UTC+00:00
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

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
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

Prints the current projection matrix to the Console (the text window at the bottom of Processing).

Underlying Java method: `printProjection <https://processing.org/reference/printProjection_.html>`_

Syntax
======

.. code:: python

    print_projection() -> None

Updated on February 13, 2021 18:02:35pm UTC

