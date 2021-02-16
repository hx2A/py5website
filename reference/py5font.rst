.. title: Py5Font
.. slug: py5font
.. date: 2021-02-16 15:03:15 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Font documentation
.. type: text

PFont is the font class for Processing.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_0.png
    :alt: example picture for Py5Font

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        # the font must be located in the sketch's
        # "data" directory to load successfully
        font = py5.create_font("FreeSans.ttf", 32)
        py5.text_font(font)
        py5.text("word", 10, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

PFont is the font class for Processing. To create a font to use with Processing, select "Create Font..." from the Tools menu. This will create a font in the format Processing requires and also adds it to the current sketch's data directory. Processing displays fonts using the .vlw font format, which uses images for each letter, rather than defining them through vector data. The ``load_font()`` function constructs a new font and ``text_font()`` makes a font active. The ``list()`` method creates a list of the fonts installed on the computer, which is useful information to use with the ``create_font()`` function for dynamically converting fonts into a format to use with Processing.

To create a new font dynamically, use the ``create_font()`` function. Do not use the syntax ``new Py5Font()``.

Underlying Java class: `PFont <https://processing.org/reference/PFont.html>`_

This class provides the following methods and fields:

.. include:: include/py5font_include.rst

Updated on February 16, 2021 15:03:15pm UTC

