.. title: width()
.. slug: py5font_width
.. date: 2021-04-14 15:10:22 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 width() documentation
.. type: text

Get the width of a character in this font.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_width_0.png
    :alt: example picture for width()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        font_size = 45
        font = py5.create_font('DejaVu Sans', font_size, True, 'py5')
        py5.text_font(font)

        x = 10
        py5.text('py5', x, py5.height / 2)
        py5.line(x, 0, x, py5.height)

        for c in list('py5'):
            x += font.width(c) * font_size
            py5.line(x, 0, x, py5.height)

        print(font.width('x'))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the width of a character in this font. The value is based on a font of size 1. Multiply it by the font size to get the horizontal space of the character.

This will return 0 if the character is not in the font's character set.

Underlying Java method: PFont.width

Syntax
======

.. code:: python

    width(c: chr, /) -> float

Parameters
==========

* **c**: `chr` - single character


Updated on April 14, 2021 15:10:22pm UTC

