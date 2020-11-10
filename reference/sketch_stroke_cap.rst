.. title: stroke_cap()
.. slug: stroke_cap
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 stroke_cap() documentation
.. type: text

Sets the style for rendering line endings.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_cap_0.png
    :alt: example picture for stroke_cap()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    stroke_weight(12.0)
    stroke_cap(ROUND)
    line(20, 30, 80, 30)
    stroke_cap(SQUARE)
    line(20, 50, 80, 50)
    stroke_cap(PROJECT)
    line(20, 70, 80, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the style for rendering line endings. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: SQUARE, PROJECT, and ROUND. The default cap is ROUND.

To make ``point()`` appear square, use ``stroke_cap(PROJECT)``. Using ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.

Underlying Java method: `strokeCap <https://processing.org/reference/strokeCap_.html>`_

Syntax
======

.. code:: python

    stroke_cap(cap: int) -> None

Parameters
==========

* **cap**: `int` - either SQUARE, PROJECT, or ROUND


Updated on January 01, 1970 00:00:00am UTC

