.. title: list()
.. slug: py5font_list
.. date: 2021-02-03 23:35:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 list() documentation
.. type: text

Gets a list of the fonts installed on the system.

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

    font_list = Py5Font.list()
    print(font_list)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Gets a list of the fonts installed on the system. The data is returned as a list of strings. This list provides the names of each font for input into ``create_font()``, which allows py5 to dynamically format fonts.

Underlying Java method: `PFont.list <https://processing.org/reference/PFont_list_.html>`_

Syntax
======

.. code:: python

    list() -> List[str]

Updated on February 03, 2021 23:35:44pm UTC

