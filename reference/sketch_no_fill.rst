.. title: no_fill()
.. slug: no_fill
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_fill() documentation
.. type: text

Disables filling geometry.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_no_fill_0.png
    :alt: example picture for no_fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect(15, 10, 55, 55)
        py5.no_fill()
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Disables filling geometry. If both :doc:`no_stroke` and ``no_fill()`` are called, nothing will be drawn to the screen.

Underlying Java method: `noFill <https://processing.org/reference/noFill_.html>`_

Syntax
======

.. code:: python

    no_fill() -> None

Updated on March 03, 2021 21:11:14pm UTC

