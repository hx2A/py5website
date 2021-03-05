.. title: no_stroke()
.. slug: no_stroke
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_stroke() documentation
.. type: text

Disables drawing the stroke (outline).

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_no_stroke_0.png
    :alt: example picture for no_stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Disables drawing the stroke (outline). If both ``no_stroke()`` and :doc:`no_fill` are called, nothing will be drawn to the screen.

Underlying Java method: `noStroke <https://processing.org/reference/noStroke_.html>`_

Syntax
======

.. code:: python

    no_stroke() -> None

Updated on March 03, 2021 21:11:14pm UTC

