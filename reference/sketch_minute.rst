.. title: minute()
.. slug: minute
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 minute() documentation
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

Processing communicates with the clock on your computer. The ``minute()`` function returns the current minute as a value from 0 - 59.

Underlying Java method: `minute <https://processing.org/reference/minute_.html>`_

Syntax
======

.. code:: python

    minute() -> int

Updated on January 01, 1970 00:00:00am UTC

