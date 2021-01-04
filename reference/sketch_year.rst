.. title: year()
.. slug: year
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 year() documentation
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

Processing communicates with the clock on your computer. The ``year()`` function returns the current year as an integer (2003, 2004, 2005, etc).

Underlying Java method: `year <https://processing.org/reference/year_.html>`_

Syntax
======

.. code:: python

    year() -> int

Updated on November 10, 2020 15:41:45pm UTC
