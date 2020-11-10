.. title: height
.. slug: py5shape_height
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 height documentation
.. type: text

The height of the PShape document.

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
        print(s.height)  # prints "281.0", the height of the shape

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The height of the PShape document.

Underlying Java field: `PShape.height <https://processing.org/reference/PShape_height.html>`_


Updated on January 01, 1970 00:00:00am UTC

