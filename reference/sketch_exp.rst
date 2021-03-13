.. title: exp()
.. slug: exp
.. date: 2021-03-13 17:44:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 exp() documentation
.. type: text

Returns Euler's number e (2.71828...) raised to the power of the ``n`` parameter.

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
        v1 = py5.exp(1.0)
        print(v1)  # Prints "2.718281828459045"

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns Euler's number e (2.71828...) raised to the power of the ``n`` parameter. This function is the compliment to :doc:`log`.

This function makes a call to the numpy ``exp()`` function.

Syntax
======

.. code:: python

    exp(value: float) -> float

Parameters
==========

* **value**: `float` - exponent to raise


Updated on March 13, 2021 17:44:45pm UTC

