.. title: get_default_size()
.. slug: py5font_get_default_size
.. date: 2021-04-14 13:17:06 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_default_size() documentation
.. type: text

Get the font's size that will be used when :doc:`text_font` is called.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_get_default_size_0.png
    :alt: example picture for get_default_size()

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

Get the font's size that will be used when :doc:`text_font` is called. When drawing with 2x pixel density, bitmap fonts in OpenGL need to be created at double the requested size. This ensures that they're shown at half on displays (so folks don't have to change their sketch code).

Underlying Java method: PFont.getDefaultSize

Syntax
======

.. code:: python

    get_default_size() -> int

Updated on April 14, 2021 13:17:06pm UTC

