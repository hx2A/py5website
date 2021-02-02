.. title: create_font_file()
.. slug: create_font_file
.. date: 2021-02-02 22:08:38 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_font_file() documentation
.. type: text

Utility function to create Processing's vlw font data files.

Description
===========

Utility function to create Processing's vlw font data files. In Processing, users would create these files through the PDE using the Create Font tool. This utility function accomplishes the same task.

By default it will create data files for every character available in the specified font. To reduce execution time and output file size, limit the characters using the ``characters`` parameter. The default output filename is ``{font_name}-{font_size}.vlw`` and will be saved to the current directory.

This utility function opens a window that displays a short message about the number of glyphs written to the file. To make the window close automatically, set the ``pause`` parameter to ``False``.

Get a list of font names available on your computer with Py5Font's :doc:`py5font_list` method.

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


Updated on February 02, 2021 22:08:38pm UTC

