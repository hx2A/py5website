.. title: year()
.. slug: year
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 year() documentation
.. type: text

Py5 communicates with the clock on your computer.

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
        d = py5.day()    # values from_ 1 - 31
        m = py5.month()  # values from_ 1 - 12
        y = py5.year()   # 2003, 2004, 2005, etc.
    
        py5.text(str(d), 10, 28)
        py5.text(str(m), 10, 56)
        py5.text(str(y), 10, 84)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Py5 communicates with the clock on your computer. The ``year()`` function returns the current year as an integer (2003, 2004, 2005, etc).

Underlying Java method: `year <https://processing.org/reference/year_.html>`_

Syntax
======

.. code:: python

    year() -> int

Updated on March 03, 2021 21:11:14pm UTC

