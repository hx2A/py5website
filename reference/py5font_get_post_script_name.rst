.. title: get_post_script_name()
.. slug: py5font_get_post_script_name
.. date: 2021-04-14 13:17:06 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_post_script_name() documentation
.. type: text

Get the font's postscript name.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_get_post_script_name_0.png
    :alt: example picture for get_post_script_name()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        font = py5.create_font('FreeSans', 15)
        py5.text_font(font)

        py5.text(font.get_name(), 5, 20)
        py5.text(font.get_post_script_name(), 5, 40)
        py5.text(font.get_size(), 5, 60)
        py5.text(font.get_default_size(), 5, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the font's postscript name.

Underlying Java method: PFont.getPostScriptName

Syntax
======

.. code:: python

    get_post_script_name() -> str

Updated on April 14, 2021 13:17:06pm UTC

