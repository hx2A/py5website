.. title: Py5Font.get_name()
.. slug: py5font_get_name
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Font.get_name() documentation
.. type: text

Get the font's name.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_get_name_0.png
    :alt: example picture for get_name()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        font = py5.create_font('DejaVu Sans', 15)
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

Get the font's name.

Underlying Java method: PFont.getName

Syntax
======

.. code:: python

    get_name() -> str

Updated on May 01, 2021 20:51:42pm UTC

