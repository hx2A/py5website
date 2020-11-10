.. title: second()
.. slug: second
.. date: 2020-11-10 15:41:45 UTC+00:00
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

Underlying Java method: `second <https://processing.org/reference/second_.html>`_

Syntax
======

.. code:: python

    second() -> int

Updated on November 10, 2020 15:41:45pm UTC

