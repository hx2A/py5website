.. title: list()
.. slug: py5font_list
.. date: 2020-11-03 22:19:57 UTC+00:00
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

    size(200, 200)
    font_list = Py5Font.list()
    print_array(font_list)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Gets a list of the fonts installed on the system. The data is returned as a String array. This list provides the names of each font for input into ``create_font()``, which allows Processing to dynamically format fonts.

Syntax
======

.. code:: python

    list() -> List[str]

Updated on November 03, 2020 22:19:57pm UTC

