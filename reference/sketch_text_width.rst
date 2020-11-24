.. title: text_width()
.. slug: text_width
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_width() documentation
.. type: text

Calculates and returns the width of any character or text string.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_width_0.png
    :alt: example picture for text_width()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    text_size(28)

    c = 't'
    cw = text_width(c)
    text(c, 0, 40)
    line(cw, 0, cw, 50)

    s = "Tokyo"
    sw = text_width(s)
    text(s, 0, 85)
    line(sw, 50, sw, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates and returns the width of any character or text string.

Underlying Java method: `textWidth <https://processing.org/reference/textWidth_.html>`_

Syntax
======

.. code:: python

    text_width(c: chr, /) -> float
    text_width(chars: List[chr], start: int, length: int, /) -> float
    text_width(str: str, /) -> float

Parameters
==========

* **c**: `chr` - the character to measure
* **chars**: `List[chr]` - missing variable description
* **length**: `int` - missing variable description
* **start**: `int` - missing variable description
* **str**: `str` - the String of characters to measure


Updated on November 24, 2020 21:22:32pm UTC

