.. title: no_stroke()
.. slug: no_stroke
.. date: 2021-02-13 18:02:35 UTC+00:00
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

Disables drawing the stroke (outline). If both ``no_stroke()`` and ``no_fill()`` are called, nothing will be drawn to the screen.

Underlying Java method: `noStroke <https://processing.org/reference/noStroke_.html>`_

Syntax
======

.. code:: python

    no_stroke() -> None

Updated on February 13, 2021 18:02:35pm UTC

