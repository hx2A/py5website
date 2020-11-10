.. title: text_descent()
.. slug: text_descent
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_descent() documentation
.. type: text

Returns descent of the current font at its current size.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_descent_0.png
    :alt: example picture for text_descent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    base = height * 0.75
    scalar = 0.8  # different for each font

    text_size(32)  # set initial text size
    a = text_descent() * scalar  # calc ascent
    line(0, base+a, width, base+a)
    text("dp", 0, base)  # draw text on baseline

    text_size(64)  # increase text size
    a = text_descent() * scalar  # recalc ascent
    line(40, base+a, width, base+a)
    text("dp", 40, base)  # draw text on baseline

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns descent of the current font at its current size. This information is useful for determining the height of the font below the baseline.

Underlying Java method: `textDescent <https://processing.org/reference/textDescent_.html>`_

Syntax
======

.. code:: python

    text_descent() -> float

Updated on November 10, 2020 15:41:45pm UTC

