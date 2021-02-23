.. title: width
.. slug: py5shape_width
.. date: 2021-02-23 16:06:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 width documentation
.. type: text

The width of the ``Py5Shape`` document.

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
        s = py5.load_shape("bot.svg")
        print(s.width)  # prints "281.0", the width of the shape

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The width of the ``Py5Shape`` document.

Underlying Java field: `PShape.width <https://processing.org/reference/PShape_width.html>`_


Updated on February 23, 2021 16:06:03pm UTC

