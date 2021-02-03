.. title: create_font_file()
.. slug: create_font_file
.. date: 2021-02-03 22:21:58 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_font_file() documentation
.. type: text

Utility function to create Processing's vlw font data files.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    py5.create_font_file('Comic Sans', 20)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    for size in [10, 12, 15, 20]:
        py5.create_font_file('Comic Sans', 20, f'comic_sans_{size}.vlw', characters='abcde', pause=False)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Utility function to create Processing's vlw font data files. In Processing, users would create these files through the PDE using the Create Font tool. This utility function accomplishes the same task.

This function creates a small helper sketch to create a font file. Do not use this function inside of another sketch.

By default it will create data files for every character available in the specified font. To reduce execution time and output file size, limit the characters using the ``characters`` parameter. The default output filename is ``{font_name}-{font_size}.vlw`` and will be saved to the current directory.

This utility function opens a window that displays a short message about the number of glyphs written to the file. To make the window close automatically, set the ``pause`` parameter to ``False``.

Get a list of font names available on your computer with Py5Font's :doc:`py5font_list` method. If you request an unavailable font, it will create the data file anyway but using a default font.

Syntax
======

.. code:: python

    create_font_file(font_name: str, font_size: int, filename: str = None, characters: str = None, pause: bool = True) -> None

Parameters
==========

* **characters**: `str = None` - limit glyphs to characters found in string
* **filename**: `str = None` - vlw data file to save font data to
* **font_name**: `str` - name of font found on computer
* **font_size**: `int` - font size in units of pixels
* **pause**: `bool = True` - pause after creating font file


Updated on February 03, 2021 22:21:58pm UTC

