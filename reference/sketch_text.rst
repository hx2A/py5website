.. title: text()
.. slug: text
.. date: 2021-02-28 03:31:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text() documentation
.. type: text

Draws text to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_0.png
    :alt: example picture for text()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.text_size(32)
        py5.text("word", 10, 30)
        py5.fill(0, 102, 153)
        py5.text("word", 10, 60)
        py5.fill(0, 102, 153, 51)
        py5.text("word", 10, 90)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_1.png
    :alt: example picture for text()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.text_size(32)
        py5.fill(0, 102, 153, 204)
        py5.text("word", 12, 45, -30)  # specify a z-axis value
        py5.text("word", 12, 60)  # default depth, no z-value specified

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_2.png
    :alt: example picture for text()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = "The quick brown fox jumps over the lazy dog."
        py5.fill(50)
        py5.text(s, 10, 10, 70, 80)  # text wraps within text box

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draws text to the screen. Displays the information specified in the first parameter on the screen in the position specified by the additional parameters. A default font will be used unless a font is set with the ``text_font()`` function and a default size will be used unless a font is set with ``text_size()``. Change the color of the text with the ``fill()`` function. The text displays in relation to the ``text_align()`` function, which gives the option to draw to the left, right, and center of the coordinates.

The ``x2`` and ``y2`` parameters define a rectangular area to display within and may only be used with string data. When these parameters are specified, they are interpreted based on the current ``rect_mode()`` setting. Text that does not fit completely within the rectangle specified will not be drawn to the screen.

Note that py5 lets you call ``text()`` without first specifying a Py5Font with ``text_font()``. In that case, a generic sans-serif font will be used instead. (See the third example.)

Underlying Java method: `text <https://processing.org/reference/text_.html>`_

Syntax
======

.. code:: python

    text(c: chr, x: float, y: float, /) -> None
    text(c: chr, x: float, y: float, z: float, /) -> None
    text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
    text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
    text(num: float, x: float, y: float, /) -> None
    text(num: float, x: float, y: float, z: float, /) -> None
    text(num: int, x: float, y: float, /) -> None
    text(num: int, x: float, y: float, z: float, /) -> None
    text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
    text(str: str, x: float, y: float, /) -> None
    text(str: str, x: float, y: float, z: float, /) -> None

Parameters
==========

* **c**: `chr` - the alphanumeric character to be displayed
* **chars**: `List[chr]` - the alphanumberic symbols to be displayed
* **num**: `float` - the numeric value to be displayed
* **num**: `int` - the numeric value to be displayed
* **start**: `int` - array index at which to start writing characters
* **stop**: `int` - array index at which to stop writing characters
* **str**: `str` - missing variable description
* **x1**: `float` - by default, the x-coordinate of text, see rectMode() for more info
* **x2**: `float` - by default, the width of the text box, see rectMode() for more info
* **x**: `float` - x-coordinate of text
* **y1**: `float` - by default, the y-coordinate of text, see rectMode() for more info
* **y2**: `float` - by default, the height of the text box, see rectMode() for more info
* **y**: `float` - y-coordinate of text
* **z**: `float` - z-coordinate of text


Updated on February 28, 2021 03:31:12am UTC

