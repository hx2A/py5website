.. title: text_align()
.. slug: sketch_text_align
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_align() documentation
.. type: text

Sets the current alignment for drawing text.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_align_0.png
    :alt: example picture for text_align()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    background(0)
    text_size(16)
    text_align(RIGHT)
    text("ABCD", 50, 30)
    text_align(CENTER)
    text("EFGH", 50, 50)
    text_align(LEFT)
    text("IJKL", 50, 70)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_align_1.png
    :alt: example picture for text_align()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    background(0)
    stroke(153)
    text_size(11)
    text_align(CENTER, BOTTOM)
    line(0, 30, width, 30)
    text("CENTER,BOTTOM", 50, 30)
    text_align(CENTER, CENTER)
    line(0, 50, width, 50)
    text("CENTER,CENTER", 50, 50)
    text_align(CENTER, TOP)
    line(0, 70, width, 70)
    text("CENTER,TOP", 50, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the current alignment for drawing text. The parameters LEFT, CENTER, and RIGHT set the display characteristics of the letters in relation to the values for the ``x`` and ``y`` parameters of the ``text()`` function.
 
An optional second parameter can be used to vertically align the text. BASELINE is the default, and the vertical alignment will be reset to BASELINE if the second parameter is not used. The TOP and CENTER parameters are straightforward. The BOTTOM parameter offsets the line based on the current ``text_descent()``. For multiple lines, the final line will be aligned to the bottom, with the previous lines appearing above it.
 
When using ``text()`` with width and height parameters, BASELINE is ignored, and treated as TOP. (Otherwise, text would by default draw outside the box, since BASELINE is the default setting. BASELINE is not a useful drawing mode for text drawn in a rectangle.)
 
The vertical alignment is based on the value of ``text_ascent()``, which many fonts do not specify correctly. It may be necessary to use a hack and offset by a few pixels by hand so that the offset looks correct. To do this as less of a hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the hack works even if you change the size of the font.

Syntax
======

.. code:: python

    text_align(align_x: int) -> None
    text_align(align_x: int, align_y: int) -> None

Parameters
==========

* **align_x**: `int` - horizontal alignment, either LEFT, CENTER, or RIGHT
* **align_y**: `int` - vertical alignment, either TOP, BOTTOM, CENTER, or BASELINE


Updated on November 03, 2020 22:19:57pm UTC

