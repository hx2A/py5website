.. title: day()
.. slug: day
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 day() documentation
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

    d = day()    # values from_ 1 - 31
    m = month()  # values from_ 1 - 12
    y = year()   # 2003, 2004, 2005, etc.

    s = string.value_of(d)
    text(s, 10, 28)
    s = string.value_of(m)
    text(s, 10, 56)
    s = string.value_of(y)
    text(s, 10, 84)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Processing communicates with the clock on your computer. The ``day()`` function returns the current day as a value from 1 - 31.

Underlying Java method: `day <https://processing.org/reference/day_.html>`_

Syntax
======

.. code:: python

    day() -> int

Updated on January 01, 1970 00:00:00am UTC

