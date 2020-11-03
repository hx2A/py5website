.. title: second()
.. slug: sketch_second
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 second() documentation
.. type: text

Processing communicates with the clock on your computer.

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
        background(204)
        s = second()  # values from_ 0 - 59
        m = minute()  # values from_ 0 - 59
        h = hour()    # values from_ 0 - 23
        line(s, 0, s, 33)
        line(m, 33, m, 66)
        line(h, 66, h, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Processing communicates with the clock on your computer. The ``second()`` function returns the current second as a value from 0 - 59.

Syntax
======

.. code:: python

    second() -> int

Updated on November 03, 2020 22:19:57pm UTC

