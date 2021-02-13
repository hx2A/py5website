.. title: second()
.. slug: second
.. date: 2021-02-13 18:02:35 UTC+00:00
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
        py5.background(204)
        s = py5.second()  # values from_ 0 - 59
        m = py5.minute()  # values from_ 0 - 59
        h = py5.hour()    # values from_ 0 - 23
        py5.line(s, 0, s, 33)
        py5.line(m, 33, m, 66)
        py5.line(h, 66, h, 100)

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

Updated on February 13, 2021 18:02:35pm UTC

