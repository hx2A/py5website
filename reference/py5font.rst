.. title: Py5Font
.. slug: py5font
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Font documentation
.. type: text

Py5Font is the font class for py5.

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

Py5Font is the font class for py5. To create a font to use with py5, use :doc:`create_font_file`. This will create a font in the format py5 requires. Py5 displays fonts using the .vlw font format, which uses images for each letter, rather than defining them through vector data. The :doc:`load_font` function constructs a new font and :doc:`text_font` makes a font active. The :doc:`py5font_list` method creates a list of the fonts installed on the computer, which is useful information to use with the :doc:`create_font` function for dynamically converting fonts into a format to use with py5.

To create a new font dynamically, use the :doc:`create_font` function. Do not use the syntax ``Py5Font()``.

Underlying Java class: `PFont <https://processing.org/reference/PFont.html>`_

This class provides the following methods and fields:

.. include:: include/py5font_include.rst

Updated on March 03, 2021 21:11:14pm UTC

