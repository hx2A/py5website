.. title: text_ascent()
.. slug: text_ascent
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_ascent() documentation
.. type: text

Returns ascent of the current font at its current size.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_ascent_0.png
    :alt: example picture for text_ascent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    base = height * 0.75
    scalar = 0.8  # different for each font

    text_size(32)  # set initial text size
    a = text_ascent() * scalar  # calc ascent
    line(0, base-a, width, base-a)
    text("dp", 0, base)  # draw text on baseline

    text_size(64)  # increase text size
    a = text_ascent() * scalar  # recalc ascent
    line(40, base-a, width, base-a)
    text("dp", 40, base)  # draw text on baseline

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns ascent of the current font at its current size. This information is useful for determining the height of the font above the baseline.

Underlying Java method: `textAscent <https://processing.org/reference/textAscent_.html>`_

Syntax
======

.. code:: python

    text_ascent() -> float

Updated on January 01, 1970 00:00:00am UTC

