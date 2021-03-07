.. title: list()
.. slug: py5font_list
.. date: 2021-03-06 19:17:57 UTC+00:00
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

    font_list = py5.Py5Font.list()
    print(font_list)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Gets a list of the fonts installed on the system. The data is returned as a list of strings. This list provides the names of each font for input into :doc:`create_font`, which allows py5 to dynamically format fonts.

This works outside of a running Sketch.

Underlying Java method: `PFont.list <https://processing.org/reference/PFont_list_.html>`_

Syntax
======

.. code:: python

    list() -> List[str]

Updated on March 06, 2021 19:17:57pm UTC

