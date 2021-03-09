.. title: asin()
.. slug: asin
.. date: 2021-03-09 14:45:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 asin() documentation
.. type: text

The inverse of :doc:`sin`, returns the arc sine of a value.

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
        a = py5.PI/3
        s = py5.sin(a)
        a_s = py5.asin(s)
        # prints "1.04719757 : 0.86602541 : 1.04719757"
        print(round(a, 8), ':', round(s, 8), ':', round(a_s, 8))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = py5.PI + py5.PI/3
        s = py5.sin(a)
        a_s = py5.asin(s)
        # prints "4.18879027 : -0.86602543 : -1.04719761"
        print(round(a, 8), ':', round(s, 8), ':', round(a_s, 8))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The inverse of :doc:`sin`, returns the arc sine of a value. This function expects the values in the range of -1 to 1 and values are returned in the range ``-HALF_PI`` to ``HALF_PI``.

This function makes a call to the numpy ``asin()`` function.

Syntax
======

.. code:: python

    asin(value: float) -> float

Parameters
==========

* **value**: `float` - value in the range of -1 to 1 whose arc sine is to be returned


Updated on March 09, 2021 14:45:46pm UTC

