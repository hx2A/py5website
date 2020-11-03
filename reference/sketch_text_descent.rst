.. title: text_descent()
.. slug: sketch_text_descent
.. date: 2020-11-03 22:19:57 UTC+00:00
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

Syntax
======

.. code:: python

    text_descent() -> float

Updated on November 03, 2020 22:19:57pm UTC

