.. title: width
.. slug: py5shape_width
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 width documentation
.. type: text

The width of the PShape document.

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

    def setup():
        global s
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = load_shape("bot.svg")
        print(s.width)  # prints "281.0", the width of the shape

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The width of the PShape document.

Underlying Java field: `PShape.width <https://processing.org/reference/PShape_width.html>`_


Updated on January 01, 1970 00:00:00am UTC

