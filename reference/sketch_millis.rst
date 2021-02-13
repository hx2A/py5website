.. title: millis()
.. slug: millis
.. date: 2021-02-13 18:02:35 UTC+00:00
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
        m = py5.millis()
        py5.no_stroke()
        py5.fill(m % 255)
        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns the number of milliseconds (thousandths of a second) since starting the program. This information is often used for timing events and animation sequences.

Underlying Java method: `millis <https://processing.org/reference/millis_.html>`_

Syntax
======

.. code:: python

    millis() -> int

Updated on February 13, 2021 18:02:35pm UTC

