.. title: millis()
.. slug: sketch_millis
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 millis() documentation
.. type: text

Returns the number of milliseconds (thousandths of a second) since starting the program.

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

    def draw():
        m = millis()
        no_stroke()
        fill(m % 255)
        rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns the number of milliseconds (thousandths of a second) since starting the program. This information is often used for timing events and animation sequences.

Syntax
======

.. code:: python

    millis() -> int

Updated on November 03, 2020 22:19:57pm UTC

